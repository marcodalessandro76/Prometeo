#include "Simulation.h"

using namespace std;

Simulation::Simulation(string inpFile) : randomGenerator(), inputFile(inpFile), pi_estimate(0.0) {
    cout << "Input filename to be used: " << inputFile << endl;
    parseInputFile(); // Initialize inputPars member variable 
}

void Simulation::parseInputFile() {

    try {
        YamlParser parser(inputFile); // Load the configuration from the YAML file
        inputPars.num_samples = parser.getInt("num_samples"); // Get the number of samples from the YAML file
        // You can add more parameters here as needed
    } catch (const YamlParser::KeyNotFoundException& e) {
        // key not found in the YAML file
        std::cerr << "Error: " << e.what() << std::endl;
    } catch (const YamlParser::YamlParseException& e) {
        // parsing error in the YAML file 
        std::cerr << "Error YAML: " << e.what() << std::endl;
    }
}

void Simulation::run() {
    long long count_inside = 0;

    cout << "Calculating pi using Monte Carlo with " << inputPars.num_samples << " samples..." << endl;
    cout << "Number of threads in Simulation: " << omp_get_max_threads() << endl;

    #pragma omp parallel
    {
        long long local_count = 0;

        #pragma omp for
        for (long long i = 0; i < inputPars.num_samples; i++) {
            double x = randomGenerator.getRandomNumber();
            double y = randomGenerator.getRandomNumber();

            if (x * x + y * y <= 1.0) {
                local_count++;
            }
        }

        #pragma omp atomic
        count_inside += local_count;
    }

    pi_estimate = 4.0 * count_inside / inputPars.num_samples;
}

double Simulation::getPiEstimate() const {
    return pi_estimate;
}