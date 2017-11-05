# Machine Learning Recipes #1 from Google Developers - https://www.youtube.com/watch?v=cKxRvEZd3Mw

from sklearn import tree

# 0 = Bumpy. 1 = Smooth.
features = [[140, 1], [130, 1], [150, 0], [170, 0]]

# 0 = Apple. 1 = "Orange"
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print(clf.predict([[160,0]]))
