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

