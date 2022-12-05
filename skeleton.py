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
        self.name = name 
        
        
    def add_person(self):
        """Adds a person object to the queue
        
        Args:
        
        """
        
        queue = []
        
        queue.append(Person(self.name))
        
        return queue
    
        
    def remove_person(self):
        """Removes a person object from the queue
        
        Args:
        """
    
def create_appt(person, time, day, reason=None):
    """Creates an appointment for the person. 
    
    Args:
        person (Person): The Person that is creating the appointment
        time (str): Time of the day that the appointment takes place.
        day (str): Day that the appointment takes place on.
        reason (str): Brief explanation for the reason of the appointment 
            Defaults to None.
            
    Returns:

    Side-effects:

    """
    
def __repr__(self):
    """Returns a formal representation of the appointment"""
        
def main():
    """_summary_
    """
    
def export():
    """Returns data (appt time, etc) in various forms, excel sheet, datafram, csv
    """
    
def parse_args():
    """_summary_
    """
    
    