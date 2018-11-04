import itertools
import numpy as np

from lab_2 import cross_db_query

COST_BASE = 0
COST_CROSS_DB = 5
COST_CROSS_DB_PARTS = [2, 3, 2]
COST_SIMPLE = [1, 3, 2]

COST_CROSS_DB_MIN_MATRIX = np.split(np.array(cross_db_query(cost_base=COST_CROSS_DB, cost_serv=COST_CROSS_DB_PARTS)), 3)
COST_CROSS_DB_MIN_COST, *_, COST_CROSS_DB_MIN_DRIVER = \
    zip(*[sorted(row, key=lambda el: el[0])[0] for row in COST_CROSS_DB_MIN_MATRIX])

INDEX = list(range(1, len(COST_SIMPLE) + 1, 1))
MASK = np.array(INDEX)
VARIANTS = list(itertools.product(INDEX, repeat=2))

results = np.array([
    {
        'cost': np.ma.array(COST_SIMPLE, mask=MASK == driver).sum() + COST_CROSS_DB_MIN_COST[source-1] + (source != driver) * COST_BASE,
        'source': source,
        'driver': driver,
        'cross_db_driver': COST_CROSS_DB_MIN_DRIVER[source-1]
    } for source, driver in VARIANTS
]).reshape(3, 3)

print('\nМатрица. Строка - источник; Столбец - координатор:\n',
      np.array([[result['cost'] for result in row] for row in results]))

optimals = [min(row, key=lambda el: el['cost']) for row in results]
for optimal in optimals:
    print('''
        Источник: {source};
        Коордиантор: {driver};
        Координатор распределенного запроса {cross_db_driver}
        Общая стоимость: {cost}
    '''.format(**optimal))
