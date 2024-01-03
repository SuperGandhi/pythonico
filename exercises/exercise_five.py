def age_high(user):
    return user.age < 17

class User:
    def __init__(self,age):
        self.age = age

user = User(15)
user2 = User(20)

result1 = age_high(user)
result2 = age_high(user2)

print(result1, result2)


