# Author: SMR (AMDG) 12/3/21
# Step 1: Input Statement
emotion = input("Enter an emotion for Oscar to respond to: ")
# Step 2: Negative Emotion
negative_emotion = "not"
# Step 3: Conditional
if negative_emotion in emotion:
    print(emotion)
if negative_emotion not in emotion:
    print("You're {0} {1},".format(negative_emotion, emotion)+" now SCRAM!")
    