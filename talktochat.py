#basic chat bot to communicate with chat gpt and access it's API to complete a message request
#allows you to choose which version of chatgpt you'd like, and let's you talk to it from the terminal!

import openai
import sys

#put ur api key here :3
api_key = "PUTURKEYHERE"
openai.api_key = api_key
#convohistory will just append the messages you send to gpt and also the messages you receive to itself
convohistory = []
#chat needs to specify you as a user or as the system
roles = ["system","user"]
#to check when to leave the program
exitToken = "goodbye"
#keeps track of the input and output texts
userinput = [""]
systemoutput = ""
model = "gpt-4o-mini"

#gets all the available models of chat gpt
id = [id for id in list(map(lambda d: d.id, list(openai.models.list()))) if 'gpt' in id]
#print(id)


# ANSI escape codes for bold and colors
BOLD = "\033[1m"
RESET = "\033[0m"  # Reset to default
# Define some color codes for customization
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"



#this function gets an output or reply (completion) from chat gpt based on an input given by messages
#we specify messages to be convohistory, therefore chat generates a response based on the back and forth there as well as 
#the last message sent to it

def answerquestion():
    completion = openai.chat.completions.create(
        model = model,
        messages = convohistory,
        #set to 200 to limit how many tokens we use cuz i don't wanna run out of money lol
        max_tokens=200
    )
    #the choices attribute contains a list of the generated completions; [0] accesses the first one
    #.messages accesses the message from the choice
    #print(completion.choices[0].message.content) ###the .content extracts only the actual text while .message itself contains other info
    answer = completion.choices[0].message.content
    return answer



#gets user input and returns it as a string so i can put it in the while loop
def getInput(userinput, inputstring):
    userinput[0] = input(f"\n{BOLD}{MAGENTA}{inputstring}{CYAN}")
    if userinput[0] == "":
        return " "
    return str(userinput[0])



#prints a header at the beginning of the program
print(f"{BOLD}{GREEN}*******************************************************************{RESET}")
print(f"{BOLD}{GREEN}welcome to chat bot lol, talk to any version of gpt you want to!{RESET}")
print(f"{BOLD}{GREEN}if you want to exit this program simply type 'goodbye'{RESET}")
print(f"{BOLD}{GREEN}here are the different types of gpt you can try: {RESET}")
print(f"{BOLD}{CYAN}"+str(id))
print(f"{BOLD}{GREEN}*******************************************************************\n{RESET}")



while getInput(userinput, "enter model version: "):

    if userinput[0].lower() == "goodbye":
        sys.exit()

    if (userinput[0] not in id) or (userinput[0]==""):
        print(f"{BOLD}{YELLOW} error: not a valid name, enter a valid name from the list")
        continue
    
    else:
        model = userinput[0]
        break



#main body of communication
#starts by getting a user prompt to ask chat
while getInput(userinput, "talk to me: "):

    #appends the user input to the message history by attributing the input to the content value
    convohistory.append({"role": "user", "content": userinput[0]})
    #gets the output of chat and adds it to the message history
    systemoutput = answerquestion()
    convohistory.append({"role": "system", "content": systemoutput})
    #prints chat output
    print(f"\n{BOLD}{MAGENTA}gpt: {CYAN}{systemoutput}")

    #checks for exit
    if(userinput[0].lower()==exitToken):
        break




