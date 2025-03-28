#include "YamlParser.h"
#include <fstream>

// Constructor: loads the YAML file
YamlParser::YamlParser(const std::string& filename) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        throw YamlParser::YamlParseException("Could not open file: " + filename);
    }
    try {
        config = YAML::Load(file);
    } catch (const YAML::ParserException& e) {
        throw YamlParser::YamlParseException("YAML parsing error: " + std::string(e.what()));
    }
}

// Retrieves a string value by key
std::string YamlParser::getString(const std::string& key) const {
    if (config[key] && config[key].IsScalar()) {
        return config[key].as<std::string>();
    }
    throw KeyNotFoundException("Key not found or not a string: " + key);
}

// Retrieves an integer value by key
int YamlParser::getInt(const std::string& key) const {
    if (config[key] && config[key].IsScalar()) {
        return config[key].as<int>();
    }
    throw KeyNotFoundException("Key not found or not an integer: " + key);
}

// Retrieves a double value by key
double YamlParser::getDouble(const std::string& key) const {
    if (config[key] && config[key].IsScalar()) {
        return config[key].as<double>();
    }
    throw KeyNotFoundException("Key not found or not a double: " + key);
}

// Retrieves a boolean value by key
bool YamlParser::getBool(const std::string& key) const {
    if (config[key] && config[key].IsScalar()) {
        return config[key].as<bool>();
    }
    throw KeyNotFoundException("Key not found or not a boolean: " + key);
}

// Retrieves a list of strings by key
std::vector<std::string> YamlParser::getStringList(const std::string& key) const {
    if (config[key] && config[key].IsSequence()) {
        std::vector<std::string> result;
        for (const auto& node : config[key]) {
            if (node.IsScalar()) {
                result.push_back(node.as<std::string>());
            } else {
                throw YamlParseException("List contains non-string elements.");
            }
        }
        return result;
    }
    throw KeyNotFoundException("Key not found or not a list: " + key);
}

// Retrieves a map of strings by key
std::map<std::string, std::string> YamlParser::getStringMap(const std::string& key) const {
    if (config[key] && config[key].IsMap()) {
        std::map<std::string, std::string> result;
        for (const auto& pair : config[key]) {
            if (pair.first.IsScalar() && pair.second.IsScalar()) {
                result[pair.first.as<std::string>()] = pair.second.as<std::string>();
            } else {
                throw YamlParseException("Map contains non-string keys or values.");
            }
        }
        return result;
    }
    throw KeyNotFoundException("Key not found or not a map: " + key);
}

// Retrieves any YAML node by key
YAML::Node YamlParser::getNode(const std::string& key) const {
    if (config[key]) {
        return config[key];
    }
    throw KeyNotFoundException("Key not found: " + key);
}