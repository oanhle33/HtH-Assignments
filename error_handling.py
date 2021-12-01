"""
We're writing a program that adds two numbers together. 
Test this and solve any errors you find if you can. 
Solving one problem might turn up a new error...
Be sure to keep a note of whatever errors you find!
"""


print("Welcome to the addition helper")
number1 = input("Please enter the first number: " )
number2 = input("Please enter the second number: ")

print("The result is: ", int(number1) + int(number2))

"""
Below you will find broken pieces of code, do you think you can spot all the errors and fix them? Don't forget to use the debugging skills that you have learned so far!

If you think this stuff is too easy for you, you can try to see if you can master the VS Code debugger! Just click the link above and get started.
"""

# 1
greeting = "Hello World"

if greeting in ("Arrr!"):
    print("Go away, pirate.")
else:
    print("Greetings, hater of pirates!")
                
# 2
authors = {
    "Charles Dickens": 1870,
    "William Thackeray": 1863,
    "Anthony Trollope": 1882,
    "Gerard Manley Hopkins": 1889}

for author, date in authors.items():
    print("%s" % (authors) + " died in " + "%d" % (date))

                
# 3

year = int(input("Greetings! What is your year of origin? "))

if year <= 1900:
    print ("Woah, that's the past!")
elif year > 1900 and year < 2020:
    print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")
           
# 4
class Person:
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name
    def speak(self):
        print("My name is" + " " + self.first + " " + self.last)

me = Person("Brandon", "Walsh")
you = Person("Ethan", "Reed")

me.speak()
you.speak()
           
# 5
exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

exam_three = int(input("Input exam grade three: "))

grades = [exam_one, exam_two, exam_three]
sum = 0
for grade in grades:
  sum = sum + grade

avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade == "F":
    print ("Student is failing.")
else:
    print ("Student is passing.")
