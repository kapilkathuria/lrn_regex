# https://www.python-course.eu/python3_re.php

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

from urllib.request import urlopen
with urlopen('https://www.python-course.eu/simpsons_phone_book.txt') as fh:
    for line in fh:
        # line is a byte string so we transform it to utf-8:
        line = line.decode('utf-8').rstrip() 
        if re.search(r"J.*Neu",line):
            print(line)

# match() is misleading name, because match(re_str, s) checks for a match of re_str merely 
#   at the beginning of the string. But anyway, match() is the solution to our question, 
#   as we can see in the following example:
#   match is python specific method
s1 = "Mayer is a very common Name"
s2 = "He is called Meyer but he isn't German."
print(re.search(r"M[ae][iy]er", s1))
print(re.search(r"M[ae][iy]er", s2))
 # matches because it starts with Mayer
print(re.match(r"M[ae][iy]er", s1)) 
# doesn't match because it doesn't start with Meyer or Meyer, Meier and so on:
print(re.match(r"M[ae][iy]er", s2))
# below method also works  
print(re.search(r"^M[ae][iy]er", s1))  
print(re.search(r"^M[ae][iy]er", s2))  

# if we combine two line, now for previous searach to work, we will need MULTILINE parameter
# match() never checks anything but the beginning of the string for a match.
s = s2 + "\n" + s1
print(re.search(r"^M[ae][iy]er", s))
print(re.search(r"^M[ae][iy]er", s, re.MULTILINE))
print(re.match(r"^M[ae][iy]er", s, re.M))

# let's search end of line using $
print(re.search(r"Python\.$","I like Python."))
print(re.search(r"Python\.$","I like Python and Perl."))
print(re.search(r"Python\.$","I like Python.\nSome prefer Java or Perl."))
print(re.search(r"Python\.$","I like Python.\nSome prefer Java or Perl.", re.M))

# ? -  A question mark declares that the preceding character or expression is optional.
s3 = "Mayr is a very common Name"
print(re.match(r"M[ae][iy]e?r", s3, re.M))
# below means that 'ruary' is optional
someDateString = "20 Feb 2011"
print(re.match(r"Feb(ruary)? 2011", someDateString, re.M))

# Quantifiers
# * -  following a character or a subexpression group means that this expression or character may be repeated arbitrarily, even zero times..
#   r"[0-9]*" - may or may not have digits
# + The plus operator is very similar to the star operator, except that the character or subexpression followed by a "+" sign has to be repeated at least one time.
#   r"^[0-9]+ " - that means at least first character will be digit
# {} - last expresson will be repeated 
#   r"^[0-9]{4}" - last expresson will be repeated 4 times
#   r"^[0-9]{4,5} [A-Z][a-z]{2,}" - The general syntax is {from, to}. first four characters will be digit 
#       and next atleast two characters will be alphabets

# group(), span(), start() and end(),
mo = re.search(r"^M[ae][iy]er", s, re.M)
print (mo.group())
print (mo.span())
print (mo.start())
print (mo.end())
