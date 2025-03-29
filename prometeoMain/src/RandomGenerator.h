#ifndef RANDOMGENERATOR_H
#define RANDOMGENERATOR_H

#include <random>
#include <vector>
#include <omp.h>
#include <iostream>

class RandomGenerator {
public:
    // Constructor initializes the random number generators and distributions for each thread
    RandomGenerator();
    // Function to get a random number in the range [0.0, 1.0)
    double getRandomNumber(); 

private:
    // Vectors to hold the random number generators and distributions for each thread
    // The number of threads is determined at runtime using OpenMP  
    // Each thread has its own generator to avoid contention
    std::vector<std::mt19937> generators;
    // Each thread has its own distribution to generate random numbers 
    std::vector<std::uniform_real_distribution<double>> distributions;
};

#endif // RANDOMGENERATOR_H