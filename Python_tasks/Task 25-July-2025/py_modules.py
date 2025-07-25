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

