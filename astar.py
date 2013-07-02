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

def astar_search(num_proc, data, spark_context):
    def process_prepare(pairs):
        data_bc.value.load_library()
        newNodes = []
        for nodes, old_g in pairs:
            g = data_bc.value.calc_g_delta(nodes) + old_g
            h = data_bc.value.calc_h(nodes)
            newNodes.append(TreeNode(nodes,g,h))

        return newNodes

    data_bc = spark_context.broadcast(data)
    depth = data.residue_num
    heap = [TreeNode([],0,0)]
    ans = []
    ans_value = 1
    
    countExpandedNodes = 0
    totalNumMul = 1
    totalNum = 0
    for i in range(data.residu_num):
        totalNumMul *= data.rotamer_num[i]
        totalNum += totalNumMul 
    
    while heap[0].g < ans_value:
        prepare = []
        # the old vector prepare is divided into several subsets
        subSetSize = 500

        while len(prepare) < num_proc * subSetSize and len(heap) > 0:
            current = heapq.heappop(heap)
            if len(current.nodes) >= depth:
                if current.g < ans_value:
                    ans_value = current.g
                    ans = current.nodes
            else:
                resi = len(current.nodes)
                for rotamer in range(data.rotamer_num[resi]):
                    prepare.append((current.nodes + [rotamer], current.g))
        countExpandedNodes += len(prepare)
                
        if num_proc <= 1:
            data.load_library()
            for nodes,old_g in prepare:
                g = data.calc_g_delta(nodes) + old_g
                h = data.calc_h(nodes)
                heapq.heappush(heap, TreeNode(nodes,g,h))
        else:
            # regroup the vector prepare
            prepareNew = []
            temp = []
            counter = 0
            for nodes, old_g in prepare:
                temp.append((nodes, old_g))
                counter += 1
                if counter == subSetSize:
                    prepareNew.append(temp)
                    temp = []
                    counter = 0

            if temp:
                prepareNew.append(temp)

            prepare_p = spark_context.parallelize(prepareNew)
            groupOfNodes = prepare_p.map(process_prepare).collect()
            for nodes in groupOfNodes:
                for node in nodes:
                    heapq.heappush(heap, node)
    
    print "The number of counted nodes: " + countExpandedNodes
    print "The total number of nodes" + totalNum
    return ans
