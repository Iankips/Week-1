import random
import string

print("An 8-digit Password Generator.")

def get_string(lower_count, upper_count, digits_count,symbol_count):
    lower = ''.join((random.choice(string.ascii_lowercase) for i in range(lower_count)))
    upper = ''.join((random.choice(string.ascii_uppercase) for i in range(upper_count)))
    digits = ''.join((random.choice(string.digits) for i in range(digits_count)))
    symbol = ''.join((random.choice(string.punctuation) for i in range(symbol_count)))
    
    sample_list = list(lower + upper + digits + symbol)
    random.shuffle(sample_list)
    final_string = ''.join(sample_list)
    print(final_string)
    
get_string(2, 2, 2, 2)