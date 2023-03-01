from collections import deque
from unittest import TestCase

from HopperState import HopperState


class Test(TestCase):
    def test_depth_first_search(self):
        use_closed_list = True
        startState = HopperState(0,0,0)
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
