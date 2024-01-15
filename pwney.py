from argparse import ArgumentParser
import random
import string

upper_letters = string.ascii_uppercase
lower_letters = string.ascii_lowercase
special_chars = string.punctuation
number_list = string.digits
char_pool=[]
pwd_pool=[]

parser = ArgumentParser(description='Pwney Basic Wordlist Generator')

# adding arguments
parser.add_argument('-f','--filename', type=str, required=True, help="Specify the output filename")
parser.add_argument('-a','--amount',  type=int , required=True, help="Specify the number of passwords to generate")
parser.add_argument('-p', '--pwdlength', type=int, required=True, help="Specify the length of each password")
parser.add_argument('-u', '--upper', action='store_true', help='Enable uppercase characters')
parser.add_argument('-l', '--lower', action='store_true', help='Enable lowercase characters')
parser.add_argument('-s', '--special', action='store_true', help='Enable special characters')
parser.add_argument('-n', '--numbers', action='store_true', help='Enable numeric digits')

args = parser.parse_args()

# default creation
if not (args.upper or args.lower or args.special or args.numbers):
          for a in upper_letters:
           char_pool.append(a)
          for b in lower_letters:
           char_pool.append(b)
          for c in number_list:
           char_pool.append(c)
          for d in special_chars:
           char_pool.append(d)

else:
   
# custom creation
   if args.upper:
       for i in upper_letters:
           char_pool.append(i)
       
   if args.lower:
       for i in lower_letters:
           char_pool.append(i)
   
   if args.special:
       for i in special_chars:
           char_pool.append(i)   
   
   if args.numbers:
       for i in number_list:
           char_pool.append(i)

# Greeting   
def greeting():
# Meet Pwney *.*
    art = r"""
     ⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣠⣤⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀
     ⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
     ⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
     ⠀⠀⠀⠘⣿⣿⣿⣿⠟⠁⠀⠀⠀⠹⣿⣿⣿⣿⣿⠟⠁⠀⠀⠹⣿⣿⡿⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⢼⣿⠀⢿⣿⣿⣿⣿⠀⣾⣷⠀⠀⢿⣿⣷⠀⠀⠀⠀⠀
     ⠀⠀⠀⢠⣿⣿⣿⣷⡀⠀⠀⠈⠋⢀⣿⣿⣿⣿⣿⡀⠙⠋⠀⢀⣾⣿⣿⠀⠀⠀⠀⠀
     ⢀⣀⣀⣀⣿⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣿⣾⣿⣷⣦⣤⣴⣿⣿⣿⣿⣤⠤⢤⣤⡄
     ⠈⠉⠉⢉⣙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣀⣀⣀⡀⠀
     ⠐⠚⠋⠉⢀⣬⡿⢿⣿⣿⣿⣿⣿⣿   ⣿⣿⣿⣿⣿⣿⣿⡿⣥⣀⡀⠈⠀⠈⠛
     ⠀⠀⠴⠚⠉⠀⠀⠀⠉⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠋⠁⠀⠀⠀⠉⠛⠢⠀⠀
     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
░       ░░  ░░░░  ░   ░░░  ░        ░  ░░░░  ░
▒  ▒▒▒▒  ▒  ▒  ▒  ▒    ▒▒  ▒  ▒▒▒▒▒▒▒▒  ▒▒  ▒▒
▓       ▓▓        ▓  ▓  ▓  ▓      ▓▓▓▓▓    ▓▓▓
█  ███████   ██   █  ██    █  ██████████  ████
█  ███████  ████  █  ███   █        ████  ████
"""
    print(f"\033[34m {art} \033[0;37;40m \n")

# creates the wordlist
def create_wordlist():
    
    try:

        for i in range(args.amount): 
         
         password = ''.join(random.choice(char_pool) for _ in range(args.pwdlength))
         pwd_pool.append(password)

        print("{args.amount} password generated!")

    except:

        print("Failed to generate passwords!")

    return pwd_pool

# save wordlist
def save():
    try:
        filename = args.filename
        if ".txt" in filename:
            f = open(args.filename, "w")
        else:
            f = open(filename + ".txt", "w")
        
        for i in pwd_pool:
            f.write(i+"\n")

        f.close()
        print("Save successfull!")
        
    except:

        print("Failed to save!")

greeting()
create_wordlist()
save()


