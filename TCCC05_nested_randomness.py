__author__ = 'Tiger'

def nested_randomness(n, nestings, target):
    prob = [1 / n] * n
    for nest in range(1, nestings):
        for i in range(0, n - nest + 1):
            temp = 0
            for j in range(i + 1, n - nest + 1):
                #print("i:{} | {}/{} * {}".format(i, 1, j, prob[j]))
                temp += 1/j * prob[j]
            prob[i] = temp
    return prob[target]

print(nested_randomness(5, 2, 1))
print(nested_randomness(10, 4, 0))
print(nested_randomness(1000, 10, 990))