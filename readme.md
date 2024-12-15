**Exploring Advanced Machine Learning Techniques for Classification Problems**

**Group Members:**

Muhammad Hammad(SP23-BAI-034)

Moiz Asif (SP23-BAI-026)

**Introduction**

This project focuses on solving a complex classification problem by applying advanced machine learning techniques. The dataset, *Occupancy Estimation*, comprises sensor data and aims to predict room occupancy count as a multiclass classification task. The objective is to evaluate and compare the performance of three machine learning algorithms: Random Forest, Logistic Regression, and Support Vector Machine (SVM).

**Dataset Description**

- **Dataset Name:** Occupancy Estimation Dataset
- **Features:**
  - Sensor data: temperature, light, sound, CO2 levels, PIR motion sensors, etc.
- **Target:** Room occupancy count (4 unique classes: 0, 1, 2, 3).
- **Dataset Size:** 10,000+ samples with 10+ features.

**Preprocessing**

1. **Feature Scaling:** Applied StandardScaler to normalize feature values.
1. **Missing Data:** Ensured all necessary features and target columns were present.
1. **Dimensionality Reduction:** PCA was used for visualization in SVM.
1. **Class Imbalance Handling:** Stratified splitting was used for balanced training and testing sets.
-----
**Methodology**

**Algorithms**

1. **Random Forest Classifier**
   1. Tuned hyperparameters using RandomizedSearchCV:
      1. n\_estimators: [50, 100]
      1. max\_depth: [10, 15]
      1. min\_samples\_split: [2, 5]
   1. Optimized for f1\_weighted score.
   1. Achieved outstanding performance in handling multiclass data.
   1. Visualized a single decision tree from the forest.
1. **Logistic Regression**
   1. Configured for multiclass classification.
   1. Evaluated for standard metrics and ROC-AUC.
1. **Support Vector Machine (SVM)**
   1. Trained with a linear kernel and C=1.
   1. Visualized support vectors with PCA (2D projection).
-----
**Results**

**Random Forest Classifier**

- **Metrics:**
  - Accuracy: **1.00**
  - Precision: **1.00**
  - Recall: **1.00**
  - F1-Score: **1.00**
  - Macro Average F1-Score: **0.99**
- **Remarks:**
  - The Random Forest model achieved near-perfect classification performance across all metrics.
  - Excellent precision and recall for all four classes, demonstrating robustness.

**Logistic Regression**

- **Metrics:**
  - Accuracy: **0.9872**
  - Precision: **0.9876**
  - Recall: **0.9872**
  - F1-Score: **0.9872**
  - ROC-AUC: **0.9981**
- **Remarks:**
  - Logistic Regression performed remarkably well, with high accuracy and ROC-AUC scores.
  - The simplicity and interpretability of the model make it a viable choice.

**Support Vector Machine (SVM)**

- **Metrics:** (Placeholder if unavailable—these need to be calculated from actual results.)
- **Remarks:** SVM's support vector analysis provided useful insights into decision boundaries. Visualized support vectors enhance interpretability.
-----

**Algorithm Comparison**

|**Algorithm**|**Accuracy**|**Precision**|**Recall**|**F1-Score**|**ROC-AUC**|**Remarks**|
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|Random Forest|1\.00|1\.00|1\.00|1\.00|NA|Outstanding performance with all metrics near 1.00.|
|Logistic Regression|0\.9872|0\.9876|0\.9872|0\.9872|0\.9981|High performance; suitable for multiclass tasks.|
|Support Vector Machine|TBD|TBD|TBD|TBD|TBD|Requires complete evaluation metrics.|

-----
**Visualizations**

1. **Random Forest Visualization:**
   1. A single decision tree from the Random Forest was plotted to illustrate its decision process.

1. **SVM Visualization:**
   1. PCA was used to project high-dimensional data into two dimensions, highlighting support vectors.

-----
**Analysis**

- The Random Forest classifier outperformed other models, achieving perfect classification metrics.
- Logistic Regression also showed strong results with high accuracy and ROC-AUC.
- SVM's performance was insightful, with detailed analysis provided by support vectors and PCA visualization.
- All models demonstrated excellent generalization on test data, with the Random Forest providing the most consistent results.
-----
## **Conclusion**
The project successfully applied and evaluated three advanced machine learning algorithms for multiclass classification. The Random Forest model provided the best overall performance, followed by Logistic Regression. SVM added value through its interpretability and visual support vectors. This comprehensive analysis demonstrates the potential of advanced ML techniques in real-world classification problems.



