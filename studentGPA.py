# M02 Lab - Case Study: if...else and while
# Author:Sisay Degefa
# File Name: student_qualification.py
# Description: This app accepts student names and GPAs, tests if the student qualifies for Dean's List or Honor Roll,
# and prints a corresponding message.

def check_qualification(first_name, last_name, gpa):
    # Test if the student's GPA is 3.5 or greater for Dean's List
    if gpa >= 3.5:
        return f"{first_name} {last_name} has made the Dean's List."
    
    # Test if the student's GPA is 3.25 or greater for Honor Roll
    elif gpa >= 3.25:
        return f"{first_name} {last_name} has made the Honor Roll."
    
    # If GPA is below 3.25, return no qualification message
    else:
        return f"{first_name} {last_name} does not qualify for Dean's List or Honor Roll."

def process_student_records():
    while True:
        # Ask for and accept a student's last name
        last_name = input("Enter student's last name (enter 'ZZZ' to quit): ")
        
        # Quit processing student records if the last name entered is 'ZZZ'
        if last_name == 'ZZZ':
            break
        
        # Ask for and accept a student's first name
        first_name = input("Enter student's first name: ")
        
        # Ask for and accept the student's GPA as a float
        gpa = float(input("Enter student's GPA: "))
        
        # Call the check_qualification function and print the result
        result = check_qualification(first_name, last_name, gpa)
        print(result)

# Call the process_student_records function to start the program
process_student_records()
