class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

class Teacher(SchoolMember):
    def __init__(self, name, age, salary, subject):
        super().__init__(name, age)
        self.salary = salary
        self.subject = subject

    def getSalary(self):
        return self.salary

    def getSubject(self):
        return self.subject

class Student(SchoolMember):
    def __init__(self,name, age, courses, year, grades):
        super().__init__(name, age)
        self.courses = courses
        self.year = year
        self.grades = grades

    def getCourses(self):
        return f"Courses: {self.courses}"

    def getGrades(self):
        return f"Grades: {self.grades}"

    def getYear(self):
        return self.year

t = Teacher("Mima", 20, 1000, "Math")

print(t.getAge())
print(t.getSalary())

s = Student("Nasko", 30, ["Math","English"], 2025, [6,3,2,5])

print(s.getCourses())