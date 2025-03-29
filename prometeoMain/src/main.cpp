#include "Simulation.h"
#include <iostream>
#include "ArgsParser.h"

using namespace std;

int main(int argc, char *argv[]) {
    
    ProgramArgs parsedArgs = parseArgs(argc, argv);
    
    double start_time = omp_get_wtime(); 
    Simulation sim(parsedArgs.inputFile);
    sim.run();
    double end_time = omp_get_wtime(); 
    
    cout << "Estimated π: " << sim.getPiEstimate() << endl;
    cout << "Execution time: " << (end_time - start_time) << " seconds" << endl;

    return 0;
}
