/**
 * @file ArgsParser.h
 * @brief Header file for command line argument parsing.
 *
 * This file defines the structure and function for parsing command-line arguments.
 */

 #ifndef ARGSPARSER_H
 #define ARGSPARSER_H
 
 #include <iostream>
 #include <string>
 #include <optional>
 
 /**
  * @brief Structure to hold the parsed program arguments.
  *
  * This structure contains the parsed command-line arguments, such as the input filename.
  */
 struct ProgramArgs {
     /**
      * @brief The input filename.
      *
      * Default value is "input.yaml".
      */
     std::string inputFile = "input.yaml";
 
     /// @todo Add other optional parameters here.
 };
 
 /**
  * @brief Function declaration for parsing command-line arguments.
  *
  * This function parses the command-line arguments and returns a ProgramArgs structure.
  *
  * @param argc The number of command-line arguments.
  * @param argv An array of command-line argument strings.
  * @return A ProgramArgs structure containing the parsed arguments.
  */
 ProgramArgs parseArgs(int argc, char *argv[]);
 
 #endif // ARGSPARSER_H