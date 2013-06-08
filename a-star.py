import "heapq"
import "protein_types"

class TreeNode:
    def __init__(self,nodes,g,h):
        self.nodes = nodes
        self.g = g
        self.h = h
    def __lt__(self,other):
        return (self.g + self.h) < (other.g + other.h)

def calc_g(nodes_above, rotamer, old_g, data):
    pass

def calc_h(nodes_above, data):
    pass

def astar_search(residue_num, residues, data):
    depth = residue_num
    heap = []
    current = TreeNode([],0,0)
    while len(current.nodes) < depth:
        resi = len(current.nodes)
        for rotamer in residues[resi].rotamers:
            g = calc_g(current.nodes, rotamer, current.g, data)
            new_nodes = current.nodes + [rotamer]
            h = calc_h(new_nodes, data)
            heappush(heap, TreeNode(new_nodes,g,h))
        current = heappop(heap)
    return current.nodes
