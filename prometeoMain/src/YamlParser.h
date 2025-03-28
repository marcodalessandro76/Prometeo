#ifndef YAML_PARSER_H
#define YAML_PARSER_H

#include <string>
#include <stdexcept>
#include <vector>
#include <map>
#include <yaml-cpp/yaml.h>

class YamlParser {
public:
    // Constructor: loads the YAML file
    explicit YamlParser(const std::string& filename);

    // Methods to retrieve scalar values
    std::string getString(const std::string& key) const;
    int getInt(const std::string& key) const;
    double getDouble(const std::string& key) const;
    bool getBool(const std::string& key) const;

    // Methods to retrieve lists and maps
    std::vector<std::string> getStringList(const std::string& key) const;
    std::map<std::string, std::string> getStringMap(const std::string& key) const;

    // Generic method to retrieve any YAML node
    YAML::Node getNode(const std::string& key) const;

    // Custom exception classes
    class YamlParseException : public std::runtime_error {
    public:
        YamlParseException(const std::string& message) : std::runtime_error(message) {}
    };

    class KeyNotFoundException : public std::runtime_error {
    public:
        KeyNotFoundException(const std::string& message) : std::runtime_error(message) {}
    };

private:
    YAML::Node config;
};

#endif // YAML_PARSER_H