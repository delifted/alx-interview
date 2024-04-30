#!/usr/bin/python3
'''
Lockboxes
'''
def canUnlockAll(boxes):
    '''
    Function definition
    '''
    if not boxes:
        return False

    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True  # Mark the first box as visited

    queue = [0]  # Start BFS traversal from the first box

    # Perform BFS traversal
    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if 0 <= key < num_boxes and not visited[key]:
                visited[key] = True
                queue.append(key)

    # Check if all boxes have been visited
    return all(visited)
