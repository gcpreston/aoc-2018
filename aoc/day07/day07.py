import re
from data.graphs import DirectedGraph


def main():
    p = re.compile(r'Step (\S) must be finished before step (\S) can begin.')
    with open('input.txt') as file:
        edges = []
        for line in file.readlines():
            m = p.match(line.strip())
            edges.append((m.group(1), m.group(2)))

    print('Part 1:', part1(edges))


def part1(edges):
    g = DirectedGraph()
    added = set()

    for u, v in edges:
        if u not in added:
            g.add_node(u)
            added.add(u)
        if v not in added:
            g.add_node(v)
            added.add(v)

        g.add_edge(u, v)

    return ''.join(g.topological_sort())


def part2():
    pass


if __name__ == '__main__':
    main()
