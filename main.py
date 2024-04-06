from heap_snapshot_parser import ParserInterface

with open("test.heapsnapshot", "r") as file:
    str_with_contents = file.read()

print(str_with_contents)
parser = ParserInterface(str_with_contents)
parser.create_graph()
res = parser.query(["asin", "price"])
print(res)
