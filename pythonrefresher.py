age = 23 
name = "Fatinah"

def hello(name='Fatinah', age='23'):
    return f"Hello {name} you are {age} years old".format(name,age)

def hi(name, age):
    print('Hello ' + name + ' you are ' + age + 'years old')

# print(age)
# print(name)

# print(hello())

#list
dognames = ["eric", 'collins', 'tensley']

dognames.insert(0, "terry")
dognames[3]
# print(dognames)

# for loops 
# for dog in dognames:
#     print(dog)

# for dog in range(1,4):
#     print(dog)

# while loop 
# age = 15
# while age <= 18: 
#     print(age)
#     age += 1

#dictionary
cats = {"Larry": 7, "Sally": 9, "Carrie": 8}


class Dogs:

    def bark():
        print("BARK!")

myDog = Dogs()