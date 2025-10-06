def generate_puzzle_instance(goal_state, depth):
    current_state = goal_state 
    for _ in range(depth):
        successors = get_successors(Node(current_state))

        next_state = random.choice(successors)
        current_state = next_state

    return current_state
