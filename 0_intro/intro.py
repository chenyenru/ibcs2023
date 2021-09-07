print("hello world")
x = 8
if x > 10:
    print("hi")


def greetings(name):
    print(f"Hello, I am {name}")


greetings("Rebecca")

school = input("Type your school name")

if (school == "mdid"):
    print("Hello")
elif(school == "mdhs"):
    print("Hello you suck")
else:
    print("Welcome")


if __name__ == "__main__":
    print("This only executes when we execute this file")
    print("This will also not run if it's run from other files")
