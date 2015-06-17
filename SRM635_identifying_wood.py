__author__ = 'Tiger'

def identifying_wood(s, t):
    if t == "":
        return "Yep, it's wood"
    if s == "":
        return "Nope"
    if s[0] == t[0]:
        return identifying_wood(s[1:], t[1:])
    else:
        return identifying_wood(s[1:], t[:])

print(identifying_wood("absdefgh", "asdf"))
print(identifying_wood("oxoxoxox", "ooxxoo"))
print(identifying_wood("oxoxoxox", "xxx"))
print(identifying_wood("qwerty", "qwerty"))
print(identifying_wood("string", "longstring"))
