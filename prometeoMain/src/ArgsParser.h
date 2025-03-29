#ifndef ARGSPARSER_H
#define ARGSPARSER_H

#include <iostream>
#include <string>
#include <optional>

// Structure to hold the parsed program arguments
struct ProgramArgs {
    std::string inputFile = "input.yaml"; // Default input filename
    // You can add other optional parameters here
};

// Function declaration for parsing command-line arguments
ProgramArgs parseArgs(int argc, char *argv[]);

#endif // ARGSPARSER_H