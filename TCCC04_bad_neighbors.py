__author__ = 'Tiger'

def bad_neighbors(donations):
    money = list(donations)
    #money[i] is going to be max donation including donations[i]
    #money[i] = max(money[j] + donations[i]) where j < i - 1
    for i in range(1, len(donations)):
        for j in range(1, i - 1):
            if money[j] + donations[i] > money[i]:
                money[i] = money[j] + donations[i]

    money2 = list(donations)
    for i in range(len(donations) - 1):
        for j in range(i - 1):
            if money2[j] + donations[i] > money2[i]:
                money2[i] = money2[j] + donations[i]

    return max([max(money), max(money2)])

print(bad_neighbors([10, 3, 2, 5, 7, 8]))
print(bad_neighbors([11, 15]))
print(bad_neighbors([7, 7, 7, 7, 7, 7, 7]))
print(bad_neighbors([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
print(bad_neighbors([94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61, 6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397, 52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72]))
