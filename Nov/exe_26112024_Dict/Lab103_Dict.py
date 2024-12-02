#Frequency of characters in a string
#write a program to count the frequency of each character on a given string
string="automation"
string=input("Enter the the input e.g automation")

#{a:2,u:1,t:2,0:2,m:1,i:1,n:1}

char_count={}

#logical bilding
#I/P--- string
#O/P--> dict
for char in string:
    char_count[char]=char_count.get(char,0) +1
print(char_count)