class Student:

    school = "Nagarjuna Vidyalayam"

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def show(self):
        print(self.name, self.age, self.marks)

    def displayschool(self):
        print(self.school)


s1 = Student("Madhava", 30, 100)

s1.show();
s1.displayschool()
