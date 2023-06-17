def depth(tree_node):
    if tree_node is None:
        return 0

    left_depth = depth(tree_node.get("left_child"))
    right_depth = depth(tree_node.get("right_child"))

    if left_depth > right_depth:
        return left_depth + 1
    else:
        return right_depth + 1

# Helper function to build trees
def build_bst(my_list):
    if len(my_list) == 0:
        return None

    mid_idx = len(my_list) // 2
    mid_val = my_list[mid_idx]

    tree_node = {"data": mid_val}
    tree_node["left_child"] = build_bst(my_list[:mid_idx])
    tree_node["right_child"] = build_bst(my_list[mid_idx + 1:])

    return tree_node

# Helper variables
tree_level_1 = build_bst([1])
tree_level_2 = build_bst([1, 2, 3])
tree_level_4 = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) 

# Test cases
print(depth(tree_level_1) == 1)
print(depth(tree_level_2) == 2)
print(depth(tree_level_4) == 4)
