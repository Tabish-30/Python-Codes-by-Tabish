# EXERCISE 1 (Create a Calculator)

x = input("Enter First Number: ")
y = input("Enter Second Number: ")
O = input("Enter the Sign of Operator you want: ")

if(O == "+"):
    print(int(x)+int(y))
elif(O == "-"):
    print(int(x)-int(y))
elif(O == "*"):
    print(int(x)*int(y))
elif(O == "/"):
    print(int(x)/int(y))
else:
    print("Bas ye char me se hi ek daalna hai (+,-,*,/)")
    print('abhi itna hi aata hai hmko😅')




# print("The value of",x, "exponent" ,y, "is-", x**y)
# alt + shift + down arrow = replicate that line
# alt + left click to edit in multiple areas at the same time


# EXERCISE 2 (TIME MODULE)

import time
Time = time.strftime('%H:%M:%S')
T = int(time.strftime("%H"))
print(Time)

if(T < 12):
    if(T >= 4):
        print("Good Morning Sir")
    else:
        print("Good Night Sir")    
elif(T >= 12):
    if(T < 17):
        print("Good Afternoon Sir")
    elif(T >= 17):
        if(T < 21):
            print("Good Evening Sir")   
        else:
            print("Good Night Sir") 


# BONUS EXERCISE (WHILE LOOP)

X = int(input("Enter your speed (in m/s): "))
A = int(input("Enter your Acceleration (in m/s*s): "))

while(X <= 100):
    print("your speed is", X, "m/s")
    X = X + A
else: 
    print("............you are dead bruh :(".center(80))
    

# NORMAL While Loop


i = int(input("Enter the number: "))
while(i <= 20):
    print("your number is: ", i)
    i = 2*i
print("Loop Done")

# EMULATED DO WHILE LOOP

i = int(input("Enter the Number: "))
while True:
    print("your number is: ", i)
    i = 2*i
    if not i <= 20:
        break
print("Loop Done")

   

