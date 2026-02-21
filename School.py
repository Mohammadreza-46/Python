class Student:
    def __init__(self, Name, Student_ID, grade):
        self.name = Name
        self.Student_ID = Student_ID
        self.grade = grade
        self.score = {}
        self.present_days = 0
        self.absent_days = 0
    def add_score(self, subject,score):
        self.score.setdefault(subject, [])
        self.score[subject].append(score)
    def mark_attendance(self, status):
        if status == 'P':
            self.present_days += 1
        elif status == 'A':
            self.absent_days += 1
    def get_average(self):
        a = 0
        b = 0
        for score in self.score.values():
            for i in score:
                a += i
            b += 1
        return a/b
    def get_report(self):
        print(f'Name: {self.name}\n',
              f'Student ID: {self.Student_ID}\n',
              f'Student Grade: {self.grade}\n',
              f'Score: {self.score}\n',
              f'Present Days: {self.present_days}\n',
              f'Absent Days: {self.absent_days}',)
class Teacher:
    def __init__(self,Name, Teacher_ID, subject):
        self.Name = Name
        self.Teacher_ID = Teacher_ID
        self.subject = subject
    def give_score(self, score,student):
        student.add_score(self.subject,score)
    def get_info(self):
        print(f'Name: {self.Name}\n',
              f'Teacher ID: {self.Teacher_ID}\n',
              f'Subject: {self.subject}')
class Classroom:
    def __init__(self, Name, Teacher, subject):
        self.Name = Name
        self.Teacher = Teacher
        self.subject = subject
        self.students = []
    def __repr__(self):
        return self.Name
    def add_student(self, student):
        for i in self.students:
                if student.Student_ID == i.Student_ID:
                    return
        self.students.append(student)
    def remove_student(self, student_Id):
        for i in self.students:
            if i.Student_ID == student_Id:
                self.students.remove(i)
    def get_student(self, student_Id):
        for i in self.students:
            if i.Student_ID == student_Id:
                print(i.get_report())
    def show_all_students(self):
        for i in self.students:
            i.get_report()
            print('=================================')
    def get_class_average(self):
        List_average = []
        for i in self.students:
            List_average.append(i.get_average())
        list_average = sum(List_average) / len(List_average)
        print(list_average)
    def get_class_report(self):
        print(f'Name: {self.Name}\n',
              f'Teacher: {self.Teacher.Name}\n',
              f'Subject: {self.subject}',)
        print('Studens:')
        for i in self.students:
            print(i.name)
class School:
    def __init__(self,Name):
        self.Name = Name
        self.classrooms = []
    def add_classroom(self, classroom):
        self.classrooms.append(classroom)
    def show_all_classrooms(self):
        for i in self.classrooms:
            i.get_class_report()
            print('===============================')
    def generate_school_report(self):
        print(f'Name: {self.Name}\n',
              f'Classrooms: {self.classrooms}\n',)
    def find_students(self, ID):
        for i in self.classrooms:
            for j in i.students:
                if j.Student_ID == ID:
                    return j
