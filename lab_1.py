import itertools
import numpy as np

DATA = [1, 3, 4]
INTENSITY = [       # row is server, column is intensity
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

COSTS = np.array(INTENSITY) * DATA

INDEX = list(range(1, len(DATA)+1, 1))
MASK = np.array([[i] * len(DATA) for i in INDEX])
VARIANTS = list(itertools.product(INDEX, repeat=len(DATA)))

print('\nРазмещения на серверах (Т1, Т2, Т3):\n', VARIANTS)
results = ((np.ma.array(COSTS, mask=MASK == variant).sum(), variant) for variant in VARIANTS)
print('\nОптимально (ОПД, (Т1, Т2, Т3)):\n', sorted(results, key=lambda el: el[0])[0])
