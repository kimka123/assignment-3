#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1

age = int(input('Please enter your age: '))

citizenship =input('Are you a citizen? ')

if age>= 18 and citizenship == "yes":
        print("You are eligible to vote!")

if age < 18:
            print("You are not elligible for voting.")

if  citizenship != "yes":
    print('you are not eligible for voting')
    


# In[16]:


#Q2

y = int(input('Input year: ')) 
 
if (y%100==0 and y%400==0) or (y%100!=0 and y%4==0): 
    print(f'{y} is a leap year.') 
else: 
    print(f'{y} is NOT a leap year.')    


# In[18]:


#Q3

correct_password = "Beren2004"

user_password=input('please enter your password:')

if user_password==correct_password:
    print('Access granted , the password is correct.')

elif user_password != correct_password:
    print('Access denied, the password is incorrect')



# In[20]:


#Q4

valid_months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
month = input('Please insert a month: ')

if month == 'february':
    print(28/29)
    
elif month in valid_months:
    days_in_month = {
        'january': 31,
        'february': 28,
        'march': 31,
        'april': 30,
        'may': 31,
        'june': 30,
        'july': 31,
        'august': 31,
        'september': 30,
        'october': 31,
        'november': 30,
        'december': 31
    }
print(f'There are {days_in_month[month]} days in {month.capitalize()}.')


# In[22]:


#Q5

total_sum = sum(range(1, 21))

print(f"The sum of the numbers from 1 to 20 is: {total_sum}")


# In[23]:


#Q6

numbers = {3, 9, 1, 6, 2, 8}

smallest_number = min(numbers)

print(f"The smallest number in the list is: {smallest_number}")


# In[30]:


#Q7

for num in range(100, 500):
   
    if num % 11 == 0 and num % 2 != 0:
        
        print(num)


# In[31]:


#Q8

numbers = {-2, 13, -4, -5, -6, 10, 20, 30, -12}

positive_sum = sum(num for num in numbers if num > 0)

print(f"The sum of positive numbers in the list is: {positive_sum}")


# In[32]:


#Q9

for num in range(1, 31):

    if num % 5 != 0:
       
        print(num)


# In[35]:


#Q10

CM_TO_INCHES = 2.54

length_cm = float(input("Enter a length in centimeters: "))

if length_cm < 0:
    print("Invalid entry: Length cannot be negative.")
else:

    length_inches = length_cm / CM_TO_INCHES
    
    print(f"{length_cm} centimeters is equal to {length_inches:.2f} inches.")


# In[ ]:




