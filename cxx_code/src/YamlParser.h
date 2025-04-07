/**
 * @file YamlParser.h
 * @brief Header file for the YamlParser class, which provides methods for parsing YAML files.
 */

 #ifndef YAML_PARSER_H
 #define YAML_PARSER_H
 
 #include <string>
 #include <stdexcept>
 #include <vector>
 #include <map>
 #include <yaml-cpp/yaml.h>
 
 /**
  * @class YamlParser
  * @brief A class to parse YAML configuration files.
  *
  * This class provides a convenient interface to load and retrieve data from YAML files.
  * It supports retrieving scalar values, lists, and maps, and provides custom exception
  * classes for error handling.
  */
 class YamlParser {
 public:
     /**
      * @brief Constructor. Loads the YAML file specified by the filename.
      *
      * @param filename The path to the YAML file.
      * @throws YamlParseException If the file cannot be loaded or parsed.
      */
     explicit YamlParser(const std::string& filename);
 
     /**
      * @brief Retrieves a string value from the YAML node.
      *
      * @param key The key to look up in the YAML node.
      * @return The string value associated with the key.
      * @throws KeyNotFoundException If the key is not found.
      * @throws YamlParseException If the value is not a string.
      */
     std::string getString(const std::string& key) const;
 
     /**
      * @brief Retrieves an integer value from the YAML node.
      *
      * @param key The key to look up in the YAML node.
      * @return The integer value associated with the key.
      * @throws KeyNotFoundException If the key is not found.
      * @throws YamlParseException If the value is not an integer.
      */
     int getInt(const std::string& key) const;
 
     /**
      * @brief Retrieves a double value from the YAML node.
      *
      * @param key The key to look up in the YAML node.
      * @return The double value associated with the key.
      * @throws KeyNotFoundException If the key is not found.
      * @throws YamlParseException If the value is not a double.
      */
     double getDouble(const std::string& key) const;
 
     /**
      * @brief Retrieves a boolean value from the YAML node.
      *
      * @param key The key to look up in the YAML node.
      * @return The boolean value associated with the key.
      * @throws KeyNotFoundException If the key is not found.
      * @throws YamlParseException If the value is not a boolean.
      */
     bool getBool(const std::string& key) const;
 
     /**
      * @brief Retrieves a list of strings from the YAML node.
      *
      * @param key The key to look up in the YAML node.
      * @return A vector of strings.
      * @throws KeyNotFoundException If the key is not found.
      * @throws YamlParseException If the value is not a list of strings.
      */
     std::vector<std::string> getStringList(const std::string& key) const;
 
     /**
      * @brief Retrieves a map of string keys to string values from the YAML node.
      *
      * @param key The key to look up in the YAML node.
      * @return A map of strings to strings.
      * @throws KeyNotFoundException If the key is not found.
      * @throws YamlParseException If the value is not a map of strings to strings.
      */
     std::map<std::string, std::string> getStringMap(const std::string& key) const;
 
     /**
      * @brief Retrieves a raw YAML node from the configuration.
      *
      * This method allows direct access to the YAML node for more complex parsing.
      *
      * @param key The key to retrieve the node from.
      * @return The YAML node associated with the key.
      * @throws KeyNotFoundException If the key is not found.
      */
     YAML::Node getNode(const std::string& key) const;
 
     /**
      * @class YamlParseException
      * @brief Exception class for YAML parsing errors.
      */
     class YamlParseException : public std::runtime_error {
     public:
         /**
          * @brief Constructor.
          *
          * @param message The error message.
          */
         YamlParseException(const std::string& message) : std::runtime_error(message) {}
     };
 
     /**
      * @class KeyNotFoundException
      * @brief Exception class for when a key is not found in the YAML node.
      */
     class KeyNotFoundException : public std::runtime_error {
     public:
         /**
          * @brief Constructor.
          *
          * @param message The error message.
          */
         KeyNotFoundException(const std::string& message) : std::runtime_error(message) {}
     };
 
 private:
     /**
      * @brief The parsed YAML configuration.
      */
     YAML::Node config;
 };
 
 #endif // YAML_PARSER_H
