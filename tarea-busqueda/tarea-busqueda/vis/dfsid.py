from search import SearchAlgorithm

class DepthFirstSearchID(SearchAlgorithm):
    def __init__(self, problem):
        super().__init__(problem)
        self.stack = [(0,[self.startState])]
        self.pastCosts[self.startState] = 0
        self.path = []
        self.cost = 0
        self.finish = False
    def stateCost(self, state):
        return self.pastCosts.get(state, None)
    
    def step(self):
        problem = self.problem

        if self.finish == True:
            return self.path

        if self.stack == []:
            self.stack = [(0,[self.startState])]
            self.cost+=1
        
        pathCost, path= self.stack.pop()
        lastState = path[-1]

        if problem.isEnd(lastState):
            self.finish = True
            self.stack = []
            self.path = path
            return path
        for action, newState, cost in problem.successorsAndCosts(lastState):
            if newState not in path:
                if pathCost + cost <= self.cost:
                    temppath = path.copy()
                    temppath.append(newState)
                    self.stack.append((pathCost+cost, temppath))
                    self.pastCosts[newState] = self.pastCosts[lastState]+cost
        return path