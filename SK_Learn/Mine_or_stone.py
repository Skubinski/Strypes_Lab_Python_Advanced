import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

def get_mlp():
    return make_pipeline(StandardScaler(), MLPClassifier(max_iter=2000))

def get_dtc():
    return DecisionTreeClassifier()

def get_rfc():
    return RandomForestClassifier()

def evaluate_classifier(x, y, classifier_fn):
    model = classifier_fn()
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)

    model.fit(x_train, y_train)
    prediction = model.predict(x_test)

    count_true = np.sum(prediction == y_test)
    count_false = np.sum(prediction != y_test)

    return count_true, count_false

def calculate(arr, steps, y, classifier_fn):
    accuracy_count = []
    for i in steps:
        np.random.shuffle(arr)
        x = arr[:, :i].astype(float)
        count_true, count_false = evaluate_classifier(x, y, classifier_fn)
        accuracy = (count_true / (count_true + count_false)) * 100
        accuracy_count.append(accuracy)
        print(f"Using first {i} features | Accuracy: {accuracy:.2f}%")
    visualize(steps, accuracy_count)

def visualize(steps, accuracy):
    plt.bar(steps, accuracy, color=['red', 'green', 'blue'])
    plt.title("Accuracy vs. Number of Features")
    plt.xlabel("Number of Features (Steps)")
    plt.ylabel("Accuracy (%)")
    plt.show()

arr = np.genfromtxt('sonar.all-data', delimiter=',', dtype='str')
y = arr[:, -1]

steps = [20, 40, 60]

calculate(arr, steps, y, get_mlp)
