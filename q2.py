string=input("please enter your String")
search=input("Please enter your Search")
count=0
for i in range(len(string)):
    if(string[i]==search):
        count = count + 1
print(count)