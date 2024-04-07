#ifndef HEAP_SNAPSHOT_PARSER_INTERFACE_H
#define HEAP_SNAPSHOT_PARSER_INTERFACE_H
#include "Heap_Snapshot_Parser.h"



class ParserInterface{
public:
    ParserInterface(std::string to_parse_str);
    ~ParserInterface();

    void create_graph();
    std::vector<std::unordered_map<std::string, std::string>> query_for_properties(std::vector<std::string>);
    void shutdown();
private:
    std::unique_ptr<Heap_Snapshot_Parser> p_parser;
    bool is_valid;
};


#endif //HEAP_SNAPSHOT_PARSER_INTERFACE_H
