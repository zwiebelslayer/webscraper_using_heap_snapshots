cmake_minimum_required(VERSION 3.4...3.18)
project(heap_snapshot_parser)



add_subdirectory(lib/heap_snapshot_parser_cpp_impl)
include_directories(lib/heap_snapshot_parser_cpp_impl/include)
include_directories(include)

add_subdirectory(pybind11)
pybind11_add_module(heap_snapshot_parser src/bindings.cpp src/interface.cpp)

target_link_libraries(heap_snapshot_parser PRIVATE heap_snapshot_parser_cpp_impl)