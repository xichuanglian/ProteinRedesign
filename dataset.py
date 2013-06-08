from ctypes import *

class c_Dataset_s(Structure):
    _fields_ = [("residue_num", c_int),
                ("rotamer_num", POINTER(c_int)),
                ("energy", c_void_p)]

class Dataset:
    def __init__(self, rlib_name, elib_name):
        self.lib = cdll.LoadLibrary("./example.so")
        self.c_data = self.lib.read_libs(c_char_p(rlib_name), c_char_p(elib_name))
        self.residue_num = self.c_data.residue_num

    def rotamer_num(self, resi):
        return self.lib.get_rotamer_num(self.c_data.rotamer_num, resi).value

    def calc_g_delta(self, nodes):
        c_nodes_p = (c_int * len(nodes)) (*nodes)
        c_g_delta = self.lib.calc_g_delta(c_nodes_p, len(nodes), self.c_data)
        return c_g_delta.value

    def calc_h(self, nodes):
        c_nodes_p = (c_int * len(nodes)) (*nodes)
        c_h = lib.calc_h(c_nodes_p, len(nodes), self.c_residue_num, self.c_data)
        return c_h.value
