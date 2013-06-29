from ctypes import *

class Dataset:
    def __init__(self, rlib_name, elib_name):
        #self.lib = cdll.LoadLibrary("./utils.so")
        #self.lib.calc_g_delta.restype = c_float
        #self.lib.calc_h.restype = c_float

        # read the number of rotamers for each residue
        rlib_file = open(rlib_name)
        self.residue_num = int(rlib_file.readline())
        self.rotamer_num = [int(x) for x in rlib_file.readline().split()]
        assert self.residue_num == len(self.rotamer_num)
        rlib_file.close()
        print self.rotamer_num

        # build the offset list
        self.offset = [-1] * (self.residue_num ** 2)
        s = 0

        # read the energy table
        elib_file = open(elib_name)
        self.energy = []
        assert int(elib_file.readline()) == self.residue_num
        for line in elib_file:
            ls = line.split()
            a = int(ls[0])
            b = int(ls[1])
            nums = [float(x) for x in ls[2:]]
            assert len(nums) == self.rotamer_num[a] * self.rotamer_num[b]
            self.energy.extend(nums)
            self.offset[a * self.residue_num + b] = s
            s += len(nums)
        elib_file.close()

        #self.rotamer_num_c = (c_int * self.residue_num)(*self.rotamer_num)
        #self.offset_c = (c_int * len(self.offset))(*self.offset)
        #self.energy_c = (c_float * len(self.energy))(*self.energy)

    def load_library(self):
        self.lib = cdll.LoadLibrary("./utils.so")
        self.lib.calc_g_delta.restype = c_float
        self.lib.calc_h.restype = c_float
        self.lib.calc_energy.restype = c_float
        self.rotamer_num_c = (c_int * self.residue_num)(*self.rotamer_num)
        self.offset_c = (c_int * len(self.offset))(*self.offset)
        self.energy_c = (c_float * len(self.energy))(*self.energy)

    def calc_g_delta(self, nodes):
        nodes_c = (c_int * len(nodes))(*nodes)
        return self.lib.calc_g_delta(byref(nodes_c), len(nodes), self.residue_num,
                                     byref(self.rotamer_num_c), byref(self.offset_c), byref(self.energy_c))

    def calc_h(self, nodes):
        nodes_c = (c_int * len(nodes))(*nodes)
        return self.lib.calc_h(byref(nodes_c), len(nodes), self.residue_num,
                               byref(self.rotamer_num_c), byref(self.offset_c), byref(self.energy_c))

    def calc_energy(self, nodes):
        nodes_c = (c_int * len(nodes))(*nodes)
        return self.lib.calc_energy(byref(nodes_c), self.residue_num,
                                    byref(self.rotamer_num_c), byref(self.offset_c), byref(self.energy_c))
