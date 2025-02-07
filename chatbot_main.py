import time
import sys
import random
import os
def type_pr(str):
    for letter in str:
        sys.stdout.write(letter)
        time.sleep(0.005)
def passwd_en():
  def logo_lat():
    os.system("cls")
    type_pr("###################################     \n")
    type_pr("\           ____             __    \   \n")
    type_pr(" \         /    \           _| |    \  \n")
    type_pr("  \       /  0   \          -| \     \ \n")
    type_pr("   \     |___|____|          | |      \ \n")
    type_pr("    \    |________|         [_!_]      \ \n")
    type_pr("     \#################################/\n")
    type_pr("     /####1##2##3##4##5##6##7##8##9##0/\n")
    type_pr("    /################################/\n")
    type_pr("   /################################/\n")
  def logo_one():
    type_pr("###################################     \n")
    type_pr("\           ____             __    \   \n")
    type_pr(" \         /    \           _| |    \  \n")
    type_pr("  \       /  0   \          -| \     \ \n")
    type_pr("   \     |___|____|          | |      \ \n")
    type_pr("    \    |________|         [_!_]      \ \n")
    type_pr("     \#################################/\n")
    type_pr("     /####1##2##3##4##5##6##7##8##9##0/\n")
    type_pr("    /################################/\n")
    type_pr("   /################################/\n")
  logo_lat()
  pass_en = input("Encypte a password: \n")
  
  pass_or = pass_en
  pass_en = pass_en.replace("e", "3")
  pass_en = pass_en.replace("E", "3")
  print(pass_en)
  time.sleep(0.3)
  os.system("cls")
  pass_en = pass_en.replace("i", "1")
  pass_en = pass_en.replace("I", "1")
  print(pass_en)
  time.sleep(0.3)
  os.system("cls")
  pass_en = pass_en.replace(" ", "_")
  pass_en = pass_en.replace(",", "'")
  print(pass_en)
  time.sleep(0.3)
  os.system("cls")
  pass_en = pass_en.replace("s", "5")
  pass_en = pass_en.replace("S", "5")
  print(pass_en)
  time.sleep(0.3)
  os.system("cls")
  pass_en = pass_en.replace("a", "4")
  pass_en = pass_en.replace("A", "4")
  print(pass_en)
  time.sleep(0.3)
  os.system("cls")
  pass_en = pass_en.replace("b", "8")
  pass_en = pass_en.replace("B", "8")
  print(pass_en)
  time.sleep(0.3)
  os.system("cls")
  pass_en = pass_en.replace("o", "0")
  pass_en = pass_en.replace("O", "0")
  print(pass_en)
  time.sleep(0.3)
  os.system("cls")
  pass_en = pass_en.replace("s", "$")
  pass_en = pass_en.replace("S", "$")
  print(pass_en)
  time.sleep(0.3)
  os.system("cls")
  pass_en = pass_en.replace("k", "|-\n|-\n|-")
  pass_en = pass_en.replace("K", "|-\n|-\n|-")
  print(pass_en)
  time.sleep(0.3)
  os.system("cls")
  pass_en = pass_en.replace("d", "|)")
  pass_en = pass_en.replace("D", "|)")
  print(pass_en)
  time.sleep(0.3)
  os.system("cls")
  pass_en = pass_en.replace("l", "|_")
  pass_en = pass_en.replace("L", "|_")
  print(pass_en)
  time.sleep(0.3)
  os.system("cls")
  print(pass_en)
  dec = input("Decode: [y/n]")
  if dec == "y":
    pass_en = pass_en.replace("3", "e")
    print(pass_en)
    time.sleep(0.3)
    os.system("cls")
    pass_en = pass_en.replace("1", "I")
    print(pass_en)
    time.sleep(0.3)
    os.system("cls")
    pass_en = pass_en.replace("_", " ")
    pass_en = pass_en.replace("'", ",")
    print(pass_en)
    time.sleep(0.3)
    os.system("cls")
    pass_en = pass_en.replace("5", "s")
    print(pass_en)
    time.sleep(0.3)
    os.system("cls")
    pass_en = pass_en.replace("4", "a")
    print(pass_en)
    time.sleep(0.3)
    os.system("cls")
    pass_en = pass_en.replace("8", "B")
    print(pass_en)
    time.sleep(0.3)
    os.system("cls")
    pass_en = pass_en.replace("0", "o")
    print(pass_en)
    time.sleep(0.3)
    os.system("cls")
    pass_en = pass_en.replace("$", "s")
    print(pass_en)
    time.sleep(0.3)
    os.system("cls")
    pass_en = pass_en.replace("|-\n|-\n|-", "k")
    print(pass_en)
    time.sleep(0.3)
    os.system("cls")
    pass_en = pass_en.replace("|)", "D")
    print(pass_en)
    time.sleep(0.3)
    os.system("cls")
    pass_en = pass_en.replace("|_", "ghj")
    print(pass_en)
    time.sleep(0.3)
    rst = input("Restart?[y/n]")
    if rst == "y":
      main()
    else:
      print("Finished")
  else:
    print("done")
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
  def printLogo():
    delay_print("   |--------|               \n")
    delay_print("   |--------|           (!)\n")
    delay_print("       ||       /\      |-| \n")
    delay_print("       ||      /__\     | | \n")
    delay_print("       ||     /    \    | | \n")
    delay_print("       ||    /      \   |_|     ")
  printLogo()
  delay_print("  Hello, I am TAI, your new AI companion, I can read, do math, and generate passwords.  Try it!!!(keywords: passwd, an integer, encrypt, and a string)\n")
 
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
     
  if (is_number(beginq) == False) and (beginq != "passwd") and (beginq != "encrypt"):
    delay_print("  This is a string.")
   
  if beginq == "encrypt":
    passwd_en()
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
