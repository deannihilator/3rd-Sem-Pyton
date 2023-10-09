#WAP to demonstrate the String Operations....
str1="Welcome You All Students"
capital=str1.upper()    #converting the above string into UPPERCASE
print(capital)          
small=str1.lower()      #converting the above string into LOWERCASE
print(small)            
#Replacing "Students" with "Engineers" in the above String....
str2=str1.replace("Students","Engineers")  #replaced
print(str2)
#Strip Example
st="This is an Example of Strip"
left=st.lstrip()
print(left)
right=st.rstrip()
print(right)
#prefix operations on string
prefix1=str1.startswith("Welcome")
print(prefix1)
prefix2=str2.startswith("W")
print(prefix2)
prefix3=str2.endswith("S")
print(prefix3)