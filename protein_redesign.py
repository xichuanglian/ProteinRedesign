from dataset import Dataset
import astar
import sys
import time

from pyspark import SparkContext

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print >> sys.stderr, \
                "Usage: ProteinRedesign <master> <cores>"
        exit(-1)
    files = ["dataset.py","astar.py","utils.so"]
    sc = SparkContext(sys.argv[1], "Protein Redesign", pyFiles=files)
    data = Dataset("rotamerLibrary", "energyTable")
    start = time.time()
    result = astar.astar_search(int(sys.argv[2]),data,sc)
    elapsed = time.time()-start
    print result
    print elapsed
