"""Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

Inputs: "abc", "bc"
Output: true

Inputs: "abc", "d"
Output: false"""

def solution(text, ending):
    if len(ending) > len(text):
        return False
    for i in range(len(ending)):
        spot = ((i+1) * -1)
        if not text[spot] == ending[spot]:
            return False
    return True

# endswith exists, oops
