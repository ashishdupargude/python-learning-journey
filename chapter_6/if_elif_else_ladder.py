#elif else ladder

b = int(input(" enteryour age:"))
if(b>=18):
    print("you are above the age of consent")
    print("good for you")

elif(b<0):
    print("you are entered an invalid negative age")

elif(b==0):
    print("you are entering 0 which is not vaild age")

else:
    print("you are below the age of consent")

print("End of Program")
