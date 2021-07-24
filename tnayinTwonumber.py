
#-------------
# PROGRAM N-1
#-------------
#This program get string and giv me middle name

str1 = "JonDipPeta"   #One string
str2 = "JaSonAy"      # Two srring
word=" "              # Variable whith two word plus
arr=[]                # Array whit divide string value

def stringConvert(string):    #Function giv me word in divide string 
    arr.append("".join([(" "+i if i.isupper() else i) for i in string]).strip().split()) # divide string to words
    return(arr)

stringConvert(str1)       # Giv mi first string
stringConvert(str2)       # Give me second string
word=arr[0]+arr[1]        # Array in two value and this value have three value
word=word[1]+" "+word[4]  # first  word  plus second word but it is four value in from array
print(word)               # Show two name 



#------------
#PROGRAM N-2
#------------
# First string plus second string

s1="Ault"           #first string
s2="Kelly"          # Second string
def divide(word):   # function in divide word 
    return [char for char in word]  

s3=divide(s1)       # function value get array s3

# Version one
# s1=s3[0]+s3[1]+s2+s3[2]+s3[3] 
# print(s1)

# Second version
s1=" "    # We not recuired value s1 and we change s1= string" 
for i in range(len(s3)):  
    if i == len(s3)/2:  
        s1=s1+s2
    else:
        s1=s1+s3[i] 

print(s1)


