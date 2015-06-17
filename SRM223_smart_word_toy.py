__author__ = 'Tiger'

def smart_word_toy(start, inish, forbid):
    return

def combos(options):
    combos = []
    options = options.split(' ')
    indicies = [len(x) - 1 for x in options]
    while sum(indicies) > 0:
        str = ""
        for i in range(len(options)):
            str += options[i][indicies[i]]
        #decrement the next guy
        for i in range(len(indicies)):
            if indicies[i] > 0:
                indicies[i] -= 1
                break
        combos.append(str)
    str = ""
    for i in range(len(options)):
        str += options[i][indicies[i]]
    combos.append(str)
    return combos


print(combos("abcdefghijkl abcdefghijkl abcdefghijkl abcdefghijk"))