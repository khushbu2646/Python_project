print("Welcome to the Cybersecurity quiz!")
Playing = input("Do you want to play: ")

if Playing != "yes":
    quit()

print("let's play now :)")
Current_score = 0

First_Question = input("First question: What does the 'C' stand for in CIA, a fundamental concept in cybersecurity? ")
if First_Question == "Confidentiality":
    print("CORRECT! ")
    Current_score += 1
else:
    print("WRONG")

second_question = input("Second Question: Which type of malware is designed to block access to a computer system until a sum of money is paid?: ")
if second_question == "Ransomware":
    print("CORRECT! ")
    Current_score += 1
else:
    print("WRONG")

Third_question = input("Third Question: What is the purpose of a firewall in a computer network?: ")
if Third_question == "Security and access control":
    print("CORRECT! ")
    Current_score += 1
else:
    print("WRONG")

Fourth_question = input("Fourth Question: Which encryption method uses different keys for encryption and decryption?: ")
if Fourth_question == "Asymmetric":
    print("CORRECT! ")
    Current_score += 1
else:
    print("WRONG")

Fifth_question = input("Fifth Question: Which term refers to a simulated environment used to detect and analyze cyber threats?: ")
if Fifth_question == "Sandbox":
    print("CORRECT! ")
    Current_score += 1
else:
    print("WRONG")

print("You got " + str(Current_score) + "questions correct!")
print("You got " + str((Current_score / 5) * 100) + "%.")


