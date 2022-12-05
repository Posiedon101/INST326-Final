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
    def __init__(self, person, date, time, reason=None):
        """"""
    
        self.person = person 
        self.date = date
        self.time = time
        self.reason = reason 
        
        
    def add_appt(self, date):
        """Adds an appointment to the queue for that day"""
        
        queue = []
        
        queue.append(Appointment())
        
        return queue
    
    
    
    def remove_appt(self, date):
        """Removes an appointment from the queue for that day"""
        
    def edit_appt(self, person, date=None, time=None, reason=None):
        
        
def main(name, date, time):
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
    
def __str__(self):
       """""" 
    
def export():
    """Exports data into a specified file type. Those types could be any of 
        csv, txt, xls, etc. (We wont export to all only 1 or possibly 2)
    """
    
def parse_args(arglist):
    """Parse command-line arguments
        Expects the arguments, the path to a file of appointments
        
    Args:
        arglist (list): command line arguments.
    
    Returns:
        namespace: the parsed arguments, as a namespace. The arguments include
            name of the person, date of the appointment, and the time on that
            day.  
    """

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.name, args.date, args.time)