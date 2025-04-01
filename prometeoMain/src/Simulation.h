#ifndef SIMULATION_H
#define SIMULATION_H

#include <omp.h>
#include <string>
#include <iostream>
#include "YamlParser.h"
#include "RandomGenerator.h"

class Simulation {
    /* @brief Class to run the Monte Carlo simulation for estimating Pi.
       This class handles input parameters and runs the simulation.
    */
    public:
      /* @brief Constructor that initializes the simulation with the input file.
           @param inpFile The path to the input YAML file containing simulation parameters.
        */  
      Simulation(std::string inpFile);
      /* @brief Runs the Monte Carlo simulation to estimate Pi.
           This method performs the actual simulation using the parameters defined in the input file.
           It uses OpenMP for parallel processing to speed up the computation.
        */
      void run(); 
      double getPiEstimate() const;

    private: 
      /* @brief Structure to hold input parameters for the simulation.
         This structure can be extended to include more parameters as needed. 
      */  
      struct InputParameters {
         long long num_samples = 1; // Default number of samples
         // Add other parameters as needed 
      };
      /* @brief Path to the input YAML file.
         This file contains the parameters for the simulation.
      */  
      std::string inputFile;
      /* @brief Instance of the InputParameters structure that holds the input parameters.
         This object is initialized by parsing the YAML file.
      */ 
      InputParameters inputPars; // Input parameters for the simulation
      /*
      @brief Method to parse the input file and initialize the input parameters.
           This method uses the YamlParser class to read the YAML file and populate the inputPars structure.
           It also handles any errors that may occur during parsing.
      */ 
      void parseInputFile();
      double pi_estimate; 
      RandomGenerator randomGenerator; 
};

#endif // SIMULATION_H