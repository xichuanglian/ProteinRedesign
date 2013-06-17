from dataset import Dataset
import astar
import sys

# from pyspark import SparkContext

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print >> sys.stderr, \
                "Usage: ProteinRedesign <master>"
        exit(-1)
    files = ["dataset.py","astar.py","utils.so"]
    # sc = SparkContext(sys.argv[1], "Protein Redesign", pyFiles=files)
    data = Dataset("rotamerLibrary", "energyTable")
    result = astar.astar_search(1,data)
    print result
