from ctypes import *

class c_Dataset_s(Structure):
    _fields_ = [("residue_num", c_int),
                ("rotamer_num", POINTER(c_int)),
                ("energy", c_void_p)]

class Dataset:
    def __init__(self, rlib_name, elib_name):
        self.lib = cdll.LoadLibrary("./utils.so")
        self.lib.read_libs.restype = c_Dataset_s
        self.c_data = self.lib.read_libs(c_char_p(rlib_name), c_char_p(elib_name))
        self.residue_num = self.c_data.residue_num

    def rotamer_num(self, resi):
        return self.lib.get_rotamer_num(self.c_data.rotamer_num, resi)

    def calc_g_delta(self, nodes):
        c_nodes_p = (c_int * len(nodes)) (*nodes)
        self.lib.calc_g_delta.restype = c_float
        c_g_delta = self.lib.calc_g_delta(c_nodes_p, len(nodes), byref(self.c_data))
        return c_g_delta

    def calc_h(self, nodes):
        c_nodes_p = (c_int * len(nodes)) (*nodes)
        self.lib.calc_h.restype = c_float
        c_h = self.lib.calc_h(c_nodes_p, len(nodes), byref(self.c_data))
        return c_h
