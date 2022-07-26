import numpy as np
from scipy.linalg import hadamard

#Integers only.
#1. Get number of users. 
#2. Generate codes.     
#3. Get messages from each user.
#4. Squash messages into signal.
#5. Print signal.
#6. Ask which user.
#7. Print message.



userCodeDictionary = {}
numberOfUsers = 0
messages = {}
signal = 0
codeLength = 0

def getNumberOfUsers():
    global numberOfUsers, codeLength
    print("Input number of users: ")
    numberOfUsers = int(input())
    codeLength = 1 if numberOfUsers == 0 else np.exp2(np.ceil(np.log2(numberOfUsers)))
    return

def generateCodes():
    hadamardMatrix = hadamard(codeLength)
    for user in range(numberOfUsers):
        userCodeDictionary[user] = (hadamardMatrix[user])
    return

def getMessages():
    for user in range(numberOfUsers):
        print("Input message for user (must be integer) " + str(user) +".")
        while True:
            try: 
                message = int(input())
                break
            except ValueError:
                print("MUST BE INTEGER >:(")
        messages[user] = message
    return
def squashMessages():
    global signal
    for user in messages:
        signal += messages[user] * userCodeDictionary[user]
    print("The transmitted signal is: " + str(signal))

def printMessage():
    global signal
    user = ""
    while(user != "exit"):
        print("Enter user number: ")
        user = input()
        try: 
            message = int(np.dot(signal, userCodeDictionary[int(user)])/codeLength)
            print("The message for user " + str(user) + " is: " + str(message))
        except:
            print("User not found.")


getNumberOfUsers()
generateCodes()
getMessages()
squashMessages()
printMessage()