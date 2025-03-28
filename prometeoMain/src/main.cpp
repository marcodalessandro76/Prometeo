#include "Simulation.h"
#include <iostream>
#include "YamlParser.h"

using namespace std;

int main() {
    try {
        // Crea un'istanza di YamlParser, passando il nome del file YAML
        YamlParser parser("test1.yaml");

        // Ottieni il valore intero associato alla chiave "età"
        int iteration = parser.getInt("iteration");

        // Stampa il valore intero
        std::cout << "iteration: " << iteration << std::endl;
    
    } catch (const YamlParser::KeyNotFoundException& e) {
        // Gestisci l'eccezione se la chiave non viene trovata
        std::cerr << "Errore: " << e.what() << std::endl;
    } catch (const YamlParser::YamlParseException& e) {
        // Gestisci l'eccezione se si verifica un errore durante il parsing del file YAML
        std::cerr << "Errore YAML: " << e.what() << std::endl;
    }

    long long num_samples = 100000000; 

    cout << "Calculating π using Monte Carlo with " << num_samples << " samples..." << endl;

    double start_time = omp_get_wtime(); 
    Simulation sim(num_samples);
    sim.run();
    double end_time = omp_get_wtime(); 
    
    cout << "Estimated π: " << sim.getPiEstimate() << endl;
    cout << "Execution time: " << (end_time - start_time) << " seconds" << endl;

    return 0;
}
