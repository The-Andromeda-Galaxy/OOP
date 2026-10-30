class School:
    def __init__(self,name):
        self.name = name

    def display(self):
        print("\nThe details of the student are:")
        print(f"Name:{self.name}")

class Student(School):
    def __init__(self, name,grade,roll,section):
        super().__init__(name)
        self.grade = grade
        self.roll = roll
        self.section = section

    def show_details(self):
        print(f"Class:{self.grade}")
        print(f"Section:{self.section}")
        print(f"Roll:{self.roll}")

#creating the objects
student1= Student("Anvi","8","12","T")
student1.display()
student1.show_details()

student2 = Student("Abc","8","15","T")
student2.display()
student2.show_details()
