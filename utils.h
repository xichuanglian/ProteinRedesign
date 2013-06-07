#include <stdio.h>
#include <stdlib.h>

#define INT_SIZE 4
#define FLOAT_SIZE 4

int read_rotamer_lib(const char* file_name, int** rotamer_num);
void* read_energy_lib(const char* file_name,
                      const int resi_num, const int* rotamer_num);
