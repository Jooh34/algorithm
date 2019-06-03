import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, index, x, y, l, r):
        self._index = index
        self._x = x
        self._y = y
        self._l = l
        self._r = r
        self._left = None
        self._right = None

def solution(nodeinfo):
    indexed_nodeinfo = []
    for i, node in enumerate(nodeinfo):
        indexed_nodeinfo.append([i]+node)

    indexed_nodeinfo = sorted(indexed_nodeinfo, key=lambda x: x[1])
    indexed_nodeinfo = sorted(indexed_nodeinfo, key=lambda x: x[2], reverse=True)

    same_y = []
    last_y = indexed_nodeinfo[0][2]
    level_list = []
    for nodeinfo in indexed_nodeinfo:
        if last_y == nodeinfo[2]:
            same_y.append(Node(nodeinfo[0] + 1, nodeinfo[1], nodeinfo[2], None, None))

        else:
            level_list.append(same_y)
            same_y = []
            same_y.append(Node(nodeinfo[0] + 1, nodeinfo[1], nodeinfo[2], None, None))
            last_y = nodeinfo[2]

    level_list.append(same_y)
    # root_node
    root_node = level_list[0][0]
    root_node._l = 0
    root_node._r = 100000

    level_len = len(level_list)
    for level in range(0, level_len-1):
        parent_list = level_list[level]
        child_list = level_list[level+1]
        p_index = 0
        c_index = 0
        while True:

            if child_list[c_index]._x in range(parent_list[p_index]._l+1, parent_list[p_index]._x):
                child_list[c_index]._l = parent_list[p_index]._l
                child_list[c_index]._r = parent_list[p_index]._x
                parent_list[p_index]._left = child_list[c_index]
                c_index += 1
                if c_index >= len(child_list):
                    break

            if child_list[c_index]._x in range(parent_list[p_index]._x+1, parent_list[p_index]._r):
                child_list[c_index]._l = parent_list[p_index]._x
                child_list[c_index]._r = parent_list[p_index]._r
                parent_list[p_index]._right = child_list[c_index]
                c_index += 1
                if c_index >= len(child_list):
                    break

            p_index += 1
            if p_index >= len(parent_list):
                break

    preorder_list = []
    postorder_list = []
    def dfs(current):
        preorder_list.append(current._index)
        if current._left:
            dfs(current._left)

        if current._right:
            dfs(current._right)
        postorder_list.append(current._index)

    dfs(root_node)
    answer = [preorder_list, postorder_list]
    return answer


nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))
