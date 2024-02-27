cmake_minimum_required(VERSION 3.0)
project(HelloWorld C)

# Check if Clang compiler is available
find_program(CLANG_EXECUTABLE clang)

if(CLANG_EXECUTABLE)
    # Set Clang as the compiler
    set(CMAKE_C_COMPILER "${CLANG_EXECUTABLE}")
    set(CMAKE_CXX_COMPILER "${CLANG_EXECUTABLE}")
else()
    message(FATAL_ERROR "Clang compiler not found. Please install Clang.")
endif()

# Add the 'src' directory to include directories
include_directories(src)

# Define the source files
set(SOURCES src/hello.c)

# Create the executable
add_executable(hello ${SOURCES})
