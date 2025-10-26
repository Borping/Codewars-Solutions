"""Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  """""

import re

def solution(s):
    split_s = re.split(r'(?=[A-Z])', s)
    return " ".join(split_s)
