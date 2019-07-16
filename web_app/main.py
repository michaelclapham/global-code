from functools import reduce

def is_too_old(age): return age > 50
person = {
    "age": 25,
    "name": "Michael",
    "is_too_old": is_too_old
}

print("result is ", person["is_too_old"](person["age"]))

class Person:

    def __init__(self, name = "", age = 0):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        if age < 0:
            print("People can't be less than zero!")
        else:
            self.age = age

    def is_too_old(self):
        return self.age > 50

providence = Person()
# providence.set_name("Providence")
providence.set_name(input("what is your name"))
print(providence.get_name(), " is " ,providence.get_age(), "years old :)")
print("Is providence too old?", providence.is_too_old())

numbers = [12, 54, 33, 67, 24, 89, 11, 24, 47]

words = ["hello", "my", "name", "is", "Michael"]
print([(word, len(word)) for word in words if len(word) > 2])

def is_longer(word):
    return len(word) > 2

def to_tuple(word):
    return (word, len(word))

print(list(map(to_tuple, filter(is_longer, words))))

#print([n for n in numbers if n % 2 == 0])

total = 0
numbers = [1, 2, 3]
for num in numbers:
    total = total + num