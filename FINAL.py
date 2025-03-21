import sys
name = input('Greetings! What is your name? (please type your name)-> ')
print(f"Hello {name}! I am Mr.QuickFix I will be assisting you with your concern today!")
print('However, before moving forward I need to verify you are human.\nI am going to ask you to type in a word, please type it exactly as it appears.')
verificationWord = "paradise"
attempts = 0
max_attempts = 3
while attempts < max_attempts: 
    guess = input("Please type in paradise.-> ") 
    if guess == verificationWord:
        print('Wonderfull! Moving forawrd.\n')
        break
    else:
        attempts += 1
        print('Please confirm you are typing the word EXACTLY as it appears & try again.')
if attempts == max_attempts:
        print("Robot detected, please restart the program.")
        sys.exit()
issues = ['Network connectivity', 'Slow computer performance', 'System crashing']
for i in range(len(issues)):
    print(f"{i+1}. {issues[i]}\n")
  
def get_first_response():
    while True:
            first_response = int(input("I know you're here due to issues with your network,\nplease enter in the number from the list above\nthat corresponds closest to the issue you are encountering.-> "))
            if first_response in [1, 2, 3]:
                return first_response
            else:
                print("Please only enter 1, 2, or 3.")
first_response = get_first_response()
if first_response == 1:
    print('\nNetwork connectivity:\nPlease try rebooting the router or modem & let me know if that remedies the issue you are facing.')
elif first_response == 2:
    print('\nSlow computer performance:\nPlease uninstall any unused apps & programs & see if that remedies the issue your facing.')
elif first_response == 3:
    print('\nSystem crashing:\nYour software & drivers could need updating, please verify they are up to date.')
def get_response_1():
    while True:
        response1 = input("Please type yes if that corrected the issue & no if it did not.-> ")
        if response1.lower() == "yes" or response1.lower() == "no":
            return response1
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
response1 = get_response_1()
def get_survey_results():
    while True:
        try:
            satisfaction = int(input("On a scale of 1-5 with 5 being great & 1 being not great, how would you rate your experience with Mr.QuickFix?-> "))
            if 1 <= satisfaction <= 5:  
                print(f"Thank you for your participation! Your rating: {satisfaction}")
                sys.exit()
            else:
                print("Please only enter a number between 1 & 5.")  
        except ValueError:  
            print("Please only enter a valid number between 1 & 5.")
if response1 == "yes":
    print("Okay! I  am glad to hear it was successfull, please partake in the following brief survey. Until next time "+ name + "!")
    print("\nSURVEY")
    get_survey_results()
elif response1 == "no":
    print("\nIf you selected option 1 please try checking all the physical wiring cables to make sure they are not damaged. Faulty cabling can upset your connection.\n\nIf you selected option 2 your nodes slow performance can be due to bloatware. Please try disabling all startup programs.\n\nIf you selected option 3 dust can be the culprit of your problems. Try giving your hardware a thorough cleaning to see if that helps.")
    def get_response_b():
        while True:
            responseb = input("\nPlease type yes if this corrected the issue & no if it did not.-> ")
            if responseb.lower() == "yes" or responseb.lower() == "no":
                return responseb
            else:
                print("Please only type 'yes' or 'no'.")
    responseb = get_response_b()  
    if responseb == "yes":
        print("\nOkay! I am glad to hear it was successfull, please partake in the following brief survey. Until next time "+ name + "!")
        print("\nSURVEY")
        get_survey_results()
    elif responseb=="no":
         print("This issue is beyond my capabilites, please reachout to your closest IT professional.")
         sys.exit()
    while True:
        try:
            satisfaction1 = int(input("On a scale of 1-5 with 5 being great & 1 being poor, how would you rate your experience with Mr.QuickFix?-> "))
            if 1 <= satisfaction1 <= 5:  # Check if input is within the valid range
                print(f"Thank you for your participation! Your rating: {satisfaction1}")
                sys.exit()
            else:
                print("Please enter a number between 1 & 5.")  
        except ValueError:  
            print("Please enter a number between 1 & 5.")
        if responseb == "no":
            print("This issue is beyond my capabilites, please reachout to your closest IT professional.")
            sys.exit()
        if responseb == "yes":
            print("Okay! I am glad to hear it was successfull, please partake in the following brief survey. Until next time "+ name + "!")
            print("\nSURVEY")
            satisfaction = input("On a scale of 1-5 with 5 being great & 1 being not great, how would you rate your experience with Mr.QuickFix?_> ")
            print("Thank you for your participation!")
            sys.exit()
