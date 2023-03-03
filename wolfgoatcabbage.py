from search import *

class WolfGoatCabbage(Problem):
    def __init__(self, initial=set({'F', 'W', 'G', 'C'}), goal=set()):
        super().__init__(initial, goal)

    def goal_test(self, state):
        """returns True if the given state is a goal state"""
        return state == self.goal

    def result(self, state, action):
        """returns the new state reached from the given state
        and the given action. Assume that the action is valid."""

        return state - action

    def actions(self, state):
        """returns a list of valid actions in the given state"""

        def is_restricted(state):
            restrictions = [set({'W', 'G'}), set({'G', 'C'})]
            for restriction in restrictions:
                if restriction.issubset(state):
                    return True
            return False

        actions = []
        # can farmer leave alone?
        bank = state.copy()
        bank = bank - set({'F'})
        if not is_restricted(bank):
            actions.append(set({'F'}))

        # can farmer take one item?
        for item in bank:
           items = bank.copy() - set({item})
           if not is_restricted(items):
               actions.append(set({'F', item}))

        return actions


if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    goal_test = wgc.goal_test(set())
    print('goal_test: ', goal_test)

    result = wgc.result(set({'F', 'W', 'G', 'C'}), set({'F', 'G'}))
    print('new state: ', result)

    actions = wgc.actions(set({'F','G', 'C'}))
    print('actions: ', actions)

    # solution = depth_first_graph_search(wgc).solution()
    # print(solution)
    # solution = breadth_first_graph_search(wgc).solution()
    # print(solution)
