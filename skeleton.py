from argparse import ArgumentParser
import sys
import pandas as pd
    
class Appointment:
    """Creates an appointment object for the person. 
    
    Attributes:
        person (str): The name of the person that is creating the appointment
        date (str): Date that the appointment takes place on.
        time (str): Time of the day that the appointment takes place.
        reason (str): Brief explanation for the reason of the appointment 
            Defaults to None.
        location (str): The location the person wants to meet, In person or 
            online.
    """
    def __init__(self, person, date, time, reason, location):
        """Initializes the attributes of the Appointment Class"""
    
        self.person = person 
        self.date = date
        self.time = time
        self.reason = reason 
        self.location = location
        
    def add_appt(self, date, lst):
        """Adds an appointment to the queue for that day
        
        Written by Christian Marchello. Covers conditional expressions. 
        """
        if self.date == date:
            lst.append([self])
        return lst
    
    def remove_appt(self, date, lst):
        """Removes all appointments from the queue for that day
        
        Written by Rachel Van Culin. Covers conditional expressions. 
        """
        if self.date == date:
            lst.remove([self])
        return lst
        
    def edit_appt(self, person, date=None, time=None, reason=None, 
                  location = None):
        """Allows the user to edit the created appointment objects

        Args:
            person (str): Name of the person that the appointment object 
                            belongs to. 
            date (str, optional): Date of the appointment. Defaults to None.
            time (str, optional): Time of the appointment. Defaults to None.
            reason (str, optional): Reason for the appointment. 
                                        Defaults to None.
            location (str, optional): Location of the appointment. 
                                        Defaults to None.
        
        Written by Rachel Van Culin. Covers conditional expressions and 
        optional parameters.
        """
        if date is None:
            self.date = self.date
        else:
            self.date = date
        
        if time is None:
            self.time = self.time
        else:
            self.time = time
            
        if reason is None:
            self.reason = self.reason
        else:
            self.reason = reason
            
        if location is None:
            self.location = self.location
        else:
            self.location = location
            
    def __repr__(self):
        """A representation of what the appointment information
        
        Returns:
            String: A message of what would appear when the User schedules 
            an appointment
        
        Written by Jay Jean-Baptiste. Covers magic methods other than '__init__'
        and fstrings.
        """ 
            
        return f"""{self.person}, {self.date}, {self.time}, {self.reason}, 
                    {self.location}"""
            
    def __lt__(self, other):
        """Compares the time of 2 appointment objects. 

        Args:
            other (Appointment): 2nd appointment which to compare to the first. 

        Returns:
            bool: Returns True if the first time is earlier than the second.
            
        Written by Jason Carlin. Covers magic methods other than '__init__' 
        """
        if self.time < other.time:
            return True
        else:
            return False
        
        
def main(filepath):
    """ Main will take in 1 argument, a path to a file as a string. Main will
        then create a dataframe from the file that it takes in. Then it will 
        make instances of Appointment for each row in the dataframe. Main will 
        then prompt the use to either "1: Create Appointment", 
        "2: View Appointments for a specified day", "3: Edit a pre-existing 
        appointment" or "4: Quit the program". Once the user selects their 
        option they are then prompted further depending on what information 
        is needed from them to complete the action. Once they are done with 
        everything they will be prompted to clear the queue for that day.
        Finally, once the program is done with user input it will export any
        changes to any appointment object on the dataframe to a new csv file 
        so that next time the program is run all of the new/edited data will be 
        there. 
        
        Args:
            filepath(str): Path to a file with pre made appointments. 
            
        Side effects:
            Creates a new csv file. 
            
        Written by Jason Carlin. Covers conditional expressions, custom list 
        sorting, fstrings, and filtering with pandas. 
    """
    appointments = pd.read_csv("Appointments CSVs - Sheet1.csv")
    people = []
    repeat = ""

    for i in range(len(appointments)):
        person = Appointment(appointments.loc[i][0], appointments.loc[i][1], 
                             appointments.loc[i][2], appointments.loc[i][3], 
                             appointments.loc[i][4])
        people.append(person)
        
    while repeat != "n":
        main_dec = input("""Welcome to our Scheduler:\n
                            Please enter an option below:\n
                            1. Create Appointment\n
                            2. View Appointments for a day\n
                            3. Edit Appointment\n
                            4. Quit
                            """)

        if main_dec == "1":
            appt_info = (input("""Please enter Name, Date, Time (Format HH:MM), 
                               Reason, and Location for the appointment: 
                               """).strip().split(","))
            appt = Appointment(appt_info[0], appt_info[1], appt_info[2], 
                               appt_info[3], appt_info[4])
            appointments.loc[len(appointments)] = appt_info
            people.append(appt)
            repeat = input("Is there anything else you need? (y/n): ")
            

        elif main_dec == "2":
            current_day = input("What day would you like to view? ")
            todays_appts = []
            
            for i in people:
                todays_appts = i.add_appt(current_day, todays_appts)
            print(f"""Here are your appointments for today: 
                  {sorted(todays_appts)}""")
            repeat = input("Is there anything else you need? (y/n): ")


        elif main_dec == "3":
            edit=""
            username = input("Please enter your name: ")
            for i in people:
                if i.person == username:
                    current_appt = i
            print(f"Your current appointment information is: {current_appt}")        
            while edit != "5":
                edit = input("""What would you like to edit: \n
                            Please enter an option below: \n
                            1. Date\n
                            2. Time\n
                            3. Reason\n
                            4. Location\n
                            5. Quit
                            """)
                if edit == "1":
                    new_date = input("What would you like the new date to be: ")
                    current_appt.edit_appt(username, date=new_date)
                    print(repr(current_appt))
                    appointments.loc[appointments['Person']==username, 
                                     'Date'] = new_date
                elif edit == "2":
                    new_time = input("""What would you like the new time to be 
                                     (HH:MM format): """)
                    current_appt.edit_appt(username, time=new_time)
                    print(repr(current_appt))
                    appointments.loc[appointments['Person']==username, 
                                     'Time'] = new_time
                elif edit == "3":
                    new_reason = input("""What would you like the new 
                                       reason to be: """)
                    current_appt.edit_appt(username, reason=new_reason)
                    print(repr(current_appt))
                    appointments.loc[appointments['Person']==username, 
                                     'Reason'] = new_reason
                elif edit == "4":
                    new_location = input("""What would you like the new 
                                         location to be: """)
                    current_appt.edit_appt(username, location=new_location)
                    print(repr(current_appt))
                    appointments.loc[appointments['Person']==username, 
                                     'Location'] = new_location
                repeat = input("Is there anything else you need? (y/n): ")
                
                if repeat == "n":
                    break 
        else:
            repeat = "n"
    remove = input("""Would you like to remove appt from the queue for  
                    today? (y/n)""")
    
    if remove == "y":
        if len(todays_appts) == 0:
            print(f"There are no appointments to remove!")
        else:
            for i in people:
                todays_appts = i.remove_appt(current_day, todays_appts)
            print(f"The queue has been emptied for the day!")
    
    export(appointments)

def export(df):
    """Exports data into a csv file.
    
    Written by Jay Jean-Baptiste. 
    """
    df.to_csv("New_Appointment_File")
    
def parse_args(arglist):
    """Parse command-line arguments
        Expects the arguments, the path to a file of appointments
        
    Args:
        arglist (list): command line arguments.
    
    Returns:
        namespace: the parsed arguments, as a namespace. The arguments include
            path to a specified file with appointments. 
            
    Written by Jason Carlin. Covers the ArgumentParser class.   
    """
    parser = ArgumentParser()
    parser.add_argument("file", help= "file of pre-made appointments")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)