from search import SearchAlgorithm

class DynamicProgramming(SearchAlgorithm):
    def __init__(self, problem):
        super().__init__(problem)
        self.backrefs = {}
        self.fCosts = {}
        self.futureQueue = [problem.endState()]
        self.currentState = problem.startState()
        self.startState = problem.startState()
        self.finish = False

    def futureCosts(self):
        def exploredCosts(self):
            if len(self.futureQueue) == 0:
                return
            state = self.futureQueue.pop(0)
            if self.problem.isEnd(state):
                self.fCosts[state] = 0
                for _, previousState, _ in self.problem.successorsAndCosts(state):
                    self.futureQueue.append(previousState)
            if state not in self.fCosts:
                alreadyVisited = []
                for _, nextState, nextCost in self.problem.successorsAndCosts(state):
                    if nextState in self.fCosts:
                        alreadyVisited.append((nextState, nextCost))
                    else:
                        self.futureQueue.append(nextState)
                self.fCosts[state] = min(nextCost + self.fCosts[nextState] for nextState, nextCost in alreadyVisited) 
            return self.fCosts[state]
        exploredCosts(self)

    def stateCost(self, state):
        return self.fCosts.get(state, None)
    
    def path(self, state):
        path = []
        while state != self.problem.startState():
            _, prevState = self.backrefs[state]
            path.append(state)
            state = prevState
        path.reverse()
        return path

    def step(self):
        if self.finish == True:
            return self.path(self.currentState)
        
        problem = self.problem
        backrefs = self.backrefs
        state = self.currentState
        path = self.path(state)

        if problem.isEnd(state):
            self.finish = True
            return path
        if state not in self.fCosts:
            for _ in range(len(self.futureQueue)):
                self.futureCosts()
            return path
        nextState = state
        bestAction = None

        for action, neighbor, _ in problem.successorsAndCosts(state):
            if self.fCosts[neighbor] < self.fCosts[nextState]:
                nextState = neighbor
                bestAction = action
        backrefs[nextState] = (bestAction, state)
        self.currentState = nextState
        return path