
class students_management(object): #At first we start with the class students management

    def __init__(self, name, id, major, courses_and_grades): # this is the def to make class and put name , id , major and courses&grades
        self.id = id
        self.name = name
        self.major = major
        self.courses_and_grades = courses_and_grades

    def display_info(self): # so we create def to display info which is display the name , major ,id and the courses&grades
        print("--------------------------------------------------------------------")

        print("student name: ", self.name, " , student id: ", self.id, " , student major: ",
              self.major)
        for course in self.courses_and_grades:
            print("student course: ", course, " , student grade: ", self.courses_and_grades[course])

        print("--------------------------------------------------------------------")





def add_student (): #def add_student is to add a new student it will ask for student id , name , major , courses and grades
    while True:
        id = input("Please Enter Id: ") # the new ID
        name = input("Please Enter name: ") # the new name
        major = input("Please Enter major: ") # the new major
        courses_and_grades = {} #we put course and grade in dictionary  because more than courses_and_grades per student and courses_and_grades are linked

        question = input("Do you want to add course for this student? ") #here we add question if he want to to add course
        if question.lower() == "yes": #if the user wrote yes will ask him for the course and grade
            while True:
                course = input("Please Enter course: ") #then it will ask for the course
                grade = input("Please Enter grade: ") #then it will ask for the grade

                courses_and_grades[course] = grade # here we link the course and the grade
                question = input("Do you want to add new course and grade? ")
                if question.lower() == "no": #if the user said yes it is will loop him to the grade and course , if no it will break
                    break

        student_info = students_management(name, id, major, courses_and_grades) #student_info will contains the student_info in the class
        Student_list.append(student_info) #student_info saved in the student list
        question = input("Do you want to add a new students? ") #here ask the user if he want to add student or no
        if question.lower() == "no": #if the user said no it will break
            break





def search(): # this is for the search
    if len(Student_list) == 0: #here it will pick up if there is student or not
        print("Empty list, Please add student..") #if we have 0 students it will print this
    else:
        id = input("Enter the id for the student that you are looking for:") #the search will be on the id because name might be similar
        for x in Student_list: #here it will loop and search for id
             if x.id == id:
                 return x #here it will return student info





def delete_student(): #this for delete student
    if len(Student_list) == 0: #here it will pick up if there is student or not
        print("Empty list, Please add student..") #if the list has 0 students it will print Empty list, Please add student..
    else:
        delete = search() #it will send the user to the search function and returned it to delete
        if delete is None: print("this student does not exist")
        else: delete.display_info()

        question = input("Do you want to delete it? ") #it will ask you before you delete it to make sure if you want to delete it or not
        if question.lower() == "yes":
            Student_list.remove(delete)
            print("Student deleted successfully ..") #if you type yes it will get delete and this will be printed




