import random


class Student:
    def __init__(self, ide, name, course):
        self.id = ide
        self.name = name
        self.course = course
        self.mark = 0

    def __str__(self):
        return f"Student ID: {self.id}, Name: {self.name}, Course: {self.course}, Mark: {self.mark}"

    def setmark(self, newmark):
        if newmark < 0 or newmark > 100:
            return False
        else:
            self.mark = newmark
            return True

    def getgrade(self):
        if self.mark >= 70:
            return "Grade is First"
        elif self.mark >= 60:
            return "Grade is 2/1"
        elif self.mark >= 50:
            return"Grade is 2/2"
        elif self.mark >= 40:
            return "Grade is Third"
        else:
            return "Grade is Fail"

    def didpass(self):
        if self.mark >= 40:
            return True
        else:
            return False


students = []
for count in range(5):
    newStudent = Student(101 + count, input("What is the next name? "), "se")
    students.append(newStudent)
    students[count].setmark(random.randint(1, 100))
    print(students[count].didpass())
    print(students[count].getgrade())
    print(students[count])

'''
print(students[1].getgrade())
students[1].setmark(5)
print(students[1].getgrade())
students[3].mark = random.randint(1,100)
if students[3].didpass():
    print("Student 103 did pass")
else:
    print("Student 103 did not pass")
'''