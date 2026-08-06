import json 
def get_valid_name() :
    while True :
        name = input("Enter your name : ")
        if name.replace(" ","").isalpha() :
            break
        else :
            print("Invalid Name.Please use alphabets only.")
    name = name.lower()
    return name
def add_student():
    Students = load_students()
    Student = {}
    Student["name"] = get_valid_name()
    Student["roll_no"] = get_valid_roll(Students)
    Student["age"] = get_valid_age()
    Student["marks"] = get_valid_marks()
    Student["result"]= calculate_result(Student["marks"])
    Students.append(Student)
    print("Student Added.")
    save_students(Students)
def get_valid_age():
    while True :
        try :
            age = int(input("Enter age: "))
            break
        except ValueError:
            print("Invalid input.Try again.")
    while age < 3:
        age = int(input("Enter valid age: "))
    return age
def get_valid_roll (Students):
    while True :
            while True :
                try :
                    roll_no = int(input("Enter the roll no :"))
                    break
                except ValueError:
                    print("Enter a valid integer.")
            while roll_no <= 0 :
                roll_no = int(input("Enter the valid roll no :"))
            found = False
            for student in Students :
                if roll_no == student["roll_no"] :
                    print("Roll no exists")
                    found = True
                    break 
            if not found :
                return roll_no

def get_valid_marks():
    while True :
        try :
            marks = float(input("Enter marks: "))
            break
        except ValueError:
            print("Enter valid marks.")
    while marks < 0 or marks > 100:
        marks = float(input("Enter valid marks: "))
    return marks
def calculate_result(marks):
    if marks >= 90:
        return "Excellent"
    elif marks >= 80:
        return "Good"
    elif marks >= 50:
        return "Only Pass"
    else:
        return "Fail"
def load_students() :
    try :
        with open("students.json","r") as file :
            Students = json.load(file)
    except json.JSONDecodeError:
        Students = []
        print("No Students Available.")
    except FileNotFoundError :
        Students =[]
    return Students
def save_students(Students):
    with open ("students.json","w") as file :
        json.dump(Students,file,indent = 4)
def search_student() :
    Students = load_students()
    print("1. Search by name.")
    print("2. Search by roll no.")
    while True :
        try :
            choose = int(input("Enter the choice :"))
            break
        except ValueError :
            print("Valid Choice")
    if choose == 1 :
        search = input("Enter the name of student : ")
        search = search.lower()
        i = 0
        for student in Students :
            if student["name"] == search:
                formated_print(student)
                i+=1
        if i==0 :
            print("Nothing matches your search.")
    elif choose == 2 : 
        while True :
            try :
                search = int(input("Enter the roll no : "))
                break
            except ValueError :
                print("Enter the valid Roll number.")
        j=0
        for student in Students :
            if search == student["roll_no"] :
                formated_print(student)
                j+=1
        if j == 0 :
            print("Nothing matches your search.")
def delete_student():
    Students = load_students()
    if len(Students) == 0:
        print("No student Added.")
    else :
        found=False
        print("1.Delete by name.")
        print("2.Delete by roll no")
        while True :
            try :
                choice = int(input("Enter your choice :"))
                break
            except ValueError:
                print("Enter a valid Choice.")
        if choice == 1 :
            delete = input("Enter the name of student : ")
            delete = delete.lower()
            for student in Students :
                if delete == student["name"] :
                    Students.remove(student)
                    found = True
                    break            
            if found :
                save_students(Students)
                print("Student deleted successfully.")
            else :
                print("Nothing matches the student you want to delete.")
        elif choice == 2 :
            while True :
                try :
                    delete = int(input("Enter the roll no of student : "))
                    break
                except ValueError :
                    print("Enter a valid roll number.")
            for student in Students :
                if delete == student["roll_no"] :
                    Students.remove(student)
                    found = True
                    break          
            if found :
                save_students(Students)
                print("Student deleted successfully.")
            else :
                print("Nothing matches the student you want to delete.")
        else :
            print("Invalid Input.")
           
def display_students():
    Students = load_students()
    if len(Students) == 0:
        print("No student Added.")
    else:
        for student in Students :
            formated_print(student)
def update_student():
    Students = load_students()
    while True :
        try :
            roll_no = int(input("Enter roll no to update: "))
            break
        except ValueError :
            print("You entered an invalid roll number.")
    for student in Students:
        if student["roll_no"] == roll_no:
            student["name"] = input("Enter new name: ").lower()
            student["age"] = get_valid_age()
            student["marks"] = get_valid_marks()
            student["result"] = calculate_result(student["marks"])
            save_students(Students)
            print("Student updated successfully.")
            return
    print("Student not found.")
def formated_print(student) :
    print("==========================================")
    print("      Name       :",student["name"])
    print("      Roll No    :",student["roll_no"])
    print("      Age        :",student["age"])
    print("      Marks      :",student["marks"])
    print("      Result     :",student["result"])