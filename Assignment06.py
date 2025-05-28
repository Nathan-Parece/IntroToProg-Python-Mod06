# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   NParece, 5/28/2025, Created Script
# ------------------------------------------------------------------------------------------ #

import json


# Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Variables
students: list = []  # A table of student data
menu_choice: str = ''  # Holds the choice made by the user

# Classes
class FileProcessor:
    """
    A collection of functions that read and write JSON data to files

    ChangeLog: (Who, When, What)
    NParece,5.28.2025,Created Class
    NParece,5.28.2025,Added methods to read and write data
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads JSON data from a file into a local variable

        ChangeLog: (Who, When, What)
        NParece,5.28.2025,Created function

        :param file_name: Name of the file
        :param student_data: List of dicts containing student data
            (empty on initialization)

        :return: JSON data from referenced file
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
        except FileNotFoundError as e:
            IO.output_error_messages(
                "Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages(
                "There was an unspecified error!", e)
        finally:
            try:
                file.close()
            except UnboundLocalError as e:
                IO.output_error_messages(
                    "You can't close a file that doesn't exist!", e)
            except Exception as e:
                IO.output_error_messages(
                    "There was an unspecified error!", e)

        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes JSON data from a variable into a text file

        ChangeLog: (Who, When, What)
        NParece,5.28.2025,Created function

        :param file_name: Name of the file
        :param student_data: List of dicts containing student data
            (defined during operation)

        :return: None
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            print("The following data was saved to file!")
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except TypeError as e:
            IO.output_error_messages(
                "Please ensure the data is in JSON format.", e)
        except Exception as e:
            IO.output_error_messages(
                "There was a problem with writing to the file.", e)
        finally:
            try:
                file.close()
            except UnboundLocalError as e:
                IO.output_error_messages(
                    "You can't close a file that doesn't exist!", e)
            except Exception as e:
                IO.output_error_messages(
                    "There was an unspecified error!", e)


class IO:
    """
    A collection of functions that handle input and output of student
    registration data, as well as navigation of an external text menu

    ChangeLog: (Who, When, What)
    NParece,5.28.2025,Created Class
    NParece,5.28.2025,Added methods to output the menu, errors,
    and registration data
    NParece,5.28.2025,Added methods to input menu choice and registration data
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function outputs formatted error messages to the console

        ChangeLog: (Who, When, What)
        NParece,5.28.2025,Created function

        :param message: Custom error message
        :param error: Python error data, defaults to None

        :return: None
        """
        print(message, end = "\n\n")

        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep = "\n")

    @staticmethod
    def output_menu(menu: str):
        """ This function prints a string to the console

        ChangeLog: (Who, When, What)
        NParece,5.28.2025,Created function

        :param menu: The string to be printed.
            This should always be the MENU global constant

        :return: None
        """
        print(menu)

    @staticmethod
    def input_menu_choice():
        """ This function handles user input to choose a menu option

        ChangeLog: (Who, When, What)
        NParece,5.28.2025,Created function

        :return: The menu choice string
        """
        choice: str = "0"

        try:
            choice = input("What would you like to do: ")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("Please choose a valid option!")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """ This function outputs all student registrations in csv format

        ChangeLog: (Who, When, What)
        NParece,5.28.2025,Created function

        :param student_data: List of dicts containing student data,
            including new entries

        :return: None
        """
        print("-" * 50)
        for student in student_data:
            print(f'{student["FirstName"]}, '
                  f'{student["LastName"]}, {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function allows a user to input one new student registration

        ChangeLog: (Who, When, What)
        NParece,5.28.2025,Created function

        :param student_data: List of dicts containing student data,
            including new entries

        :return: Updated list of student data
        """
        try:
            student_first_name: str = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should contain only letters.")
            student_last_name: str = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should contain only letters.")
            course_name: str = input("Please enter the name of the course: ")
            student: dict = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} "
                  f"for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(e.__str__(), e)
        except Exception as e:
            IO.output_error_messages(
                "There was a problem with your entered data.", e)
        return student_data


# When the program starts, read the file data into a list of dicts (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(FILE_NAME, students)

# Main Loop
while True:

    # Present the menu of choices
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":

        students = IO.input_student_data(students)
        continue

    # Present the current data
    elif menu_choice == "2":

        IO.output_student_courses(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":

        FileProcessor.write_data_to_file(FILE_NAME, students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

    else:
        continue # on an error or invalid menu choice

print("Program Ended")