#include "RandomGenerator.h"

RandomGenerator::RandomGenerator() {
    int num_threads = omp_get_max_threads();
    generators.resize(num_threads);
    distributions.resize(num_threads);

    for (int i = 0; i < num_threads; ++i) {
        generators[i].seed(std::random_device{}() ^ i);
        distributions[i] = std::uniform_real_distribution<double>(0.0, 1.0);
    }
}

double RandomGenerator::getRandomNumber() {
    int thread_id = omp_get_thread_num();
    return distributions[thread_id](generators[thread_id]);
}