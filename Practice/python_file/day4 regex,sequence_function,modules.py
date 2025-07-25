#regular expression

import re


def is_notvalid_phone_number(number):
  pattern = r'^\d{10}$'
  return re.match(pattern,number) is not None

def is_valid_email(email):
  pattern = r'^\b[\w.-]+@[\w.-]+\.\w+\b$'
  return re.match(pattern,email) is not None

print(is_notvalid_phone_number("1234567890")) #true
print(is_notvalid_phone_number("34546655")) #false

print(is_valid_email("sheriff@gmail.com"))# true
print(is_valid_email("notvalid.email"))#false

text = "Contact us at support@site.com or sales@company.org"
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
print(emails)  # ['support@site.com', 'sales@company.org']


#grouping with paranthesis

date = "order placed on 25-07-2025"
match = re.search(r'(\d{2})-(\d{2})-(\d{4})',date)
day,month,year = match.groups()
print(f"dob day is {day}, month is {month}, year is {year}")

def detect_choice(response):
    match = re.search(r'yes|no', response.lower())
    return match.group() if match else "No match"

print(detect_choice("Yes, I agree."))  # yes
print(detect_choice("No problem."))    # no

text1 = "so funny!, hahahaha"
match1 = re.search(r'(ha)*',text1)
print(match1.group())



#sequence functions===================================================================================

# filter
marks = [70,89,79,98,56,86,89]
passed = list(filter(lambda x: x>85,marks))
print(passed)


#map
price_usd = [10,20,30]
price_inr = list(map(lambda x:x*85.5,price_usd))
print(price_inr)

#reduce
from functools import reduce
cart_item = [100,200,300,600]
total = reduce(lambda x,y: x+y, cart_item)
print(total)

#zip
a = ["apple","banana","carrot"]
b = [1,2,3]
zipped_c = list(zip(a,b))
print(zipped_c)

#enumerate
questions = ["who r u","whats ur name"]
for i,q in enumerate(questions,start = 1):
  print(f"{i}:{q}")


#sorted
student = [("alice",90),("ben",70),("charlie",80)]
sort_stu = sorted(student,key= lambda x:x[0],reverse = True)
print(sort_stu)


#any
#all
access_right = [True,False,True]
print(any(access_right))# true
print(all(access_right))# false



#reversed
names = ["Alan","Baggey","Chara"]
print(list(reversed(names)))




#pymodules===============================================================================



import os
print("Current Directory:", os.getcwd())
print("Files:", os.listdir('.'))
#output like
#Current Directory: E:\final code hexa try\stream specific training\python_try_intros
#Files: ['pymodules.py', 'regexdemo.py', 'sequence_function.py']

import math
num = 4
print(f"Square root of {num} is : ",int(math.sqrt(num)))
print(f"power of {num} is : ",math.pow(num,3))

print(math.sqrt(16))
print(math.ceil(2.3))
print(math.floor(2.9))

from datetime import datetime
dte = datetime.now()
print(datetime.now())
print(datetime.strptime('2024-01-01', '%Y-%m-%d')) # str to datetime
print(datetime.now().strftime('%Y-%m-%d')) # datetime to str

import random
print(random.randint(1, 10))
print(random.choice(['a','b']))

mylist = ["higher","near","fear","mere","here","wear","tear","gear","rear",1,2]
print(random.shuffle(mylist))



import json
data = {"name": "Alice", "age": 25}
json_str = json.dumps(data)
print("JSON:", json_str)


import statistics
print("Mean:", statistics.mean([10, 20, 30]))


import re
text = "My number is 123-456-7890"
match = re.search(r'\d{3}-\d{3}-\d{4}', text)
print("Phone:", match.group())
