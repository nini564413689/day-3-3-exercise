# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
  result = "This year is a leap year."
  if year % 100 == 0:
    result = "This year is not a leap year."
    if year % 400 == 0:
      result = "This year is a leap year."
    else:
      result = "This year is not a leap year."
  else:
    result = "This year is a leap year."
else:
  result = "This year is a not leap year."

print (result)