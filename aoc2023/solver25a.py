from networkx import Graph, minimum_cut


def solve(data_in: str):
    graph = Graph()
    for line in data_in.splitlines():
        left, right_raw = line.split(": ")
        for right in right_raw.split(" "):
            graph.add_edge(left, right, capacity=1.0)
    nodes = list(graph.nodes)
    partitions = [], []
    for b in nodes[1:]:
        cut_value, partitions = minimum_cut(graph, nodes[0], b)
        if cut_value > 3:
            continue
        break
    return len(partitions[0]) * len(partitions[1])
