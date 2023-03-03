
import math
from collections import deque

from Graph import Node
from MarsState import MarsState
from VacuumState import VacuumState
from RomaniaState import *
from HopperState import *

from queue import PriorityQueue

s = MarsState()
s.read_mars_graph("MarsMap")
goal = MarsState('1,1', s.mars_graph)
def breadth_first_search(startState, use_closed_list=True) :
    search_queue = deque()
    closed_list = {}

    search_queue.append(startState)
    if use_closed_list :
        closed_list[startState] = True
    while len(search_queue) > 0 :
        next_state = search_queue.popleft()
        if next_state.is_goal() :
            print("Goal found")
            next_state.print_solution()
            return
        else :
            successors = next_state.successors()
            if use_closed_list :
                successors = [item for item in successors
                                    if item not in closed_list]
                for s in successors :
                    closed_list[s] = True
            search_queue.extend(successors)



def depth_first_search(startState, use_closed_list=True) :
    search_queue = deque()
    closed_list = {}
    current = 0
    search_queue.append(startState)
    while len(search_queue) > 0:
        next_state = search_queue.pop()
        if next_state.is_goal():
            print("Goal found")
            next_state.print_solution()
            return True
        else:
            successors = next_state.successors()
            current = current + 1
            if use_closed_list:
                successors = [item for item in successors
                              if item not in closed_list]
                for s in successors:
                    closed_list[s] = True

            search_queue.extend(successors)
    return False

# DFS except it only adds nodes to the queue if the cost < limit
def depth_limited_search(startState, use_closed_list=True, limit=12) :
    search_queue = deque()
    closed_list = {}
    current = 0
    search_queue.append(startState)
    while len(search_queue) > 0:
        next_state = search_queue.pop()
        if next_state.is_goal():
            print("Goal found")
            next_state.print_solution()
            return True
        elif next_state.cost < limit: #only add nodes if cost < limit
            successors = next_state.successors()
            current = current + 1
            if use_closed_list:
                successors = [item for item in successors
                              if item not in closed_list]
                for s in successors:
                    closed_list[s] = True
            search_queue.extend(successors)
    return False

## loop that calls DLS with increasing limits until the solution is found.
# good if you want completeness and linear memory
def iterative_deepening_search(startState):
    limit = 1
    goalFound = False
    while not goalFound:
        goalFound = depth_limited_search(startState, True, limit)
        limit += 1
    # print(limit)
    return goalFound

# ***how to use the heuristic func as parameter***
def a_star(startState, heuristic_func):
    search_queue = PriorityQueue()
    visited_list = {}
    search_queue.put((0, startState))
    while not search_queue.empty():
        cost, current_state = search_queue.get()
        if current_state.is_goal():
            current_state.print_solution()
            print("Goal found")
            return
        else:
            successors = current_state.successors()
            # filters out successors that have already been visited
            successors = [item for item in successors
                            if item not in visited_list]
            for s in successors:
                    visited_list[s] = True
            for s in successors:
                # h_cost = heuristic_func(s.location)
                # search_queue.put((cost + h_cost, s))
                search_queue.put((cost + SLD(current_state.location), s))

## simulate uniform cost
def uniform_cost_search(startState, use_visited_list=True):
    search_queue = PriorityQueue()
    visited_list = {}
    search_queue.put((0, startState))
    if use_visited_list:
        visited_list[startState] = True
    while not search_queue.empty():
        cost, next_state = search_queue.get()
        if next_state.is_goal():
            print("Goal found")
            next_state.print_solution()
            return
        else:
            successors = next_state.successors()
            if use_visited_list:
                successors = [item for item in successors
                              if item not in visited_list]
                for s in successors:
                    visited_list[s] = True
            for s in successors:
                search_queue.put((cost + s.cost, s))


def h1(s) :
    return 0

## implement this for the Mars rover.
def SLD(self) :
    y1, x1 = map(int, self.split(","))
    y2, x2 = map(int, goal.location.split(","))
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


## SLD to Bucharest
def RomaniaSLD(s) :
    slds = {'Arad':366, 'Bucharest':0,'Craiova':166,'Dobreta':242,
    'Eforie':161, 'Fagaras':176, 'Giurgiu':77, 'Hirsova':151,
    'Iasi':226, 'Lugoj':244, 'Mehadia':241, 'Neamt':234, 'Oradea':380,
    'Pitesti':100, 'Rimnicu Vilcea':193, 'Sibiu':253, 'Timisoara':329,
    'Urziceni':80, 'Vaslui':199, 'Zerind':374}
    return slds[s.location]



if __name__ == "__main__" :
    #start = VacuumState('left',False,False)
    # g = make_romania_graph()
    # start = RomaniaState('Arad',g)
    # iterative_deepening_search(start)
    start = HopperState(0,0,0)
    # breadth_first_search(start, True)
    # depth_first_search(start, True)
    # depth_limited_search(start, True)
    # iterative_deepening_search(start)
    uniform_cost_search(start, True)
    # start = MarsState('8,8', s.mars_graph)
    # a_star(start,SLD(start.location))

