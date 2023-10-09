#WAP to demonstrating the "if" Statement
name=input("Enter Your Name \n")
regno=input("Enter Your Reg.no \n")
marks=int(input("Enter Your Average Marks:"))
print("***********************************************")
if marks>=90:
    if marks>75 and marks<=100:
        print ("Congratulations! {0} {1} You have passed with Distinction.".format(name,regno))
    elif marks>=60 and marks<=74:
        print ("{0} {1},You have Passed with First Class Honours!".format(name,regno))
    elif marks>=45 and marks<=59:
        print ("{0} {1},You Have Passed With Second Class Honors!".format(name,regno))
    elif marks>=35 and marks<=44:
        print ("{0} {1},You Have Passed With Third Class Honors!".format(name,regno))
    else:
        print("Sorry, you failed this time :( ")