import time
import sys
import random
import os

def main():
  os.system("cls")
  prints = input("  How fast would you like to print the characters?\n(Note: Default is 5): ")
  times = float(prints)/100
  operations = ["+","-","*","/"]
  def delay_print(s):
      for c in s:
          sys.stdout.write(c)
          sys.stdout.flush()
          time.sleep(times)
  def is_number(s):
      try:
          float(s)
          return True
      except ValueError:
          return False
 
  delay_print("  Hello, I am TAI, your new AI companion, I can read, do math, and generate passwords.  Try it!!!(keywords: passwd, an integer, and a string)\n")
 
  beginq = input("")
  if (is_number(beginq) == True):
    os.system("cls")
    delay_print("  This an integer, what operation would you like me to execute?\nMultiply(*)\nSubtract(-)\nDivide(/)\nAdd(+)\n")
    m = input("Operation: ")
    if m == "+":
      a = input("Number to add: ")
      ans = float(beginq) + float(a)
      print"  The answer is: ",ans
     
    if m == "*":
      a = input("Number to multiply by: ")
      ans = float(beginq) * float(a)
      print"  The answer is: ",ans
     
    if m == "/":
      a = input("Number to divide by: ")
      ans = float(beginq) / float(a)
      print"  The answer is: ",ans
     
    if m == "-":
      a = input("Number to subtract by: ")
      ans = float(beginq) - float(a)
      print"  The answer is: ",ans
     
    if m != operations:
      print("Syntax error!")
      dec = input("  Restart program?[y/n]")
      if dec == "y":
        main()
      else:
        for i in range(5):
          os.system("cls")
          print("Closing system")
          time.sleep(0.25)
          os.system("cls")
          print("Closing system.")
          time.sleep(0.25)
          os.system("cls")
          print("Closing system..")
          time.sleep(0.25)
          os.system("cls")
          print("Closing system...")
          time.sleep(0.25)
        times = 0.035
        delay_print("#####################################################################################")
        time.sleep(0.2)
        print("Login Auth completed")
        time.sleep(0.5)
        print("Exiting program now")
        time.sleep(1)
        os.system("cls")
     
  if (is_number(beginq) == False) and (beginq != "passwd"):
    delay_print("  This is a string.")
   
   
  if beginq == "passwd":
    # Clearing the Screen
    os.system('cls')
    times = 0.075
    delay_print("Password generator\n")
    passwdopt = input("secure, memorable, and short:\n")
    if passwdopt == "secure":
      for i in range(20):
        passwd = random.choice("`~1234567890!@#$%^&*()_-+=qwertyuiop[]\{}|asdfghjkl;:'zxcvbnm,./<>?")
        sys.stdout.write(passwd)
    times = prints
   
    if passwdopt == "short":
      for i in range(5):
        passwd = random.choice("`~1234567890!@qwertyuiopasdfghjklpa,./<>?")
        sys.stdout.write(passwd)
    times = prints
   
    if passwdopt == "memorable":
      loc = input("Your favorite location on earth: ")
      num = input("Favorite number: ")
      loc = loc.replace("i","1")
      loc = loc.replace("e","3")
      loc = loc.replace("I","1")
      loc = loc.replace("E","3")
      loc = loc.replace("b","8")
      loc = loc.replace("e","3")
      loc = loc.replace("B","8")
      loc = loc.replace(" ", "_")
      loc = loc.replace(",", "")
      print ("Password: " + str(loc)+str(num))
    times = prints
   
main()
