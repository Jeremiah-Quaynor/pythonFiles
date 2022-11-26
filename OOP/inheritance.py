class UserData():
    age = 0
    name = None
    def __init__(self,name,age):
        self.name = name
        self.age = age


class PhoneNum(UserData):
    def __init__(self,name, age, num):
        super().__init__(name,age)
        self.num = num



user_1 = PhoneNum("Jeremiah",22, 551794490)
print(user_1.num)