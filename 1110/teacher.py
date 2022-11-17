class Person:
    def init__(self, name, number):
        self.name = name
        self.number = number

class Student(Person):
    UNDERGRADUATE = 0 # 상 수 클래스 변수
    POSTGRADUATE = 1 # 학 부 생 (대학생), 대학원생

    def __init__(self,name,number,studentType):
        super().__init__(name, number)
        self.studentType = studentType
        self.gpa=0
        self.classes = []

    def enrollCourse(self, course):
        self.classes.append(course)

    def __str__(self):
        return "\n 이름 =" + self.name + "\n주민번호="+self.number + "수강과목 ="+ str(self.classes) + "\n평점=" + str(self.gpa)

class Teacher(Person):
    def __init__(self,name,number):
        super().__init__(name,number)
        self.courses =[]
        self.salary=3000000

    def assignTeaching(self,course):
        self.courses.append(course)

    def __str__(self):
        return "\n 이름 =" + self.name + "\n주민번호="+self.number + "강과목 ="+ str(self.courses) + "\n월급=" + str(self.salary)

hong = Student("홍길동","12345678",Student.UNDERGRADUATE)
hong.enrollCourse("자료구조")
print(hong)

kim = Teacher("김철수","123456790")
kim.assignTeaching("Python")
print(kim)