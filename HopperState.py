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

    # return true if states have equal costs, false otherwise
    def __eq__(self,other):
        return self.hopper1 == other.hopper1 and self.hopper2 == other.hopper2 and self.hopper3 == other.hopper3
    # returns true if cost is less than other cost, false otherwise
    def __lt__(self, other):
        return self.cost < other.cost

    # returns unique hash value for hopper state
    def __hash__(self):
        return hash(self.__repr__())

    def __repr__(self):
        return "(hopper1 %i hopper2 %i hopper3 %i)" % \
               (self.hopper1, self.hopper2, self.hopper3)

    # make set goal state method
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
    # maybe try to reduce this and make more concise
    def successors(self):
        successors = []
        ## dump out hopper 1
        if (self.hopper1 > 0):
            successors.append(HopperState(0, self.hopper2, self.hopper3, self, "dump1"))
        ## dump out hopper 2
        if (self.hopper2 > 0):
            successors.append(HopperState(self.hopper1, 0, self.hopper3, self, "dump2"))
        ## dump out hopper 3
        if (self.hopper3 > 0):
            successors.append(HopperState(self.hopper1, self.hopper2, 0, self, "dump3"))
        ## fill hopper 1
        if (self.hopper1 < 8):
            successors.append(HopperState(8, self.hopper2, self.hopper3, self, "fill1"))
        ## fill hopper 2
        if (self.hopper2 < 5):
            successors.append(HopperState(self.hopper1, 5, self.hopper3, self, "fill2"))
        ## fill hopper 3
        if (self.hopper3 < 3):
            successors.append(HopperState(self.hopper1, self.hopper2, 3, self, "fill3"))
        ## pour from 1 to 2
        if (self.hopper1 > 0 and self.hopper2 < 5):
            amount = min(self.hopper1, 5 - self.hopper2)
            successors.append(HopperState(self.hopper1 - amount, self.hopper2 + amount, self.hopper3, self, "pour12"))
        ## pour from 1 to 3
        if (self.hopper1 > 0 and self.hopper2 < 3):
            amount = min(self.hopper1, 3 - self.hopper3)
            successors.append(HopperState(self.hopper1 - amount, self.hopper2, self.hopper3 + amount, self, "pour13"))
        ## pour from 2 to 1
        if (self.hopper1 < 8 and self.hopper2 > 0):
            amount = min(self.hopper2, 8 - self.hopper1)
            successors.append(HopperState(self.hopper1 + amount, self.hopper2 - amount, self.hopper3, self, "pour21"))
        ## pour from 2 to 3
        if (self.hopper2 > 0 and self.hopper3 < 3):
            amount = min(self.hopper2, 3 - self.hopper3)
            successors.append(HopperState(self.hopper1, self.hopper2 - amount, self.hopper3 + amount, self, "pour23"))
        ## pour from 3 to 1
        if (self.hopper1 < 8 and self.hopper3 > 0):
            amount = min(self.hopper3, 8 - self.hopper1)
            successors.append(HopperState(self.hopper1 + amount, self.hopper2, self.hopper3 - amount, self, "pour31"))
        ## pour from 3 to 2
        if (self.hopper2 < 5 and self.hopper3 > 0):
            amount = min(self.hopper3, 5 - self.hopper2)
            successors.append(HopperState(self.hopper1, self.hopper2 + amount, self.hopper3 - amount, self, "pour32"))
        return successors


