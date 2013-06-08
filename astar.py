import "heapq"
import "dataset"

class TreeNode:
    def __init__(self,nodes,g,h):
        self.nodes = nodes
        self.g = g
        self.h = h
    def __lt__(self,other):
        return (self.g + self.h) < (other.g + other.h)

def astar_search(num_proc, data):
    depth = data.residue_num()
    heap = [TreeNode([],0,0)]
    finished = False
    ans = []
    while not finished:
        prepare = []
        while len(prepare) < num_proc and len(heap > 0):
            current = heappop(heap)
            if len(current.nodes) >= depth:
                finished = True
                ans = current.nodes
                break
            else:
                resi = len(current.nodes)
                for rotamer in range(data.rotamer_num(resi)):
                    prepare.append((current.nodes + [rotamer], current.g))
        if not finished:
            for nodes,old_g in prepare:
                g = data.calc_g_delta(nodes, old_g) + old_g
                h = data.calc_h(nodes)
                heappush(heap, TreeNode(nodes,g,h))
    return ans
