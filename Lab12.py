#WAP to copy the content of  a file into another file

sf=input(print("Enter the name of the source file "))

tFile=input(print("Enter the name of the destination file "))
#Reading the content/texts of the source file..
fileHandle1=open(sf, "r")
texts=fileHandle1.readlines()
#fileHandle1.close()
#writing/copying the contents of source file into destination file..
fileHandle2=open(tFile,"w")
for s in texts:
    fileHandle2.write(s)
fileHandle2.close()
print("File copied successfully! :)")