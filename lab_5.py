import numpy as np
from matplotlib import pylab

TIMES = 10000
TIMEOUT = np.arange(0.5, 10, 0.5)

queries = np.array([
    np.random.exponential(1, TIMES),
    np.random.exponential(2, TIMES),
    np.random.exponential(1, TIMES),
    np.random.exponential(2, TIMES),
    np.random.gamma(2, 1, TIMES),
]).T

query_times = np.array([
    np.ma.array(np.amax(queries, axis=1), mask=np.amax(queries, axis=1) > timeout, fill_value=timeout).filled().mean()
    for timeout in TIMEOUT
])

print('Оценки среднего времени:')
[print(f'ТС: {timeout}; Среднее время: {mean_time:2.4}') for mean_time, timeout in zip(query_times, TIMEOUT)]

pylab.plot(TIMEOUT, query_times, 'k-', label='среднее время запроса')
pylab.plot(TIMEOUT, TIMEOUT, 'k*', label='ограничение ТС')
pylab.grid()
pylab.xticks(TIMEOUT)
pylab.yticks(np.arange(0, np.ceil(np.amax(TIMEOUT)) + 1, 1))
pylab.xlabel('Время ТС')
pylab.ylabel('Среднее время запроса')
pylab.title('График среднего времени запроса от ограничения ТС')
pylab.legend()
pylab.show()
