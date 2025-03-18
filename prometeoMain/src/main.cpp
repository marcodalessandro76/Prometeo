#include "Simulation.h"
#include <iostream>
#include <omp.h>

using namespace std;

int main() {
    long long num_samples = 100000000; 

    cout << "Calculating π using Monte Carlo with " << num_samples << " samples..." << endl;

    double start_time = omp_get_wtime(); 
    Simulation sim(num_samples);
    sim.run();
    double end_time = omp_get_wtime(); 
    
    cout << "Estimated π: " << sim.getPiEstimate() << endl;
    cout << "Execution time: " << (end_time - start_time) << " seconds" << endl;

    return 0;
}
