# Write a program to count the number of vowels and consonants in a string. 
s= input("enter a string : ")# ram is good boy
vovelCount=0
consCount=0
for ch in s:
    if ch>='a' and ch<='z':    
      if ch in "aeiou":
          vovelCount+=1
      else:
          consCount+=1


print(f"vovle count : {vovelCount}")
print(f"constent count : {consCount}")
