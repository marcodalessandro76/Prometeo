#include "ArgsParser.h"
#include <iostream>
#include <string>

// Function definition for parsing command-line arguments
ProgramArgs parseArgs(int argc, char *argv[]) {
    using namespace std;
    ProgramArgs args; // Initialize with the default value

    for (int i = 1; i < argc; ++i) {
        string arg = argv[i];

        if (arg == "-inp" || arg == "--input") {
            // Check if the next argument is provided
            if (i + 1 < argc) {
                args.inputFile = argv[i + 1];
                i++;
            } else {
                cerr << "Warning: specified -inp but no filename provided." << endl;
            }
        }
        // Add argument parsing for other options here (e.g., -out output_filename)
        else if (arg == "-h" || arg == "--help") {
            cout << "Usage: mpntecarlo_pi.exe [-inp| --input input_filename] [-h|--help]" << endl;
            exit(0);
        }
        else if (arg.rfind("-", 0) == 0) {
            cerr << "Warning: unrecognized option: " << arg << endl;
        }
    }

    return args;
}