#include <pybind11/pybind11.h>
#include "interface.h"
#include <pybind11/stl.h>

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

int add(int i, int j) {
    return i + j;
}

namespace py = pybind11;

PYBIND11_MODULE(heap_snapshot_parser, m) {
    py::class_<ParserInterface>(m, "ParserInterface")
            .def(py::init<std::string &>()) // constructor
            .def("create_graph", &ParserInterface::create_graph)
            .def("query", &ParserInterface::query_for_properties);
}