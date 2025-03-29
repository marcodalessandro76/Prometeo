#ifndef SIMULATION_H
#define SIMULATION_H

#include <omp.h>
#include <string>
#include <iostream>
#include "YamlParser.h"
#include "RandomGenerator.h"

class Simulation {
public:
    Simulation(std::string inpFile);
    void run();
    double getPiEstimate() const;

private:
    struct InputParameters {
        long long num_samples = 1; // Default number of samples
        // Add other parameters as needed 
    };
    std::string inputFile;
    InputParameters inputPars; // Input parameters for the simulation
    void parseInputFile(); // Function to parse input parameters from the YAML file
    double pi_estimate;
    RandomGenerator randomGenerator; 
};

#endif // SIMULATION_H