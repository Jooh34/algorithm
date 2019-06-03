def solution(nodeinfo):
    indexed_nodeinfo = []
    for i, node in enumerate(nodeinfo):
        indexed_nodeinfo.append([i]+node)

    indexed_nodeinfo = sorted(indexed_nodeinfo, key=lambda x: x[1])
    indexed_nodeinfo = sorted(indexed_nodeinfo, key=lambda x: x[2], reverse=True)

    node_list = []
    for nodeinfo in indexed_nodeinfo:
        node_list.append({
            'index': nodeinfo[0] + 1,
            'x': nodeinfo[1],
            'y': nodeinfo[2],
            'l': None,
            'r': None,
        })


    tree = []
    node_len = len(node_list)
    i = 0
    tree_index = 0

    while i < node_len:
        node = node_list[i]

        if i == 0:
            node['l'] = 0
            node['r'] = 100000
            tree.append(node)
            i += 1
            tree_index += 1
            continue

        parent_index = int((tree_index-1) / 2)
        if tree[parent_index] is None:
            tree.append(None)
            tree_index += 1
            continue

        if tree_index % 2 == 0:
            node['r'] = tree[parent_index]['r']
            node['l'] = tree[parent_index]['x']

        else:
            node['r'] = tree[parent_index]['x']
            node['l'] = tree[parent_index]['l']

        if node['x'] in range(node['l'], node['r']):
            tree.append(node)
            i += 1
            tree_index += 1
        else:
            tree.append(None)
            tree_index += 1

    def dfs(index, tree):
        l = index * 2 + 1
        r = index * 2 + 2

        preorder_list.append(tree[index]['index'])
        if l < len(tree):
            if tree[l] is not None:
                dfs(l, tree)

        if r < len(tree):
            if tree[r] is not None:
                dfs(r, tree)

        postorder_list.append(tree[index]['index'])

    preorder_list = []
    postorder_list = []
    dfs(0, tree)

    answer = [preorder_list, postorder_list]
    return answer


nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))
