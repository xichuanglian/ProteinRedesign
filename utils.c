#include <stdio.h>
#include <stdlib.h>
#include "utils.h"

dataset_s* read_libs(const char* rlib_name, const char* elib_name)
{
    dataset_s* data = malloc(sizeof(dataset_s));
    data->residue_num = read_rotamer_lib(rlib_name, &(data->rotamer_num));
    data->energy = read_energy_lib(elib_name, data->residue_num, data->rotamer_num);
    return data;
}

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
                      const int resi_num, const int* rotamer_num)
{
    FILE* file = fopen(file_name, "r");
    float** energy = malloc(resi_num * sizeof(float*));

    int i;
    for (i = 0; i < resi_num; ++i)
        energy[i] = malloc(rotamer_num[i] * FLOAT_SIZE);

    int a,b;
    while (fscanf(file,"%d %d",&a,&b)) {
        float* et = energy[a*resi_num + b];
        int m = rotamer_num[a] * rotamer_num[b];
        for (i = 0; i < m; ++i)
            fscanf(file,"%f",&et[i]);
    }

    fclose(file);
    return (void*) energy;
}

int get_rotamer_num(const int* rotamer_num, const int idx)
{
    return rotamer_num[idx];
}

float find_min_rotamer(const int* rotamers_above, const int d, const int j, const void* data_v)
{
    dataset_s* data = (dataset_s*) data_v;
    float** energy = (float**)data->energy;

	// j starts from 0!
}

float calc_g_delta(const int* rotamers_above, const int d, const void* data_v)
{
    dataset_s* data = (dataset_s*) data_v;
    float** energy = data->energy;

	// d is the length
	float deltaG = 0;

	int newRot = rotamer_above[d-1];
	for (int k = 0; k < d-1; k++)
	{
		int theOtherRot = rotamers_above[k];
		deltaG += energy[k * data->residue_num + (d-1)][theOtherRot * data->rotamer_num[d-1] + newRot];
	}

	return deltaG;
}

float calc_h(const int* rotamers_above, const int d, const void* data_v)
{
    dataset_s* data = (dataset*) data_v;

	// d is the length
	// j starts from 0!

	float valueH = 0;
	
	for (j = d; j < data->residue_num; j++)
	{
		valueH += find_min_rotamer(rotamers_above, d, j, data_v);
	}

	return valueH;
}
