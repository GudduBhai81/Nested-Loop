#take input of a word
string = input("Please Enter your own word = ")
char5 = input("Please enter your own character = ")
i = 0
count = 0
#loop will to find the occurence of chracter
while (i < len(string)):
    
    if(string[i] == char5):
        count = count + 1
    i = i + 1

print("The total number of times", char5, "has Occured = ", count)