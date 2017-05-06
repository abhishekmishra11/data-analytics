<h1>Trawler Logistic Regression Model</h1>

<h2>Import Modules</h2>

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from patsy import dmatrices
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn import model_selection
import pylab as pl


<h2>Data Pre-Processing</h2>
#Load all the data into numpy arrays
trawler_data = np.load('datasets/measures/kristina_ps.measures.npz')

#Move _data['x'][:] into _x[:]
trawler_data = trawler_data['x']

#Convert into Pandas data frame
trawler_data = pd.DataFrame(trawler_data)



#drop unknown fishing points
trawler_data['classification'].astype(int)
trawler_data = trawler_data[trawler_data['classification'] != -1]

#drop duplicate rows
trawler_data.drop_duplicates()



# create dataframes with an intercept column and dummy variables for
# occupation and occupation_husb
y, X = dmatrices('classification ~ measure_courseavg_10800 + measure_courseavg_1800 + measure_courseavg_21600 + measure_courseavg_3600 + measure_courseavg_43200 + measure_courseavg_86400 + measure_coursestddev_10800 + measure_coursestddev_1800 + measure_coursestddev_21600 + measure_coursestddev_3600 + measure_coursestddev_43200 + measure_coursestddev_86400 + measure_pos_10800 + measure_pos_1800 + measure_pos_21600 + measure_pos_3600 + measure_pos_43200 + measure_pos_86400 + measure_speedavg_10800 + measure_speedavg_1800 + measure_speedavg_21600 + measure_speedavg_3600 + measure_speedavg_43200 + measure_speedavg_86400 + measure_speedstddev_10800 + measure_speedstddev_1800 + measure_speedstddev_21600 + measure_speedstddev_3600 + measure_speedstddev_43200 + measure_speedstddev_86400', trawler_data, return_type="dataframe")
print X.columns
y = np.ravel(y)



# examine the coefficients
#pd.DataFrame(zip(X.columns, np.transpose(trawler_model.coef_)))



# evaluate the model by splitting into train and test sets
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3, random_state=0)
trawler_model = LogisticRegression()
trawler_model.fit(X_train, y_train)



# predict class labels for the test set
predicted = trawler_model.predict(X_test)
print predicted
print predicted.mean()




# generate class probabilities
probs = trawler_model.predict_proba(X_test)
print probs




# generate evaluation metrics
print metrics.accuracy_score(y_test, predicted)
print metrics.roc_auc_score(y_test, probs[:, 1])




# calculate the fpr and tpr for all thresholds of the classification
probs = trawler_model.predict_proba(X_test)
preds = probs[:,1]
fpr, tpr, thresholds = metrics.roc_curve(y_test, preds)
roc_auc = metrics.auc(fpr, tpr)

# define a function that accepts a threshold and prints sensitivity and specificity
def evaluate_threshold(threshold):
    print('Sensitivity:', tpr[thresholds > threshold][-1])
    print('Specificity:', 1 - fpr[thresholds > threshold][-1])

print evaluate_threshold(0.5)

# method I: plt
import matplotlib.pyplot as plt
plt.title('Receiver Operating Characteristic')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()





# Compute Precision-Recall and plot curve
precision, recall, thresholds = metrics.precision_recall_curve(y_test, preds)
area = metrics.auc(recall, precision)
print "Area Under Curve: %0.2f" % area

pl.clf()
pl.plot(recall, precision, label='AUC=%0.2f' % area)
pl.xlabel('Recall')
pl.ylabel('Precision')
pl.ylim([0.0, 1.05])
pl.xlim([0.0, 1.0])
pl.title('Precision-Recall' )
pl.legend(loc="center right")
pl.show()




# define a function that accepts a threshold and prints sensitivity and specificity
#def evaluate_threshold(threshold):
#    print('Sensitivity:', tpr[thresholds > threshold][-1])
#    print('Specificity:', 1 - fpr[thresholds > threshold][-1])

#for t in range(0,100):
#    print 0.005*t
#    evaluate_threshold(0.005*t)



print metrics.confusion_matrix(y_test, predicted)
print metrics.classification_report(y_test, predicted)



# evaluate the model using 10-fold cross-validation
scores = model_selection.cross_val_score(LogisticRegression(), X, y, scoring='accuracy', cv=10)
print scores
print scores.mean()



#cross_val_score(LogisticRegression(), X, y, cv=10, scoring='roc_auc').mean()
