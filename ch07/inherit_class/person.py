# Person 클래스 - 멤버 변수(name, age)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showinfo(self):
        print(self.name, self.age)

class Employee(Person):
    pass

if __name__ == "__main__":
    p1 = Person("강진", 24)
    p1.showinfo()

    e1 = Employee("남한강",30)
    e1.showinfo()

    e2 = Employee("북한강", 35)
    print(e2.name, e2.age)