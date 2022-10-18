import pandas as pd
# from numpy.random._examples.cffi.extending import state

print("WELCOME TO TOPHER ACADEMY")


class Topher_academy:
    # def __init__(self):
    #     # self.teachers = teachers
    #     # self.students = students
    #     # self.workers = workers

    def t_eachers(self):
        data = {
            "NAME": [],
            "ID_NUMBER": [],
            "DEPT": []
        }
        teacher_data = pd.DataFrame(data)
        state_teacher = input("Are you registered in Teacher portal? YES/NO ")
        if state_teacher == 'YES':
            pass  # should be asked what they want to do
        else:
            print('Enter your details below: ')
            teacher_details = []
            teacher_name = input("Enter your name: ")
            teacher_id_number = int(input("Enter your ID number: "))
            teacher_department = input("Enter your department: ")
            teacher_details.append(teacher_name)
            teacher_details.append(teacher_id_number)
            teacher_details.append(teacher_department)
            teacher_data.loc['1'] = [teacher_details[0], teacher_details[1], teacher_details[2]]
        print(teacher_data)

    def s_students(self):
        data2 = {
            "NAME": [],
            "ADM_NUMBER": [],
            "COURSE": []
        }
        student_data = pd.DataFrame(data2)
        state_student = input("Are a new student? YES/NO ")
        if state_student == 'YES':
            pass  # should be asked what they want to do
        else:
            print('Enter your details below: ')
            student_details = []
            student_name = input("Enter your name: ")
            student_admn_number = int(input("Enter your Admission number: "))
            student_course = input("Enter your Course: ")
            student_details.append(student_name)
            student_details.append(student_admn_number)
            student_details.append(student_course)
            student_data.loc['1'] = [student_details[0], student_details[1], student_details[2]]
        print(student_data)

    def w_orker(self):
        data3 = {
            "NAME": [],
            "id_NUMBER": [],
            "DESIGNATION": []
        }
        worker_data = pd.DataFrame(data3)
        state_worker = input("Are a new worker? YES/NO ")
        if state_worker == 'YES':
            pass  # should be asked what they want to do
        else:
            print('Enter your details below: ')
            worker_details = []
            worker_name = input("Enter your name: ")
            worker_id_number = int(input("Enter your ID number: "))
            worker_designation = input("Enter your Designation: ")
            worker_details.append(worker_name)
            worker_details.append(worker_id_number)
            worker_details.append(worker_designation)
            worker_data.loc['1'] = [worker_details[0], worker_details[1], worker_details[2]]
        print(worker_data)


Teacher1 = Topher_academy()
Teacher1.t_eachers()
Student1 = Topher_academy()
Student1.s_students()

