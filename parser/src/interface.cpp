/*
 * This file contains the interface class between pybind11 and the parser
 *
 *  Pybind11/Python <--- This class ---> Parser
 *
 */
#include <memory>
#include "interface.h"
#include <iostream>


ParserInterface::ParserInterface(std::string to_parse_str) {
    p_parser = std::make_unique<Heap_Snapshot_Parser>(to_parse_str);
    p_parser->copy_file_in_memory();
    this->is_valid = true;
}
ParserInterface::~ParserInterface(){
    p_parser.reset();
    this->is_valid = false;
}

void ParserInterface::shutdown(){
    p_parser.reset(); // call the destructor of the Parser(which will free the memory)
    this->is_valid = false;
}

void ParserInterface::create_graph() {

    if(this->p_parser != nullptr && this->is_valid == true){
        p_parser->create_graph();
    }
}

std::vector<std::unordered_map<std::string, std::string>>

ParserInterface::query_for_properties(std::vector<std::string> input_properties) {
    auto interesting_node_ids = p_parser->find_nodes_with_certain_edge_properties(input_properties);
    std::vector<std::unordered_map<std::string, std::string>> ret_vector; // this contains the results

    for(auto node_id : interesting_node_ids){
        auto res = p_parser->build_object(node_id);
        ret_vector.push_back(res);
    }

    return ret_vector;
}
