import math
from collections import deque
from unittest import TestCase

from HopperState import HopperState
from SearchAlgorithms import depth_limited_search


class Test(TestCase):
    def test_depth_first_search(self):
        use_closed_list = True
        startState = HopperState(0, 0, 0)
        limit = 20
        search_queue = deque()
        closed_list = {}
        current = 0
        search_queue.append(startState)
        while len(search_queue) > 0:
            next_state = search_queue.pop()
            if next_state.is_goal():
                print("Goal found")
                next_state.print_solution()
                print(closed_list.__sizeof__())
                return
            elif next_state.cost < limit:  # only add nodes if cost < limit
                successors = next_state.successors()
                current = current + 1
                if use_closed_list:
                    successors = [item for item in successors
                                  if item not in closed_list]
                    for s in successors:
                        closed_list[s] = True

                search_queue.extend(successors)


class Test(TestCase):
    def test_iterative_deepening_search(self):
        startState = HopperState(0, 0, 0)
        limit = 1
        goalFound = False
        while not goalFound:
            goalFound = depth_limited_search(startState, True, limit)
            limit += 1
        print("Limit:", limit)
        return goalFound


class Test(TestCase):
    def test_sld(self):
        s1 = '1,1'
        s2 = '3,3'
        x1, y1 = map(int, s1.split(","))
        x2, y2 = map(int, s2.split(","))
        sld = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        print(sld)
