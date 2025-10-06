def backtrack_path(goal_node):
    path = [] 
    current_node = goal_node

    while current_node is not None:
        path.insert(0, current_node.state) 
        current_node = current_node.parent 

    return path