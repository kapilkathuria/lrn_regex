import re

# search -find the first match
# r"cat" - search for cat word
print(re.search(r"cat", "A caat and a rat can't be caat educated friends."))

# r".at" - . means any character. this will match cat, rat, @at etc.
print(re.findall(r".at", "cat bat @at"))

# [xyz] means e.g. either an "x", an "y" or a "z". ]
print(re.findall(r".[abc]t", "cat cbt dct adt"))

# [a-e] a simplified writing for [abcde] or [0-5] denotes [012345].
# [A-Za-z] - all characters in small and caps
# [az-] - dash befor and after doens't have any special meaning
print(re.findall(r".[a-d]t", "cat cbt dct adt"))

# ^ - negates the choice if it is first char after [
# [^0-9] - any character but a digit
# [^abc] - anything but an "a", "b" or "c" but
# [a^bc] means an "a", "b", "c" or a "^"
print(re.findall(r".[^a-c]t", "cat cbt dct adt"))

# done till "a", "b" or "c" [a^bc] means an "a", "b", "c" or a "^" on https://www.python-course.eu/python3_re.php

