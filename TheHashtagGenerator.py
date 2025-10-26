"""The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false"""

def generate_hashtag(s):
    if not s:
        return False
    else:
        split_s = s.split()
        for i in range(len(split_s)):
            split_s[i] = split_s[i].lower().capitalize()
        print(split_s)
        output = ('#' + "".join(split_s))
        if len(output) > 140:
            return False
    return output
