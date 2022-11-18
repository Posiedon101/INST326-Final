from argparse import ArgumentParser
import sys

class Person:
    """Class that creates a Person object to represent the person that has 
        created an appointment for the scheduler
    
    Attributes:
        name (str): Name of the person
    """
    def __init__(self, name):
        """Creates Attributes of the Person Object
        
        Args:
            name (str): Name of the person. 
        """
    
class Appointment:
    """Creates an appointment object for the person object. 
    
    Attributes:
        person (Person): The Person that is creating the appointment
        date (str): Date that the appointment takes place on.
        time (str): Time of the day that the appointment takes place.
        reason (str): Brief explanation for the reason of the appointment 
            Defaults to None.
    """
    def __init__(self, person, date, time, reason=None):
        """"""
        
    def add_appt(self, date):
        """Adds an appointment to the queue for that day"""
    
    def remove_appt(self, date):
        """Removes an appointment from the queue for that day"""
        
def main(name, date, time):
    """_summary_
    
    """
    
def __repr__(self):
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