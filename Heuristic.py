class Heuristic:
    def minEuclideanDistance(state, goal_state) -> float:
        return min(((state.get_initial_state()[0] - goal_pos[0]) ** 2 + (state.get_initial_state()[1] - goal_pos[1]) ** 2) ** 0.5 for goal_pos in goal_state)
    
    
    def distanceOfTwoFood(state, goal_state):
        def manhattanDistance(state, goal_state):
            return abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1])
        pos = state.initial_state
        max_distance = 0
        first = goal_state[0]
        second = goal_state[0]
        for i in range(len(goal_state)):
            for j in range(i + 1, len(goal_state)):
                dist = manhattanDistance(goal_state[i], goal_state[j])
                if dist > max_distance:
                    max_distance = dist
                    first = goal_state[i]
                    second = goal_state[j]
        return max_distance + min( (manhattanDistance(pos, first), manhattanDistance(pos, second)) )
    