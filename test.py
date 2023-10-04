# import re
#
# email_pattern = r'\b[b]{1-3}\b'
#
# with open('emails1.txt', 'r') as file:
#     text = file.read()
# email_addresses = re.findall(email_pattern, text)


# import re
#
# pattern = r'\d+'
# text = "There are 123 apples and 456 oranges in the basket."
# matches = re.finditer(pattern, text)
# #print(type(matches))
#
# for match in matches:
#     print("Match found:", match.group())
import re

pattern = r'\b (\d+)-(\d+) apples \b'
text = "There are 123-125 apples and 456 oranges in the basket."
matches = re.findall(pattern, text)

print("All matches:", matches)

# import re
#
# pattern = r'(\d+)-(\d+)-(\d+)'
# text = "Date of birth: 2000-01-15"
# match = re.search(pattern, text)
#
# if match:
#     year = match.group(1)
#     month = match.group(2)
#     day = match.group(3)
#     print(f"Year: {year}, Month: {month}, Day: {day}")

