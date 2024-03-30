import random
import string

def pWord():
    print("Generate your customized password:\n")
    length = int(input("Password length: "))
    num_count = int(input("How many numbers? "))
    char_count = int(input("How many characters? "))
    special_count = int(input("How many special characters? "))
    
    total_count = num_count + char_count + special_count