def main():
    #Teacher
    global Student_
    ahmadi = Teacher('Ahmadi', 1, 'Math')
    tavoky = Teacher('Tavoky', 2, 'Ghor an')
    asghari = Teacher('Asghari', 3, 'Farsi')
    akbari = Teacher('Akbari', 4, 'Dini')
    rezayi = Teacher('Rezayi', 5, 'Motale at')
    askari = Teacher('Askari', 6, 'Varzesh')
    ali_zade = Teacher('Ali Zade', 7, 'Honar')
    #Class
    class_Math = Classroom('Math', ahmadi, 'Math')
    class_Ghor_an = Classroom('Ghor An', tavoky, 'Ghor an')
    class_Farsi = Classroom('Farsi', asghari, 'Farsi')
    class_Dini = Classroom('Dini', akbari, 'dini')
    class_Motal_at = Classroom('Motal at', rezayi, 'Motal at')
    class_Varzesh = Classroom('Varzesh', askari, 'Varzesh')
    class_Honar = Classroom('Honar', ali_zade, 'Honar')
    #School
    school = School('Alavi')
    school.add_classroom(class_Math)
    school.add_classroom(class_Ghor_an)
    school.add_classroom(class_Farsi)
    school.add_classroom(class_Dini)
    school.add_classroom(class_Motal_at)
    school.add_classroom(class_Varzesh)
    school.add_classroom(class_Honar)
    while True:
        print('='*30)
        print('1. Add student')
        print('2.Add score to student')
        print('3.Absent student or present student')
        print('4.Get_student')
        print('5.Get classroom student')
        print('6.Get Classroom average')
        print('7.Get classroom report')
        print('8.Get school report')
        print('9.Quit')
        answer = input('Enter your choice: ')
        if answer == '1':
            class_ = input('Enter Class Name: ').lower()
            Name = input('Enter Name of Student: ')
            ID = input('Enter ID of Student: ')
            Grade = input('Enter Grade of Student: ')
            student = Student(Name, ID, Grade)
            if class_ == 'math':
                class_Math.add_student(student)
            elif class_ == 'ghor an':
                class_Ghor_an.add_student(student)
            elif class_ == 'farsi':
                class_Farsi.add_student(student)
            elif class_ == 'dini':
                class_Dini.add_student(student)
            elif class_ == 'varzesh':
                class_Varzesh.add_student(student)
            elif class_ == 'honar':
                class_Honar.add_student(student)
            elif class_ == "motal at":
                class_Motal_at.add_student(student)
        elif answer == '2':
            name = input('Enter name of Student: ')
            Teacher_ = input('Enter Teacher Name: ').lower()
            score = int(input('Enter Score of Student: '))
            for i in school.classrooms:
                for j in i.students:
                    if j.name == name:
                        student = j
            if Teacher_ == 'tavoky':
                tavoky.give_score(score,student)
            elif Teacher_ == 'asghari':
                asghari.give_score(score,student)
            elif Teacher_ == 'akbari':
                akbari.give_score(score,student)
            elif Teacher_ == 'rezayi':
                rezayi.give_score(score,student)
            elif Teacher_ == 'askari':
                askari.give_score(score,student)
        elif answer == '3':
            A_P = input('Enter A or P: ')
            ID = input('Enter ID of Student: ')
            student = school.find_students(ID)
            student.mark_attendance(A_P)
        elif answer == '4':
            ID = input('Enter ID of Student: ')
            student =  school.find_students(ID)
            student.get_report()
        elif answer == '5':
            Classroom_ = input('Enter Classroom Name: ').lower()
            if Classroom_ == 'math':
                class_Math.show_all_students()
            elif Classroom_ == 'ghor an':
                class_Ghor_an.show_all_students()
            elif Classroom_ == 'farsi':
                class_Farsi.show_all_students()
            elif Classroom_ == 'dini':
                class_Dini.show_all_students()
            elif Classroom_ == 'varzesh':
                class_Varzesh.show_all_students()
            elif Classroom_ == 'honar':
                class_Honar.show_all_students()
            elif Classroom_ == 'motal at':
                class_Motal_at.show_all_students()
        elif answer == '6':
            Classroom_ = input('Enter Classroom Name: ').lower()
            if Classroom_ == 'math':
                class_Math.get_class_average()
            elif Classroom_ == 'ghor an':
                class_Ghor_an.get_class_average()
            elif Classroom_ == 'farsi':
                class_Farsi.get_class_average()
            elif Classroom_ == 'dini':
                class_Dini.get_class_average()
            elif Classroom_ == 'varzesh':
                class_Varzesh.get_class_average()
            elif Classroom_ == 'honar':
                class_Honar.get_class_average()
            elif Classroom_ == 'motal at':
                class_Motal_at.get_class_average()
        elif answer == '7':
            Classroom_ = input('Enter Classroom Name: ').lower()
            if Classroom_ == 'math':
                class_Math.get_class_report()
            elif Classroom_ == 'ghor an':
                class_Ghor_an.get_class_report()
            elif Classroom_ == 'farsi':
                class_Farsi.get_class_report()
            elif Classroom_ == 'dini':
                class_Dini.get_class_report()
            elif Classroom_ == 'varzesh':
                class_Varzesh.get_class_report()
            elif Classroom_ == 'honar':
                class_Honar.get_class_report()
            elif Classroom_ == 'motal at':
                class_Motal_at.get_class_report()
        elif answer == '8':
            school.generate_school_report()
        elif answer == '9':
            exit()
if __name__ == '__main__':
    main()