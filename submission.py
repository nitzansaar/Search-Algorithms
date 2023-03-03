# Author: Nitzan Saar
import math
from collections import deque
from unittest import TestCase

from HopperState import HopperState
from MarsState import MarsState
from SearchAlgorithms import depth_limited_search, a_star, SLD, iterative_deepening_search, depth_first_search, \
    uniform_cost_search, h1


class TestSearchAlgorithms(TestCase):
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
        start = MarsState('8,8', s.mars_graph)
        print(SLD(start))

    def test_a_star(self):
        print('A*')
        s = MarsState()
        s.read_mars_graph("MarsMap")
        start = MarsState('8,8', s.mars_graph)
        a_star(start, SLD)
        a_star(start, h1)

    def test_uniform_cost_search(self):
        s = MarsState()
        s.read_mars_graph("MarsMap")
        start = MarsState('8,8', s.mars_graph)
        print('uniform cost search')
        uniform_cost_search(start, True)


