from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

question = "Y"
i = 0
j = 0
names = []
ages = []
while question == "Y":
    name=str(input("Enter your name:  "))
    names.insert(i,name)
    age=int(input("Enter your age: " ))
    ages.insert(i,age)
    question=str(input("Do you want to enter another name?[Y/N]:  "))
    i = i + 1
for j in range(len(names)):
    print("Your name is", names[j], ", age", ages[j])
    print("You will turn 100 years old on", int(2020+(100-ages[j])))
    j=j+1
