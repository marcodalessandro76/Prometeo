/**
 * @file RandomGenerator.h
 * @brief Header file for the RandomGenerator class, which provides thread-safe random number generation.
 */

 #ifndef RANDOMGENERATOR_H
 #define RANDOMGENERATOR_H
 
 #include <random>
 #include <vector>
 #include <omp.h>
 #include <iostream>
 
 /**
  * @class RandomGenerator
  * @brief A class for generating thread-safe random numbers in the range [0.0, 1.0).
  *
  * This class utilizes OpenMP to determine the number of available threads and
  * initializes a separate Mersenne Twister pseudo-random number generator and a
  * uniform real distribution for each thread. This approach avoids contention
  * and ensures better performance when generating random numbers in parallel
  * regions.
  */
 class RandomGenerator {
 public:
     /**
      * @brief Constructor.
      *
      * Initializes the random number generators and uniform real distributions
      * for each thread available at the time of construction. The number of
      * threads is determined using `omp_get_max_threads()`. Each thread gets its
      * own independent generator and distribution.
      */
     RandomGenerator();
 
     /**
      * @brief Gets a random number in the range [0.0, 1.0).
      *
      * This function retrieves the thread-local random number generator and
      * distribution for the calling thread and generates a random double value
      * within the specified range.
      *
      * @return A random double number in the interval [0.0, 1.0).
      */
     double getRandomNumber();
 
 private:
     /**
      * @brief Vector to hold the Mersenne Twister pseudo-random number generators for each thread.
      *
      * The size of this vector is determined by the maximum number of OpenMP threads.
      * Each element stores a unique random number generator instance for a specific thread.
      */
     std::vector<std::mt19937> generators;
 
     /**
      * @brief Vector to hold the uniform real distributions for each thread.
      *
      * Each element corresponds to a random number generator in the `generators` vector
      * and defines a uniform distribution over the range [0.0, 1.0) for that specific thread.
      */
     std::vector<std::uniform_real_distribution<double>> distributions;
 };
 
 #endif // RANDOMGENERATOR_H
