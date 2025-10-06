def graph_search_agent(start_state, goal_state):

    frontier = priority_queue()  
    explored_set = set() 
    nodes_explored = 0  
    start_node = Node(start_state, g=0, h=heuristic(start_state, goal_state))
    frontier.push(start_node)

    while frontier is not empty:
        node = frontier.pop()
        nodes_explored += 1

        if node.state == goal_state:
            return backtrack_path(node) 

        explored_set.add(node.state)

        for successor_state in get_successors(node):
            if successor_state not in explored_set:
                g = node.g + 1
                h = heuristic(successor_state, goal_state)
                successor_node = Node(successor_state, parent=node, g=g, h=h)

                
                frontier.push(successor_node)

    return None 