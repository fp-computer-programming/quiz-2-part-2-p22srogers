# Author: SMR (AMDG) 12/3/21

# Step 1 Input: 
question = input("What letter day is is today? ")
# Step 2 Format: 
question=question.capitalize()
# Step 3 Organize which Letters are meeting vs. not meeting.
meeting = ["A", "C", "E"]
not_meeting = ["B", "D", "F", "G"]
# Step 4 Conditionals
if(question in meeting):
    print("You have Tech & Coding today because it is {0} day.".format(question))
elif(question in not_meeting):
    print("You do not have Tech & Coding today because it is {0} day.".format(question))
else:
    print("Please re-check what you put in! ")
    