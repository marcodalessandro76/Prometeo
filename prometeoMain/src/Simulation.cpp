#include "Simulation.h"
#include <iostream>
#include <random>
#include <omp.h>

// Constructor
Simulation::Simulation(long long samples) : num_samples(samples), pi_estimate(0.0) {}

// Method to run the simulation
void Simulation::run() {
    long long count_inside = 0;

    #pragma omp parallel
    {
        // Each thread gets a unique random number generator with a different seed
        std::random_device rd;
        std::mt19937 generator(rd() ^ omp_get_thread_num());
        std::uniform_real_distribution<double> distribution(0.0, 1.0);

        long long local_count = 0;

        // Distribute iterations among threads
        #pragma omp for
        for (long long i = 0; i < num_samples; i++) {
            double x = distribution(generator);
            double y = distribution(generator);

            // Check if the point (x, y) is inside the unit circle
            if (x * x + y * y <= 1.0) {
                local_count++;
            }
        }

        // Use atomic operation to safely add results from each thread
        #pragma omp atomic
        count_inside += local_count;
    }

    // Compute the estimated value of π
    pi_estimate = 4.0 * count_inside / num_samples;
}

// Method to retrieve the estimated value of π
double Simulation::getPiEstimate() const {
    return pi_estimate;
}
