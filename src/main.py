from utils import print_heading
from url_features import *

print_heading()

url = input("Enter URL: ")

print("Length:", url_length(url))
print("HTTPS:", has_https(url))
print("Dots:", count_dots(url))
print("Hyphens:", count_hyphens(url))
print("@ Symbol:", has_at_symbol(url))
print("Contains Numbers:", has_numbers(url))