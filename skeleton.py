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
    """
    def __init__(self, person, date, time, reason, location):
        """"""
    
        self.person = person 
        self.date = date
        self.time = time
        self.reason = reason 
        self.location = location
        self.todays_appts = []
        
        
    def add_appt(self, date):
        """Adds an appointment to the queue for that day"""
        
        
        if self.date == date:
            todays_appts.append([self])
        
        
        return todays_appts
    
    
    
    def remove_appt(self, date):
        """Removes an appointment from the queue for that day"""
        if self.date == date:
            todays_appts.remove([self])

        return todays_appts
        
    def edit_appt(self, person, date=None, time=None, reason=None, 
                  location = None):
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
            """A representation of what the User would see
            
            Returns:
                String: A message of what would appear when the User schedules 
                an appointment""" 
                
            return f"""Your appointment has been made for {Appointment.date} at 
            {Appointment.time} about {Appointment.reason},  
            {Appointment.location}"""
        
        
def main(filepath):
    """ Main method will take 3 arguments given by the user on the command line
        from the parse_args. It will create a Person object using the name
        provided in the user input. Next an appointment will be made using the
        Person object, the date, the time, and the optional reason for the 
        appointment. Main will also allow for the editing of pre-existing 
        appointments.
        
        Args:
            name(str): Name of the person
            date(str): Appointment Date
            time(str): Appointment Time 
    
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
                todays_appts = i.add_appt(current_day)
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
    

    
def export(df):
    """Exports data into a specified file type. Those types could be any of 
        csv, txt, xls, etc. (We wont export to all only 1 or possibly 2)
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
    """
    parser = ArgumentParser()
    parser.add_argument("file", help= "file of pre-made appointments")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)