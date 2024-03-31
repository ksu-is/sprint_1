import random
import string

def pWord():
    print("Generate your customized password:\n")
    length = int(input("Password length: "))
    num_count = int(input("How many numbers? "))
    char_count = int(input("How many characters? "))
    special_count = int(input("How many special characters? "))
    
    total_count = num_count + char_count + special_count
    
    if total_count > length:
        print("you have exceeded password length. Please try again.")
        return
    
    num = ''.join(random.choices(string.digits, k=num_count))
    chars = ''.join(random.choices(string.ascii_letters, k=char_count))
    special = ''.join(random.choices(string.punctuation, k=special_count))
    
    the_key = num + chars + special
    
    pass_list = list(the_key)
    random.shuffle(pass_list)
    the_key = ''.join(pass_list)
    
    print("Your customized randomized password is:", the_key)
