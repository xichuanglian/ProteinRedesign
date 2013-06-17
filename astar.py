import heapq

class TreeNode:
    def __init__(self,nodes,g,h):
        self.nodes = nodes
        self.g = g
        self.h = h
    def __lt__(self,other):
        return (self.g + self.h) < (other.g + other.h)
    def __str__(self):
        return str(self.nodes) + "g:%d h: %d" %(self.g, self.h)

def astar_search(num_proc, data):
    depth = data.residue_num
    heap = [TreeNode([],0,0)]
    ans = []
    ans_value = 1
    while heap[0].g < ans_value:
        prepare = []
        while len(prepare) < num_proc and len(heap) > 0:
            current = heapq.heappop(heap)
            if len(current.nodes) >= depth:
                if current.g < ans_value:
                    ans_value = current.g
                    ans = current.nodes
            else:
                resi = len(current.nodes)
                for rotamer in range(data.rotamer_num(resi)):
                    prepare.append((current.nodes + [rotamer], current.g))
        for nodes,old_g in prepare:
            g = data.calc_g_delta(nodes) + old_g
            h = data.calc_h(nodes)
            heapq.heappush(heap, TreeNode(nodes,g,h))
    return ans
