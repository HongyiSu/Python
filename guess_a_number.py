import math
import random
fname=input("give me your first name: ")
lname=input("give me your last name: ")
age=input("give me your age: ")
print("Hello! "+ fname.upper() +" " + lname.upper()+ " you are " + age +"!")

print(fname.upper() + " is cool!")


print("your initial is " +fname[0].upper()+ "" +lname[0].upper()+"." + " let's go! ")

def main():
    guesses = 3
    num = random.randint(1,10)
    answer=0

    while num != answer and guesses > 0:
        answer = int(input("guess a number between 1-100 (integers only) ? :"))
        guesses -= 1
        if answer < num:
            print("it is too low, number of guess left: " + str(guesses))
        elif answer > num:
            print("it is too high, number of guess left: " + str(guesses))
        else:
            print("you got it! " + fname[0].upper()+ "" +lname[0].upper()+"'s score is " + str(10*guesses+10) +"%")
    if answer != num:
        print("sorry, that is your last chance, the answer was " + str(num) +" "+ fname[0].upper()+ "" +lname[0].upper()+"'s score is zero!")

main()
replay = "yes"
replay = input("another game? yes?").lower()
if replay == "yes":
      main()
      replay = input("another game? yes?").lower()
      if replay == "yes":
          main()

      else:
          print("Thank you for playing!")
else:
    print("Thank you for playing!")

