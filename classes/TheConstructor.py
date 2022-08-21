class UserData():
    age = 0
    name = None 
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def user(self):
        print("User name is :{} and is {} years old.".format(self.name, self.age))


user_1 = UserData("Jerry",40)
user_2 = UserData("Jeremiah",50)
user_3 = UserData("Bored",60)
user_4 = UserData("Bismark",40)
user_5 = UserData("Mag",40)


def avg_age():
    return(user_1.age+user_2.age+user_3.age+user_4.age+user_5.age)/5

print(type(user_1))
print(user_2.name)
print(avg_age())


class Rectangle():
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def calculatArea(self):
        return (self.length * self.width)



rect_1 = Rectangle(59,49)
print(rect_1.calculatArea())