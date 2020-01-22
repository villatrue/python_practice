import string
import random
import argparse

# create a unique password thay uses uppercase, lowercase

parser = argparse.ArgumentParser()
parser.add_argument("length", type=int, help="How Long")
parser.add_argument("--upper", action='store_true')
parser.add_argument("--lower", action='store_true')
parser.add_argument("--digits", action='store_true')
parser.add_argument("--punctuation", action='store_true')

args = parser.parse_args()

length = args.length
use_upper = args.upper
use_lower = args.lower
use_digits = args.digits
use_punctuation = args.punctuation

# use_digits = True
# use_special = True

characters = ''

if use_upper:
    characters += string.ascii_uppercase 

if use_lower:
    characters += string.ascii_lowercase

if use_digits:
    characters += string.digits

if use_punctuation:
    characters += string.punctuation

password = ''

for i in range(length):
    password += random.choice(characters)

print(password)
