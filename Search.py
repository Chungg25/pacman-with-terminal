from Node import Node
from Heuristic import Heuristic
class SearchStrategy:

    def cost_sort(self, n):
        return n[0]

    def sort_cost(self, frontier):
        return sorted(frontier, key=self.cost_sort)

    def heap_push(self, cost_and_successor, frontier):
        cost, a, successor = cost_and_successor
        frontier.append((cost, a, successor))
        frontier = self.sort_cost(frontier)
        return frontier

    def check_frontier(self, frontier, successor):
        for i in frontier:
            cost, action, node = i
            if node.get_initial_state() == successor.get_initial_state():
                return False
        return True

    def remove(self, goal_node, goal_state):
        for i in goal_node:
            if i == goal_state:
                goal_node.remove(i)
                break
        return goal_node

    def is_goal(self, goal_state, current_state):
        if current_state.get_initial_state() in goal_state:
            return True
        return False
