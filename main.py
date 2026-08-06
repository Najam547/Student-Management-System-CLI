import student
import project
import os 
def clear_scr() :
    os.system("cls" if os.name == "nt" else "clear")
def pause () :
    input("\nPress enter to continue...")
while True :
    clear_scr()
    print("=======================================")
    print("       Student Management System       ")
    print("=======================================")
    print("1.Add Student")
    print("2.View Students")
    print("3.Search Student")
    print("4.Delete Student")
    print("5.Update Student")
    print("6.View project details")
    print("7.Exit")
    while True :
        try :
            choice = int(input("Choose an option :"))
            break
        except ValueError:
            print("please enter a valid integer.")
    if choice == 1 :
        clear_scr()
        student.add_student()
        pause()
    elif choice == 2 :
        clear_scr()
        student.display_students()
        pause()
    elif choice == 3 :
        clear_scr()
        student.search_student()
        pause()
    elif choice == 4 :
        clear_scr()
        student.delete_student()
        pause()
    elif choice == 6 :
        clear_scr()
        project.project_details()
        pause()
    elif choice == 5 :
        clear_scr()
        student.update_student()
        pause()
    elif choice == 7 :
        break
    else :
        print("Invlid Input")
        print("Please re-enter a valid choice")