# Author: SMR (AMDG) 12/3/21
# Step 1: Input Statement
positive_emotion = input("Enter an emotion for Oscar to respond to: ")
# Step 2: Negative Emotion
negative_emotion = "not"
# Step 3: Conditional
if negative_emotion in positive_emotion:
    print(positive_emotion)
if negative_emotion not in positive_emotion:
    print("You're {0} {1},".format(negative_emotion, positive_emotion)+" now SCRAM!")
    