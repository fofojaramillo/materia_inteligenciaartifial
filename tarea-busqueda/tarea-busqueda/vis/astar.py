from search import SearchAlgorithm
from pq import PriorityQueue
import math

class AStar(SearchAlgorithm):
    def __init__(self, problem):
        super().__init__(problem)
        self.frontier = PriorityQueue()
        self.backrefs = {}
        self.frontier.update(self.startState, 0.0)

    def stateCost(self, state):
        return self.pastCosts.get(state, None)

    def path(self, state):
        path = []
        while state != self.problem.startState():
            _, prevState = self.backrefs[state]
            path.append(state)
            state = prevState
        path.reverse()
        return path
    
    def heuristic(self, state):
        return (math.sqrt((state[0] -self.problem.endState()[0])**2 +(state[1]-self.problem.endState()[1])**2))
    
    def step(self):
        problem = self.problem
        startState = self.startState
        frontier = self.frontier
        backrefs = self.backrefs

        if self.actions:
            return self.path(problem.endState())

        state, pastCost = frontier.removeMin()
        if state is None and pastCost is None:
            return []
                
        self.pastCosts[state] = pastCost
        path = self.path(state)

        if problem.isEnd(state):
            self.actions = []
            while state != startState:
                action, prevState = backrefs[state]
                self.actions.append(action)
                state = prevState
            self.actions.reverse()
            self.pathCost = pastCost
            return path
        
        for action, newState, cost in problem.successorsAndCosts(state):
            if frontier.update(newState, pastCost + cost + self.heuristic(newState)):
                backrefs[newState] = (action, state)

        return path