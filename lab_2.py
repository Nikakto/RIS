import itertools
import numpy as np

COST_BASE = 3
COST_SERV = np.array([1, 3, 2])


def cross_db_query(cost_base, cost_serv):

    INDEX = list(range(1, len(cost_serv)+1, 1))
    MASK = np.array(INDEX)
    VARIANTS = list(itertools.product(INDEX, repeat=2))

    print('\nВарианты (источник, координатор):\n', VARIANTS)
    results = [(np.ma.array(cost_serv, mask=MASK == driver).sum() + (source != driver) * cost_base, source, driver)
               for source, driver in VARIANTS]

    matrix = np.array([row[0] for row in results]).reshape(len(cost_serv), len(cost_serv))
    print('\nМатрица. Строка - источник; Столбец - координатор:\n', matrix)
    print('\nОптимально (ОПД, источник, координатор):\n', sorted(results, key=lambda el: el[0])[0])

    return results


if __name__ == '__main__':
    cross_db_query(COST_BASE, COST_SERV)
