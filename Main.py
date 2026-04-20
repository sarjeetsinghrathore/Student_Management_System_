
from models.Student import Student
from Database.services.Student_services import Services

# Crreatig the object of the service class
ser = Services()
ser.create_table()

while True:
    print("1. Press 1 to add student\n2 Press 2 to view all the students\n3 Press 3 to update the student details\n4 Press 4 to delete the student\n5 Press 5 to exit")
    
    Option = int(input('Enter your Option: '))
    if Option == 1:
        id = input('Enter the student ID:')
        name = input('Enter the student name: ')
        age = int(input('Enter the age of the student: '))
        course = input('Enter the course details of the student: ')
        email = input('Enter the email of the student: ')
        
        obj = Student(id, name, age, course, email)
        ser.add_student(obj)
        print('The Student Added Successfully!')
    elif Option == 2:
        data = ser.view_students()
        if data:
            print("\n" + "="*90)
            print(f"{'ID':<10} {'Name':<25} {'Age':<10} {'Course':<20} {'Email':<25}")
            print("="*90)
            for student in data:
                print(f"{str(student[0]):<10} {str(student[1]):<25} {str(student[2]):<10} {str(student[3]):<20} {str(student[4]):<25}")
            print("="*90 + "\n")
        else:
            print("\nNo students found in the database!\n")
    elif Option == 3:
        id = int(input('Enter the student ID to update:'))
        name = input('Enter the new student name: ')
        age = int(input('Enter the new age of the student: '))
        course = input('Enter the new course details of the student: ')
        email = input('Enter the new email of the student: ')
        
        obj = Student(id, name, age, course, email)
        ser.update_student(id, obj)
        print('The Student Data Updated Successfully!')
    elif Option == 4:
        id = int(input('Enter the student ID to delete:'))
        ser.delete(id)
        print('The Student Data Deleted Successfully From The Database!')
    elif Option == 5:
        print('Exiting...')
        break
    else:
        print('Please Enter a Valid Option!')
