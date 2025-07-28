import numpy as np
from Weighted_method import weighted_method
def topsis_method(matrix, weights, criteria):
    result = np.sum(matrix ** 2, axis=0)
    normalization = np.sqrt(result)
    matrix = matrix / normalization

    weighted_matrix = matrix * weights


    adjusted_matrix = weighted_matrix * criteria
    ideal_decision = np.max(adjusted_matrix, axis=0) * criteria
    worst_decision = np.min(adjusted_matrix, axis=0) * criteria

    dist_to_ideal = np.linalg.norm(weighted_matrix - ideal_decision, axis=1)
    dist_to_worst = np.linalg.norm(weighted_matrix - worst_decision, axis=1)

    closeness = dist_to_worst / (dist_to_ideal + dist_to_worst)

    return closeness

criteria = np.array([1, 1, 1, 1, -1])

brands = ["Nissan Qashqai", "Audi A5", "BMW F10", "Mazda CX-5", "Hyundai IX 35"]

matrix = np.array([
    #Vision | Interior | Comfort | Power | Price
    [8, 8, 8, 6, 8],
    [9, 9, 9, 8, 6],
    [9, 8, 8, 9, 5],
    [7, 8, 8, 7, 7],
    [8, 7, 8, 6, 8]
])

weights = weighted_method(matrix, 0.0001)
scores = topsis_method(matrix, weights, criteria)

sorted = sorted(dict(zip(brands, scores)).items(), key=lambda kvpt: kvpt[1], reverse=True)

for key, value in sorted:
    print(f"{key}: {value:.4f}")

print(f"Best choice: {sorted[0][0]}")