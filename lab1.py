#1.Find The greatest common divisor of multiple numbers read from the console.


def gcdc(num1,num2):
    maxn=max(num1,num2)
    minn=min(num1,num2)
    if(minn==0):
        return maxn
    return gcdc(maxn%minn,minn)

numbers = input("Enter the numbers (separated by spaces): ").split()

def gcdd(*nums):
    ret=1
    for i in range(len(nums)-1):
        ret=gcdc(nums[i],nums[i+1])
    return ret
numbers = [int(num) for num in numbers]



# Print the result
#print("The greatest common divisor is:", gcdd(*numbers))
#2.Write a script that calculates how many vowels are in a string.
def vowels(s):
    c = 0
    s=s.lower()
    for l in s:
        if (l in "aeiou"):
            c = c+1
    return c         
#print(vowels("kangaroo"))
#3.Write a script that receives two strings and prints the number of occurrences of the first string in the second.
def findc(s1,s2):
    c = 0
    p = 0
    for l in s2:
        if(l==s1[p]):
            if (p == len(s1) - 1 ):
                c = c + 1
                p = 0
            else:
                p = p + 1
        else: p=0
    return c            
#print(findc("dog","A dooog doooooog dooog walks besides another dog while talking about dogs"))
#4.Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.
def convert(str):
    newstring=""

    for i in range(len(str)):
        if(str[i].isupper() and i != 0):
            newstring+="_"
        newstring+=str[i].lower()
    return newstring


       

print(convert("UpperCamelCaseWordAA"))    


#5.
#firs      1  2  3  4    =>   first_python_lab
#n_lt      12 13 14 5
#oba_      11 16 15 6
#htyp      10 9  8  7


#6.Write a function that validates if a number is a palindrome.
def isPalindrome(n):
    s = str(n)
    for i in range(0,len(s)//2):
        if(s[i]!=s[len(s)-1-i]):
            return False
    return True
#print(isPalindrome(3333))
#7.Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", this function will return 123, or if the text is "abc123abc" the function will extract 123). The function will extract only the first number that is found.
def firstNumber(text):
    isNum=False
    number=0
    for c in text:
        if(ord('0')<=ord(c)<=ord('9')):
            if (not isNum):
                isNum=True
                number*=10
                number+=ord(c)-ord('0')
            else:
                number*=10
                number+=ord(c)-ord('0')
        else:
            if(isNum):
                return number
#print(firstNumber("An apple is 123 USD"))
#8.Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"
def binonescount(n):
    c = 0
    c += n % 2
    while (n != 0):
        n = n >> 1
        c += n % 2
    return c
#print(binonescount(15))

#9.Write a functions that determine the most common letter in a string. For example if the string is "an apple is not a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered. Casing should not be considered "A" and "a" represent the same character.
def occCount(s):
    ls=s.lower()
    lettercount=[0]*26
    for c in ls:
        if (ord('a')<=ord(c)<=ord('z')):
            lettercount[ord(c)-ord('a')]+=1
    maxlettercount = 0
    for i in lettercount:
        if(i>maxlettercount):
            maxlettercount=i
    return maxlettercount

        
#print(occCount("an apple is not a tomato aaaaa"))
#10.Write a function that counts how many words exists in a text. A text is considered to be form out of words that are separated by only ONE space. For example: "I have Python exam" has 4 words.

def wordCount(text):
    return len(text.split(" "))

#print(wordCount("I have Python exam"))