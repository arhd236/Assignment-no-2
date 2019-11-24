#!/usr/bin/env python
# coding: utf-8

# In[13]:


#Assignment no 2
#Write a program which takes 5 inputs from user for different subject’s marks, total it and generate mark sheet using grades ?

math = int(input("Math Obtained Marks: "))
english = int(input("English Obtained Marks: "))
physics = int(input("Physics Obtained Marks: "))
chemistry = int(input("Chemistry Obtained Marks: "))
computer = int(input("Computer Obtained Marks: "))

total_obtained_marks = math+english+physics+chemistry+computer
total_marks = 500;
percentage = (total_obtained_marks*100)/total_marks

print("Total Obtained Marks: " + str(total_obtained_marks))
print("Percentage: " + str(percentage) + "%")

if percentage >= 90:
    print("Your Grade is: A+")
elif percentage >= 80 and percentage < 90:
      print ("Your Grade is: A")
elif percentage >= 70 and percentage < 80:
      print ("Your Grade is: B+")
elif percentage >= 60 and percentage < 70:
      print ("Your Grade is: B")
elif percentage >= 50 and percentage < 60:
      print ("Your Grade is: C+")
elif percentage >= 40 and percentage < 50:
      print ("Your Grade is: C")
else:  print ("Your Grade is: F")


# In[16]:


#Write a program which take input from user and identify that the given number is even or odd?

number = int(input("Enter a number: "))
if number%2 == 0:
    print(str(number) + " is a even number")
else:
    print(str(number) + " is a ood number")


# In[19]:


#Write a program which print the length of the list?

friends = ["Aamir", "Wajid", "Kashif", "Ovais", "Sahib"]
print("Length of the List is: " + str(len(friends)))


# In[21]:


#Write a Python program to sum all the numeric items in a list?
#Write a Python program to get the largest number from a numeric list.

number_list = [23, 34, 45, 67, 78]
print("The sum of the list items is: " + str(sum(number_list)))
print("The largest number of the list is: " + str(max(number_list)))


# In[25]:


#write a program that prints out all the elements of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b= a[:4]

print(b)

print ([ x for x in a if x < 5 ])


# In[ ]:




