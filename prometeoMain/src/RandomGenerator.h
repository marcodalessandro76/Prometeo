#ifndef RANDOMGENERATOR_H
#define RANDOMGENERATOR_H

#include <random>
#include <vector>
#include <omp.h>
#include <iostream>

class RandomGenerator {
public:
    RandomGenerator();
    double getRandomNumber();

private:
    std::vector<std::mt19937> generators;
    std::vector<std::uniform_real_distribution<double>> distributions;
};

#endif // RANDOMGENERATOR_H