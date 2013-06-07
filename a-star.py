class TreeNode:
    def __init__(self,nodes,g,h):
        self.nodes = nodes
        self.g = g
        self.h = h

def calc_g(nodes_above, rotamer, old_g):
    pass

def calc_h(nodes_above):
    pass

def astar_search(residue_num):
    depth = residue_num
    heap = []
    current = TreeNode([],0,0)
    while len(current.nodes) < depth:
        resi = len(current.nodes)
        for rotamer in rotamers[resi]:
            g = calc_g(current.nodes, rotamer, current.g)
            new_nodes = current.nodes + [rotamer]
            h = calc_h(new_nodes)
            heap.push(TreeNode(new_nodes,g,h))
        current = heap.pop()
    return current.nodes
