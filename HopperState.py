from State import State

hopper1max = 8
hopper2max = 5
hopper3max = 3

class HopperState(State) :
    counter = 0

    def __init__(self, h1=0,h2=0,h3=0, prev_state=None, prev_action=None):
        State.__init__(self)
        HopperState.counter=HopperState.counter + 1
        self.hopper1 = h1
        self.hopper2 = h2
        self.hopper3 = h3
        self.prev_state = prev_state
        self.prev_action = prev_action
        if prev_state :
            self.cost = prev_state.cost + 1
        else :
            self.cost = 0

## you do this.
    def __eq__(self,other):
        return self.cost == other.cost

## you do this
    def __lt__(self, other):
        return self.cost < other.cost

## you do this
    def __hash__(self):
        return hash(self.__repr__())

    def __repr__(self):
        return "(hopper1 %i hopper2 %i hopper3 %i)" % \
               (self.hopper1, self.hopper2, self.hopper3)

    def is_goal(self):
        return self.hopper1 == 4 and \
               self.hopper2 == 4 and\
               self.hopper3 == 0

    def print_solution(self):
        ptr = self
        print(ptr)
        while ptr :
            print(ptr.prev_action)
            print(ptr.prev_state)
            ptr = ptr.prev_state
        print("Number of states: %i" % HopperState.counter)

    ## you do this.
    def successors(self):
        ## actions are: dump out hopper 1
        ## dump out hopper 2
        ## dump out hopper 3
        ## fill hopper 1
        ## fill hopper 2
        ## fill hopper 3
        ## pour from 1 to 2
        ## pour from 1 to 2
        ## pour from 2 to 1
        ## pour from 2 to 3
        ## pour from 3 to 1
        ## pour from 3 to 2
        pass
