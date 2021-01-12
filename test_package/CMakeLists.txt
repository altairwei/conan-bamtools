cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

find_package(bamtools REQUIRED)

add_executable(example example.cpp)
target_include_directories(example PRIVATE ${bamtools_INCLUDES})
target_link_libraries(example ${bamtools_LIBRARIES})

add_custom_command(
 TARGET example POST_BUILD
 COMMAND ${CMAKE_COMMAND} -E create_symlink "${CMAKE_SOURCE_DIR}/sam_file_1.bam" "${CMAKE_CURRENT_BINARY_DIR}/sam_file_1.bam" 
)

add_custom_command(
 TARGET example POST_BUILD
 COMMAND ${CMAKE_COMMAND} -E create_symlink "${CMAKE_SOURCE_DIR}/sam_file_2.bam" "${CMAKE_CURRENT_BINARY_DIR}/sam_file_2.bam" 
)
