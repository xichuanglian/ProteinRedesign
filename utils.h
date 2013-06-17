#include <stdio.h>
#include <stdlib.h>

#define INT_SIZE 4
#define FLOAT_SIZE 4

typedef struct dataset_S{
    int residue_num;
    int* rotamer_num;
    void* energy;
} dataset_s;

dataset_s read_libs(const char* rlib_name, const char* elib_name);

int read_rotamer_lib(const char* file_name, int** rotamer_num);
void* read_energy_lib(const char* file_name, const int* rotamer_num);
int get_rotamer_num(const int* rotamer_num, const int idx);
/*
 * d starts from 1
 * j starts from 0
 */
float find_min_rotamer(const int* rotamers_above, const int d, const int j, const void* data);
/*
 * calc \sum_{i=0}^{d-1} energy[i_r][d_s]
 */
float calc_g_delta(const int* rotamers_above, const int d, const void* data);
float calc_h(const int* rotamers_above, const int d, const void* data);
