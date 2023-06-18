def swap_nodes(input_list, val1, val2):
    node1 = input_list.head_node
    node2 = input_list.head_node
    # Keeping track of the nodes before our target nodes
    node1_prev = None
    node2_prev = None

    # If both the values are same, there is no point in running the whole function
    if val1 == val2:
        print("Elements are the same - no swap needed")
        return
 
    # Setting the previous nodes
    while node1 is not None:
        if node1.get_value() == val1:
            break
        node1_prev = node1
        node1 = node1.get_next_node()

    while node2 is not None:
        if node2.get_value() == val2:
            break
        node2_prev = node2
        node2 = node2.get_next_node()

    # If the nodes are none than the swapping operation is obviously not possible
    if (node1 is None or node2 is None):
        print("Swap not possible - one or more element is not in the list")
        return
    
    # If the prev node is null, that means it is the first node
    # We assign the second node to the head
    if node1_prev is None:
        input_list.head_node = node2
    else:
        # Otherwise we set the next node for our previous one as the second node
        node1_prev.set_next_node(node2)

    if node2_prev is None:
        input_list.head_node = node1
    else:
        node2_prev.set_next_node(node1)
    
    # We store the nect node of the nodes in a temp variable before swapping them
    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)