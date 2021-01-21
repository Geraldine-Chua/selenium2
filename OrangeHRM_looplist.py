from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
print("start of program")


print("Enter User Name: ")
user_name = str(input())
print("Enter Password: ")
password = str(input())
repeat = "Y"
empnames=[]
usernames=[]
pswds=[]
a=0
b=0
while repeat == "Y":
         print("me Enter Employee Name")
         empname= str(input())
         empnames.insert(a,empname)
         print("Enter User Name")
         username = str(input())
         usernames.insert(a, username)
         print("Enter User Name Password")
         UserName_pswd = str(input())
         pswds.insert(a,UserName_pswd)
         repeat = str(input("Dou you want to enter another User Name?[Y/N]: "))
         a=a+1
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
element = driver.find_element_by_id("txtUsername")
element.send_keys(user_name)
element = driver.find_element_by_id("txtPassword")
element.send_keys(password)
element.send_keys(Keys.RETURN)
for b in range(len(empnames)):
    element = driver.find_element_by_id("menu_admin_viewAdminModule")
    element.click()
    element = driver.find_element_by_id("btnAdd")
    element.click()
    element = Select(driver.find_element_by_id("systemUser_userType"))
    element.select_by_visible_text("Admin")
    element = driver.find_element_by_id("systemUser_employeeName_empName")
    element.send_keys(empnames[b])
    element = driver.find_element_by_id("systemUser_userName")
    element.send_keys(usernames[b])
    element = Select(driver.find_element_by_id("systemUser_status"))
    element.select_by_visible_text("Enabled")
    element = driver.find_element_by_id("systemUser_password")
    element.send_keys(pswds[b])
    element = driver.find_element_by_id("systemUser_confirmPassword")
    element.send_keys(pswds[b])
    element = driver.find_element_by_id("btnSave")
    element.click()
    time.sleep(6)
    b = b + 1









