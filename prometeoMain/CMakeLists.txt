cmake_minimum_required(VERSION 3.10)
project(montecarlo_pi)

# Set the C++ standard version
set(CMAKE_CXX_STANDARD 17)

# Specify the source files directory
set(SRC_DIR ${CMAKE_SOURCE_DIR}/src)

# Automatically add all source files
file(GLOB SOURCES "${SRC_DIR}/*.cpp")

# Specify the folder where the executable should be placed
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin)

# Set the output directory for both Debug and Release configurations
foreach(OUTPUTCONFIG ${CMAKE_CONFIGURATION_TYPES})
    string(TOUPPER ${OUTPUTCONFIG} OUTPUTCONFIG_U)
    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_${OUTPUTCONFIG_U} ${CMAKE_SOURCE_DIR}/bin)
endforeach()

# Create the executable
add_executable(montecarlo_pi ${SOURCES})

# Enable OpenMP
find_package(OpenMP REQUIRED)
if(OpenMP_CXX_FOUND)
    target_compile_options(montecarlo_pi PRIVATE ${OpenMP_CXX_FLAGS})
    target_link_libraries(montecarlo_pi PRIVATE ${OpenMP_CXX_LIBRARIES})
endif()

# Enable Yaml-cpp
find_package(yaml-cpp REQUIRED)
include_directories(${yaml-cpp_INCLUDE_DIRS})
target_link_libraries(montecarlo_pi PRIVATE yaml-cpp::yaml-cpp)