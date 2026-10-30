cmake_minimum_required(VERSION 3.20)
project(BharatOpt-X VERSION 0.1.0 LANGUAGES CXX)

# Enforce C++23
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Add subdirectories
add_subdirectory(engine)

# Add Engine Executable
add_executable(bharatopt_engine engine/main.cpp)
target_link_libraries(bharatopt_engine PRIVATE engine_lib)

# Enable testing
enable_testing()
add_subdirectory(tests)
