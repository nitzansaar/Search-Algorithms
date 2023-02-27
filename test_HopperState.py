from unittest import TestCase

from HopperState import HopperState


class TestHopperState(TestCase):
    def test_eq(self):
        state0 = HopperState(h1=1, h2=2, h3=3, prev_state=None, prev_action=None)
        state1 = HopperState(h1=1, h2=2, h3=3, prev_state=None, prev_action=None)
        # print(state1.cost)
        state2 = HopperState(h1=1, h2=2, h3=3, prev_state=state1, prev_action="hop")
        # print(state2.cost)
        state3 = HopperState(h1=1, h2=2, h3=3, prev_state=state2, prev_action="hop")
        # print(state3.cost)
        assert state1 == state0
        assert not state3 == state1

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

