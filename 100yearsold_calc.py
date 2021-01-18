from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

#  CODE 1
#print("Enter your name")
#name=str(input())
#print("Enter your age")
#age=int(input())
#yearage=100-age
#year100=2020+int(yearage)
#print("You will turn 100 years old on", year100)

#CODE 2

repeat = "Y"
while repeat == "Y":
    name=str(input("Enter your name:  "))
    print("Your name is", name)
    age=int(input("Enter your age: " ))
    print("Your age is", age)
    print("You will turn 100 years old on", int(2020+(100-age)))
    repeat=str(input("Do you want to enter another name?[Y/N]:  "))
print("Ok, Good Bye!")


