#ifndef SIMULATION_H
#define SIMULATION_H

#include <omp.h>
#include "RandomGenerator.h"

class Simulation {
public:
    Simulation(long long samples);
    void run();
    double getPiEstimate() const;

private:
    long long num_samples;
    double pi_estimate;
    RandomGenerator randomGenerator; 
};

#endif // SIMULATION_H