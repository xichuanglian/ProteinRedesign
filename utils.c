#include <stdio.h>
#include <stdlib.h>
#include "utils.h"

int read_rotamer_lib(const char* file_name, int** rotamer_num_p)
{
    FILE* file = fopen(file_name, "r");

    // read the number of residues
    int n;
    fscanf(file, "%d", &n);

    // read the numbers of rotamers
    *rotamer_num_p = malloc(n * INT_SIZE);
    int *rn = *rotamer_num_p;
    int i;
    for (i = 0; i < n; ++i)
        fscanf(file, "%d", &rn[i]);

    fclose(file);
    return n;
}

void* read_energy_lib(const char* file_name,
                      const resi_num, const int* rotamer_num)
{
    FILE* file = fopen(file_name, "r");
    float** energy = malloc(resi_num * sizeof(float*));

    int i;
    for (i = 0; i < resi_num; ++i)
        energy[i] = malloc(rotamer_num[i] * FLOAT_SIZE);

    int a,b;
    while (fscanf(file,"%d %d",&a,&b)) {
        float* et = eneray[a*n + b];
        int m = rotamer_num[a] * rotamer_num[b];
        for (i = 0; i < m; ++i)
            fscanf(file,"%f",&et[i]);
    }

    fclose(file);
    return (void*) energy;
}

int get_rotamer_num(const int* rotamer_num, const idx)
{
    return rotamer_num;
}
