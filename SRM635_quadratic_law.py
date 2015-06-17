__author__ = 'Tiger'


def BinarySearch(lo, hi, f):
    # f(lo) is true
    # f(hi) is false
    # returns the largest x such that f(x) is true
    while lo + 1 < hi:
        ha = (lo + hi) / 2
        if f(ha):
            lo = ha
        else:
            hi = ha
    return lo

class QuadraticLaw:
    def getTime(self, d):
        return BinarySearch(0, d + 1, lambda x: d - x - x*x >= 0 )

check = QuadraticLaw()
print(check.getTime(5))

