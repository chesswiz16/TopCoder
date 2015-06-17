__author__ = 'Tiger'


class KitayutaMart2(object):
    def numBought(self, K, T):
        total_price = 0
        i = 0
        while total_price < T:
            total_price += (2 ** i) * K
            i += 1
        return i

test_cases = {
    (100, 100): 1,
    (100, 300): 2,
    (150, 1050): 3,
    (160, 163680): 10,
}
tester = KitayutaMart2()
for test_case, expected in test_cases.items():
    result = tester.numBought(test_case[0], test_case[1])
    if result != expected:
        print("K: {0}, T: {1} failed. Expected {2} got {3}".format(test_case[0], test_case[1], expected, result))
    else:
        print("K: {0}, T: {1} succeed".format(test_case[0], test_case[1]))


