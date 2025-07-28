import numpy as np
from collections import deque
import time

def weighted_method(matrix, value):
    vectors = deque()
    current_matrix = matrix

    start_time = time.perf_counter()

    converged = False
    while not converged:
        current_matrix = current_matrix @ current_matrix

        vectors.append([i / sum(np.sum(current_matrix, axis=1)) for i in np.sum(current_matrix, axis=1)])

        if len(vectors) == 2:
            result = np.subtract(np.array(vectors[0]), np.array(vectors[1]))

            if np.all(np.abs(result) <= value):
                converged = True
            else:
                vectors.popleft()

    end_time = time.perf_counter()
    print(f"\nElapsed time: {end_time - start_time:.6f} seconds")

    return vectors.pop()


# Input matrix
matrix = np.array([
    [1.0000, 0.50000, 3.0000],
    [2.0000, 1.0000, 4.0000],
    [0.3333, 0.2500, 1.0000]
])

# Print result vector line by line
print(*weighted_method(matrix, 0.0001), sep='\n')
