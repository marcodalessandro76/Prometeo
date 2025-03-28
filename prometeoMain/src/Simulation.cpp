#include "Simulation.h"

Simulation::Simulation(long long samples) : randomGenerator() {
    num_samples = samples;
    pi_estimate = 0.0;
    std::cout << "Number of threads in Simulation: " << omp_get_max_threads() << std::endl;

}

void Simulation::run() {
    long long count_inside = 0;

    #pragma omp parallel
    {
        long long local_count = 0;

        #pragma omp for
        for (long long i = 0; i < num_samples; i++) {
            double x = randomGenerator.getRandomNumber();
            double y = randomGenerator.getRandomNumber();

            if (x * x + y * y <= 1.0) {
                local_count++;
            }
        }

        #pragma omp atomic
        count_inside += local_count;
    }

    pi_estimate = 4.0 * count_inside / num_samples;
}

double Simulation::getPiEstimate() const {
    return pi_estimate;
}