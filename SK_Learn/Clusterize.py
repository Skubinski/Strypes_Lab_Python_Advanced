import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import adjusted_rand_score
import matplotlib.pyplot as plt



column_names = ['Площ', 'Периметър', 'Компактност', 'Дължина',
                'Ширина', 'Коефициент на асиметричност', 'Дължина на улея', 'Клас']

np.random.seed(0)
df = pd.DataFrame(np.random.rand(270, 8), columns=column_names)
df['Клас'] = np.repeat([1, 2, 3], 90)

X = df.drop('Клас', axis=1)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=0)
clusters = kmeans.fit_predict(X_scaled)

true_labels = df['Клас']
ari = adjusted_rand_score(true_labels, clusters)
print(f"Adjusted Rand Index (ARI): {ari:.2f}")

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters, cmap='viridis', s=50)
plt.title("K-Means Clustering of Wheat Grains")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.show()