def update_student():
    if len(Student_list) == 0: #here it will pick up if there is student or not
        print("Empty list, Please add student..") #if the list has 0 students it will print Empty list, Please add student..

    else:
        student = search() # it will send the user to the search function and returned it to update_student
        if student is None:
            print("this student does not exist")
            update_student()
        else:
            student.display_info()  # here it will display "s" info
        while True:
            print("--------------------------------------------------------------------")
            print('''what are you looking to update
            For updating the general info such as name, id and major enter 1
            For add a new course and grade enter  2
            For deleting a course and grade enter 3
            For updating a courses and its' grades enter 4
            Or to exit the update menu enter 5''')
            Required_update = input("Enter number from 1 to 5 ")

            if Required_update == "1": # updating the general info such as name, id and major
                while True:
                    print("What do you want to update:\n For the Id entrt 1 \n For the Name entrt 2\n For the Major enter 3\n if you want to exit enter 4")  # here asking the ueser what they want to update
                    Required_update = input("Enter the number from 1 to 4")
                    if Required_update == "1":
                        id = input("Please Enter updated Id: ")  # here the input for the updated Id
                        student.id = id  # here return the updated Id to the list
                    elif Required_update == "2":
                        name = input("Please Enter updated name: ")  # here the input for the updated Name
                        student.name = name  # here return the updated name to the list
                    elif Required_update == "3":
                        major = input("Please Enter updated major: ")  # here the input for the updated Major
                        student.major = major  # here return the updated major to the list
                    elif Required_update == "4":  # here if the ueser don't want to update
                        break
                    else: print("Please enter number from 1 to 4 ")  # here we Catch the user if they didn't enter correct value


            elif Required_update == "2": #For add a new course and grade
                while True:
                    course = input("Please Enter course: ") # the input for the new course
                    grade = input("Please Enter grade: ") # the input for the new grade
                    student.courses_and_grades[course] = grade #for saveing for the new course and grade
                    for course in student.courses_and_grades: #display grades info
                        print("student course: ", course, " , student grade: ", student.courses_and_grades[course])
                    question = input("Do you want to add new course and grade? ") # the question for add new course if the user type yes he will loop again
                    if question.lower() == "no": # if the user type yes they will break
                        break

            elif Required_update == "3": #deleting a course and grade enter
                while True:
                    for course in student.courses_and_grades: #display grades info
                        print("student course: ", course, " , student grade: ", student.courses_and_grades[course])
                    course_name = input("Enter the course you are looking to delete: ") #the input for the search for the course
                    for course in student.courses_and_grades:  #the search for the course
                        if course == course_name:
                            question = input("Do you want to delete it?")  # it will ask you before you delete it to make sure if you want to delete it or not
                            if question.lower() == "yes":
                                student.courses_and_grades.pop(course_name)  #here return the updated courses_and_grades to the dictionary
                                print("Course deleted successfully ..")
                            break
                    question = input("Do you want to delete another course and grade? ") # the question forupdate course if the user type yes he will loop again
                    if question.lower() == "no": #if the user type yes they will break
                        break


            elif Required_update == "4": #updating a courses and its' grades enter
                while True:
                    for course in student.courses_and_grades: #display grades info
                        print("student course: ", course, " , student grade: ", student.courses_and_grades[course])

                    course_name = input("Enter the course you are looking to update: ") #the input for the search for the course
                    for course in student.courses_and_grades:  #the search for the course
                        if course == course_name:
                            course = input("Please Enter updated course: ") # the input for the updated course
                            grade = input("Please Enter updated grade: ") # the input for the updated grade
                            student.courses_and_grades.pop(course_name)  #here return the updated courses_and_grades to the dictionary
                            student.courses_and_grades[course] = grade  # here we link the course and the grade
                            break
                    question = input("Do you want to update another course and grade? ") # the question forupdate course if the user type yes he will loop again
                    if question.lower() == "no": #if the user type yes they will break
                        break

            elif Required_update == "5": #Or to exit the update menu enter
                student.display_info()
                break

            else: print("Please enter number from 1 to 5 ")  # here we Catch the user if they didn't enter correct value



if __name__ == '__main__': #here the program starts

    print('''Welcome to students management
    If you want to Add Student enter     1
    If you want to Delete Student enter  2
    If you want to Search Student enter  3
    If you want to Display Student enter 4 
    If you want to Update Student enter  5 ''') #this will appear (output)
    Student_list = [] #here is the list for all the student

    while True:
        Required_Request = input("Enter the number from 1 to 5 :")
        if Required_Request == "1":
            add_student() #here it will send you add student function

        elif Required_Request == "2":
            delete_student() #here it will send you delete student function

        elif Required_Request == "3":
            s= search() #here it will send you search student function. and will save it "s" . s: is the result of the
            if s is None: print("this student does not exist")
            else: s.display_info() #here it will display "s" info



        elif Required_Request == "4":
            for student in Student_list:
                student.display_info() #here it will send you display info function

        elif Required_Request == "5":
            update_student() #here it will send you update student function
