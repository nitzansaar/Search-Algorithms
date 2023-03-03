import math
from collections import deque
from unittest import TestCase

from HopperState import HopperState
from MarsState import MarsState
from SearchAlgorithms import depth_limited_search, a_star, SLD, iterative_deepening_search, depth_first_search, \
    uniform_cost_search


class Test(TestCase):
    def test_depth_first_search(self):
        print('depth first search')
        startState = HopperState(0, 0, 0)
        depth_first_search(startState)

    def test_depth_limited_search(self):
        print('depth limited search')
        startState = HopperState(0, 0, 0)
        depth_limited_search(startState)
    def test_iterative_deepening_search(self):
        print('iterative deepening search')
        startState = HopperState(0, 0, 0)
        iterative_deepening_search(startState)

    def test_sld(self):
        print('SLD heuristic')
        s = MarsState()
        s.read_mars_graph("MarsMap")
        s2 = '3,3'
        sld = SLD(s2)
        print(sld)

    def test_a_star(self):
        print('A*')
        s = MarsState()
        s.read_mars_graph("MarsMap")
        start = MarsState('8,8', s.mars_graph)
        a_star(start,SLD(start.location))

    def test_uniform_cost_search(self):
        startState = HopperState(0, 0, 0)
        print('uniform cost search')
        uniform_cost_search(startState, True)

class TestHopperState(TestCase):
    def test_eq(self):
        state0 = HopperState(h1=1, h2=2, h3=3, prev_state=None, prev_action=None)
        state1 = HopperState(h1=1, h2=2, h3=3, prev_state=None, prev_action=None)
        # print(state1.cost)
        state2 = HopperState(h1=2, h2=2, h3=1, prev_state=state1, prev_action="hop")
        # print(state2.cost)
        state3 = HopperState(h1=1, h2=2, h3=3, prev_state=state2, prev_action="hop")
        # print(state3.cost)
        assert state1 == state0
        assert state2 != state3
        assert state2 == state2


    def test_lt(self):
        state1 = HopperState(h1=1, h2=2, h3=3, prev_state=None, prev_action=None)
        state2 = HopperState(h1=1, h2=2, h3=2, prev_state=state1, prev_action="Jump")
        state3 = HopperState(h1=1, h2=2, h3=3, prev_state=state2, prev_action="hop")
        assert state1 < state2
        assert state2 < state3
        assert not state3 < state3

    def test_hash(self):
        state1 = HopperState(h1=1, h2=2, h3=3, prev_state=None, prev_action=None)
        state2 = HopperState(h1=1, h2=2, h3=3, prev_state=None, prev_action=None)
        state3 = HopperState(h1=6, h2=2, h3=3, prev_state=state2, prev_action="hop")
        assert hash(state3) == hash(state3)
        assert hash(state1) != hash(state3)
        assert hash(state1) == hash(state2)
    def test_successors(self):
        initial_state = HopperState(h1=1, h2=2, h3=0)
        successors = initial_state.successors()
        for successor in successors:
            print(successor.prev_action)
            print(successor.prev_state)
            print(successor)