from sklearn import tree

#(Tyres, Seats)

features = [[2, 2], [4, 2], [4, 5], [4, 4], [2, 1]]

labels = [0, 1, 1, 1, 0]

algorithm = tree.DecisionTreeClassifier()

algorithm = algorithm.fit(features, labels)

newData = [[2, 2]]

if algorithm.predict(newData) == 0:
    print("Motor")
else:
    print("Car")

