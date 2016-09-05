#!/usr/bin/python
import os
os.chdir('/Users/Vickykiki/Desktop/ud120-projects-master/choose_your_own')
import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture


features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
from sklearn.grid_search import GridSearchCV
### K nearest neighbors
from sklearn.neighbors import KNeighborsClassifier

#search for best parameter
param_grid = {'n_neighbors': [1,3,5,7,9],
              'weights': ['uniform', 'distance']}
clf = KNeighborsClassifier()
clf_cv = GridSearchCV(clf, param_grid).fit(features_train, labels_train)
clf_cv.best_params_

clf = KNeighborsClassifier(n_neighbors=4, weights='uniform')
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

acc = clf.score(features_test, labels_test)
#acc = float((pred==labels_test).sum())/len(labels_test)
print acc


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass

### Random forest
from sklearn.ensemble import RandomForestClassifier

#search for best parameter
param_grid = {'n_estimators': [50,100,150],
              'criterion': ['gini', 'entropy'],
              'max_depth': [3,5,8],
              'min_samples_leaf': [2,3,5]}
clf = RandomForestClassifier()
clf_cv = GridSearchCV(clf, param_grid).fit(features_train, labels_train)
clf_cv.best_params_

clf = RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=5, min_samples_leaf=2)
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

acc = clf.score(features_test, labels_test)
#acc = float((pred==labels_test).sum())/len(labels_test)
print acc
print clf.get_params


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass


### Ada Boosting
from sklearn.ensemble import AdaBoostClassifier

#search for best parameter
param_grid = {'n_estimators': [50,100,150],
              'learning_rate': [0.01, 0.05, 0.1, 0.2, 0.5]}
clf = AdaBoostClassifier()
clf_cv = GridSearchCV(clf, param_grid).fit(features_train, labels_train)
clf_cv.best_params_

clf = AdaBoostClassifier(n_estimators=100, learning_rate=0.1)
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

acc = clf.score(features_test, labels_test)
#acc = float((pred==labels_test).sum())/len(labels_test)
print acc
print clf.get_params


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass







