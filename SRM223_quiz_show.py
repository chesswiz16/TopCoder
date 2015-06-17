__author__ = 'Tiger'

def quiz_show(scores, wager_1, wager_2):
    """

    :rtype : int
    """
    my_score = scores[0]
    score_1 = scores[1]
    score_2 = scores[2]
    bet = 0
    best = 0
    for wager in range(0, my_score + 1):
        wins = 0
        for i_am_right in [-1, 1]:
            for one_is_right in [-1, 1]:
                for two_is_right in [-1, 1]:
                    my_modified_score = my_score + (i_am_right * wager)
                    if (my_modified_score > score_1 + one_is_right * wager_1 and
                                my_modified_score > score_2 + two_is_right * wager_2):
                        wins += 1
        if wins > best:
            bet = wager
            best = wins
    return bet


print(quiz_show([100, 100, 100], 25, 75))
print(quiz_show([10, 50, 60], 30, 41))
print(quiz_show([10, 50, 60], 31, 41))
print(quiz_show([2, 2, 12], 0, 10))
print(quiz_show([10000, 10000, 10000], 9998, 9997))
print(quiz_show([5824, 4952, 6230], 364, 287))


