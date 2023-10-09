#WAP to demonstrate/find factorial of a given number;
def fact(n):
#Checking the number is 1 or 0 then return 1 otherwise return factorial.
    if(n==1 or n==0):
        return (1)
    else:
        return(n*fact(n-1))
num=int(input("Enter a number:\n>"))
print("Number:",num)
print("Factorial of the given number is:\n>",fact(num))