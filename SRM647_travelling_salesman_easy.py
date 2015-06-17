__author__ = 'Tiger'

import queue

q = queue.PriorityQueue()
q.put((-10, 10))
q.put((-5, 5))
q.put((-1, 1))

a, b = 1