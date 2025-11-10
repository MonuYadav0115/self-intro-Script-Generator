# Challenge self intro Script Generator

# Create a python script that interacts with the user and generates a personalized self- introduction:

# your program should :
# 1. ask the user for their name ,age ,city ,profession and favorite hobby 

# 2. formate this data into a warm friendly paragraph of self indroduction 
# 3. print the final paragraph in clean and read-able formate:

import datetime

name = input("Enter name:").strip()
age = input("Enter age:").strip()
place = input("Enter palce:").strip()
profession = input("Enter prodession:").strip()
hobby = input("Enter hobby:").strip()

intro_message = (

    f"Hello! My name is {name} and i am {age} year old and i am from {place} "
    f" My profession is {profession} and my hobby is {hobby} and nice to meet you :) \n ThankYou\n"

)

current_date = datetime.date.today().isoformat()
intro_message += f"\n Logged on: {current_date}"

border = "*" * 150

final_output = f"{border} \n {intro_message} \n {border}"

print(final_output)


