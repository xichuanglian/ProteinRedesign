from ctypes import *

class Dataset:
    def __init__(self, rlib_name, elib_name):
        self.lib = cdll.LoadLibrary("./example.so")
        self.rotamer_num = c_int_p
        self.residue_num = lib.read_rotamer_lib(c_char_p(rlib_name), byref(rotamer_num))
        self.energy = lib.read_energy_lib(c_char_p(rlib_name), self.residue_num, self.rotamer_num)
