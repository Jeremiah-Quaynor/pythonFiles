class MyClass():
    def set_age(self,num):
        self.age = num
    def get_age(self):
        return self.age


jerry = MyClass()
jerry.set_age(49)

print(jerry.get_age())



class Person():
    def getGender(self):
        return "Unknown"

class Male(Person):
    def getGender(self):
        return "Male"


class Female(Person):
    def getGender(self):
        return "Female"

male = Male()
female = Female()

print(male.getGender())
print(female.getGender())

