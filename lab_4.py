import itertools
from networkx import DiGraph
from networkx.algorithms import find_cycle
from networkx.exception import NetworkXNoCycle


COSTS = {
    'C1': 1,
    'C2': 2,
    'C3': 3,
    'C4': 4,
    'C5': 5,
    'C6': 1,
    'C7': 2,
}

BLOCKS = [
    ('C1', 'C2'),
    ('C2', 'C3'),
    ('C3', 'C4'),
    ('C4', 'C5'),
    ('C5', 'C6'),
    ('C6', 'C1'),
    ('C3', 'C7'),
    ('C4', 'C7'),
    ('C7', 'C6'),
]


def resolve(edges, order):

    graph = DiGraph()
    graph.add_edges_from(edges)

    removed = []
    for node in order:

        try:
            find_cycle(graph)
            graph.remove_node(node)
            removed.append(node)
        except NetworkXNoCycle:
            break

    return [*graph.node, *removed], sum(COSTS[key] for key in removed)


if __name__ == '__main__':

    steps, steps_cost = resolve(BLOCKS, sorted(COSTS, key=lambda k: COSTS[k]))
    print('\n\nПошаговый алгоритм: {};\nСтоимость отката: {}'.format(steps, steps_cost))

    variants = [(resolve(BLOCKS, variant)) for variant in itertools.permutations(COSTS)]
    optimal, optimal_cost = min(variants, key=lambda result: result[1])
    print('\n\nОптимальный алгоритм: {};\nСтоимость отката: {}'.format(optimal, optimal_cost))
