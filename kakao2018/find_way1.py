import queue

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

    for level in level_list:
        print(level)

    answer = []
    # length = len(node_list)
    # root_node = node_list[0]
    # root_node._l = 0
    # root_node._r = 100000
    #
    # q = queue.Queue()
    # q.put(root_node)
    #
    # i = 1
    # while q.qsize() > 0 and i < length:
    #     node = q.get()
    #
    #     if node_list[i]._x in range(node._l, node._x):
    #         node_list[i]._l = node._l
    #         node_list[i]._r = node._x
    #         node._left = node_list[i]
    #         q.put(node_list[i])
    #         i += 1
    #
    #     if i >= length:
    #         break
    #
    #     if node_list[i]._x in range(node._x, node._r):
    #         node_list[i]._l = node._x
    #         node_list[i]._r = node._r
    #         node._right = node_list[i]
    #         q.put(node_list[i])
    #         i += 1
    #
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
