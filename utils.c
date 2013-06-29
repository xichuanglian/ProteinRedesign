#include <stdio.h>
#include <stdlib.h>
#include "utils.h"

dataset_s read_libs(const char* rlib_name, const char* elib_name)
{
    //dataset_s data = malloc(sizeof(dataset_s));
    dataset_s data;
    data.residue_num = read_rotamer_lib(rlib_name, &(data.rotamer_num));
    data.energy = read_energy_lib(elib_name, data.rotamer_num);
    return data;
}

int read_rotamer_lib(const char* file_name, int** rotamer_num_p)
{
    printf("read rotamer lib begin\n");
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
    printf("read rotamer lib end\n");
    return n;
}

void* read_energy_lib(const char* file_name, const int* rotamer_num)
{
    printf("read energy lib begin\n");
    FILE* file = fopen(file_name, "r");

    int resi_num;
    fscanf(file, "%d", &resi_num);
    float** energy = malloc(resi_num * resi_num * sizeof(float*));

    int i,j;
    for (i = 0; i < resi_num; ++i)
        for (j = 0; j < resi_num; ++j)
            energy[i * resi_num + j] = malloc(rotamer_num[i] * rotamer_num[j] * FLOAT_SIZE);

    int a,b;
    while (fscanf(file,"%d %d",&a,&b) != EOF) {
        float* et = energy[a*resi_num + b];
        int m = rotamer_num[a] * rotamer_num[b];
        for (i = 0; i < m; ++i)
            fscanf(file,"%f",&et[i]);
    }

    fclose(file);
    printf("read energy lib end\n");
    return (void*) energy;
}

int get_rotamer_num(const int* rotamer_num, const int idx)
{
    return rotamer_num[idx];
}

float find_min_rotamer(const int* rotamers_above, const int d, const int j,
                       const int residue_num, const int* rotamer_num,
                       const int* offset, const float* energy)
{
    //printf("find min rotamer begin\n");

    // j starts from 0! 

    float minSum = 1000000000;

    int i,k,s;

    for (s = 0; s < rotamer_num[j]; s++)
    {
        float sum = 0;

        // 1st term in the min()
        for (i = 0; i < d; i++)
        {
            int r = rotamers_above[i];
            //sum += energy[i * data->residue_num + j][r * data->rotamer_num[j] + s];
            int os = offset[i * residue_num + j];
            sum += energy[os + r * rotamer_num[j] + s];
        }

        // 2nd term in the min()
        for (k = j; k < residue_num; k++)
        {
            int u;
            float minSubSum = 1000000000;
            for (u = 0; u < rotamer_num[k]; u++)
            {
                //float energyJK = energy[j * data->residue_num + k][s * data->rotamer_num[k] + u];
                int os = offset[j * residue_num + k];
                float energyJK = energy[os + s * rotamer_num[k] + u];

                if (energyJK < minSubSum)
                    minSubSum = energyJK;
            }

            sum += minSubSum;
        }


        if (sum < minSum)
            minSum = sum;
    }

    //printf("find min rotamer end\n");
    return minSum;
}

float calc_g_delta(const int* rotamers_above, const int d,
                   const int residue_num, const int* rotamer_num,
                   const int* offset, const float* energy)
{
    // d is the length
    float deltaG = 0;

    int newRot = rotamers_above[d-1];
    int k;
    for (k = 0; k < d-1; k++)
    {
        int theOtherRot = rotamers_above[k];
        //deltaG += energy[k * data->residue_num + (d-1)][theOtherRot * data->rotamer_num[d-1] + newRot];
        int os = offset[k * residue_num + (d-1)];
        deltaG += energy[os + theOtherRot * rotamer_num[d-1] + newRot];
    }

    return deltaG;
}

float calc_h(const int* rotamers_above, const int d,
             const int residue_num, const int* rotamer_num,
             const int* offset, const float* energy)
{
    // d is the length
    // j starts from 0!

    float valueH = 0;
    int j;

    for (j = d; j < residue_num; j++)
    {
        valueH += find_min_rotamer(rotamers_above, d, j,
                                   residue_num, rotamer_num,
                                   offset, energy);
    }

    return valueH;
}

float calc_energy(const int* rotamers, const int residue_num, const int* rotamer_num,
                  const int* offset, const float* energy)
{
    float sum = 0;
    for (int i = 0; i < residue_num - 1; ++i)
        for (int j = i + 1; j < residue_num; ++j)
            sum += energy[offset[i * residue_num + j] + rotamers[i] * rotamer_num[i] + rotamers[j]];
    return sum;
}
