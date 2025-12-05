# 🚢 Titanic Survival Prediction - Detailed Guide

**Project:** Machine Learning Classification  
**Dataset:** Titanic Passenger Data (1309 records)  
**Goal:** Predict survival based on passenger features  
**Difficulty:** Intermediate  
**Time:** 1-2 hours  

---

## 📊 Dataset Overview

**File:** `titanic3.csv`

**Features:**
- `pclass` - Passenger class (1st, 2nd, 3rd)
- `survived` - Target variable (0 = died, 1 = survived)
- `sex` - Gender (male/female)
- `age` - Age in years
- `sibsp` - # of siblings/spouses aboard
- `parch` - # of parents/children aboard
- `fare` - Ticket fare in pounds
- `embarked` - Port of embarkation (C/Q/S)

**Data Quality:**
- Missing values present (marked as '?')
- Need type conversion for age/fare
- Some null values need handling

---

## 🎯 Project Structure

### Part 1: Data Loading & Cleaning (Cells 1-4)

**What Happens:**
```python
# Load data
data = pd.read_csv('titanic3.csv')

# Clean missing values
data.replace('?', np.nan, inplace=True)
data = data.astype({"age": np.float64, "fare": np.float64})
```

**Java Equivalent:**
```java
// Would require:
// - BufferedReader for file reading
// - Manual parsing of CSV
// - Loop through rows to clean data
// - Type conversion with try-catch
// Python: 4 lines | Java: ~50+ lines
```

---

### Part 2: Exploratory Data Analysis (Cell 5)

**Visualizations Created:**
1. **Violin Plot:** Age distribution by survival & sex
2. **Point Plot:** Siblings/spouses vs survival by sex
3. **Point Plot:** Parents/children vs survival by sex
4. **Point Plot:** Passenger class vs survival by sex
5. **Violin Plot:** Fare distribution by survival & sex

**Key Insights:**
- Women had significantly higher survival rates
- 1st class passengers survived more
- Children had higher survival probability
- Fare correlates with survival (higher fare = better class)

---

### Part 3: Feature Engineering (Cells 6-9)

**Step 1: Encode Gender (Cell 6)**
```python
data.replace({'male': 1, 'female': 0}, inplace=True)
```
- Converts categorical to numerical
- Required for ML algorithms

**Step 2: Correlation Analysis (Cell 7)**
```python
data.corr(numeric_only=True).abs()[["survived"]]
```
- Shows which features correlate with survival
- Helps identify important features

**Step 3: Create New Feature (Cell 8)**
```python
data['relatives'] = data.apply(
    lambda row: int((row['sibsp'] + row['parch']) > 0), 
    axis=1
)
```
- Combines sibsp + parch
- Binary: 1 if has family, 0 if alone
- **Why?** Being alone vs with family affects survival

**Java Note:**
```java
// Lambda: lambda row: expression
// Java 8+: row -> expression
// Python lambda is more flexible for DataFrame operations
```

**Step 4: Select Final Features (Cell 9)**
```python
data = data[['sex', 'pclass','age','relatives','fare','survived']].dropna()
```
- Keep only relevant columns
- Remove rows with missing values
- Clean dataset ready for ML

---

### Part 4: Machine Learning - Naive Bayes (Cells 10-15)

**Cell 12: Train/Test Split**
```python
x_train, x_test, y_train, y_test = train_test_split(
    data[['sex','pclass','age','relatives','fare']], 
    data.survived, 
    test_size=0.2, 
    random_state=0
)
```
- 80% training, 20% testing
- `random_state=0` ensures reproducibility
- **Java Equivalent:** Manual array manipulation and shuffling

**Cell 13: Feature Scaling**
```python
sc = StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.transform(x_test)
```

**Why StandardScaler?**
- Converts features to same scale (mean=0, std=1)
- Prevents features with larger ranges from dominating
- Example: Age (0-80) vs Fare (0-500) vs Sex (0-1)
- Critical for distance-based algorithms & neural networks

**Java Note:**
```java
// fit_transform() = Learn statistics + Apply transformation
// transform() = Apply previously learned transformation
// Similar to training vs inference pattern
```

**Cell 14: Train Model**
```python
model = GaussianNB()
model.fit(X_train, y_train)
```
- Gaussian Naive Bayes classifier
- Fast, simple, works well with small datasets
- Assumes features are independent (naive assumption)

**Cell 15: Evaluate Model**
```python
predict_test = model.predict(X_test)
print(metrics.accuracy_score(y_test, predict_test))
```
- Makes predictions on test set
- Calculates accuracy (% correct predictions)
- **Expected Accuracy:** ~75-80%

---

### Part 5: Neural Network - TensorFlow/Keras (Cells 16+)

**Cell 25: Build Neural Network**
```python
model = Sequential()
model.add(Dense(5, kernel_initializer='uniform', activation='relu', input_dim=5))
model.add(Dense(5, kernel_initializer='uniform', activation='relu'))
model.add(Dense(1, kernel_initializer='uniform', activation='sigmoid'))
```

**Architecture:**
```
Input Layer:     5 features (sex, class, age, relatives, fare)
                 ↓
Hidden Layer 1:  5 neurons (ReLU activation)
                 ↓
Hidden Layer 2:  5 neurons (ReLU activation)
                 ↓
Output Layer:    1 neuron (Sigmoid activation)
                 ↓
Output:          Probability of survival (0-1)
```

**Activation Functions:**
- **ReLU (Rectified Linear Unit):** `f(x) = max(0, x)`
  - Used in hidden layers
  - Prevents vanishing gradient problem
- **Sigmoid:** `f(x) = 1 / (1 + e^(-x))`
  - Used in output layer
  - Outputs probability (0-1)

**Cell 28: Train Neural Network**
```python
model.compile(optimizer="adam", loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, batch_size=32, epochs=50)
```

**Parameters:**
- `optimizer="adam"` - Adaptive learning rate optimizer
- `loss='binary_crossentropy'` - Loss function for binary classification
- `batch_size=32` - Process 32 samples at a time
- `epochs=50` - Train for 50 complete passes through data

**Java Note:**
```java
// Python ML framework handles backpropagation automatically
// Java: Would need Deeplearning4j or manual implementation
// Python: ~10 lines | Java DL4J: ~100+ lines
```

---

## 🔍 Key Concepts Explained

### 1. Train/Test Split
**Why?**
- Test data simulates real-world unseen data
- Prevents overfitting
- Validates model generalizes well

**Analogy:**
- Training set = Study guide
- Test set = Final exam
- Never study from the exam questions!

### 2. StandardScaler
**Before Scaling:**
```
Age:  [2, 45, 60]
Fare: [10, 500, 250]
Sex:  [0, 1, 0]
```

**After Scaling:**
```
Age:  [-1.2, 0.1, 0.9]
Fare: [-0.8, 1.5, 0.3]
Sex:  [-0.7, 0.7, -0.7]
```

All features now on similar scale → Better model performance

### 3. Lambda Functions
```python
# Python lambda
lambda row: int((row['sibsp'] + row['parch']) > 0)

# Java equivalent
row -> (row.getSibsp() + row.getParch()) > 0 ? 1 : 0
```

### 4. Correlation
- Measures relationship between features (-1 to +1)
- +1 = Perfect positive correlation
- 0 = No correlation
- -1 = Perfect negative correlation

---

## 📈 Expected Results

**Naive Bayes Accuracy:** ~75-80%
**Neural Network Accuracy:** ~78-82% (should be slightly better)

**Confusion Matrix Interpretation:**
```
                Predicted Dead | Predicted Survived
Actually Dead        [TN]      |      [FP]
Actually Survived    [FN]      |      [TP]

TN = True Negative (correctly predicted dead)
TP = True Positive (correctly predicted survived)
FN = False Negative (missed survivors)
FP = False Positive (predicted survived but died)
```

---

## 🐛 Common Issues

### Issue: Model accuracy too low (<70%)
**Possible Causes:**
- Forgot to run feature engineering cells
- Data not scaled properly
- Missing values not handled

**Solution:**
- Rerun cells 6-9 (feature engineering)
- Ensure cell 13 (StandardScaler) executed
- Check cell 9 removed NaN values

### Issue: ValueError on model.fit()
**Cause:** Shape mismatch between X and y

**Solution:**
```python
print(X_train.shape)  # Should be (n_samples, 5)
print(y_train.shape)  # Should be (n_samples,)
```

### Issue: TensorFlow import errors
**Solution:**
```bash
pip install --upgrade tensorflow
# Restart kernel
```

---

## 🎓 What You Learned

✅ Data cleaning and preprocessing  
✅ Exploratory data analysis with visualizations  
✅ Feature engineering (creating new features)  
✅ Train/test split methodology  
✅ Feature scaling with StandardScaler  
✅ Classification with Naive Bayes  
✅ Neural network architecture design  
✅ Model evaluation and comparison  

---

## 🚀 Next Steps

**Improve This Project:**
- [ ] Try other models (Random Forest, SVM, Logistic Regression)
- [ ] Add cross-validation (K-fold)
- [ ] Feature importance analysis
- [ ] Hyperparameter tuning (GridSearchCV)
- [ ] Save best model to disk (pickle/joblib)
- [ ] Create prediction function for new data

**Challenge Yourself:**
```python
# Try predicting for a new passenger
new_passenger = {
    'sex': 0,        # female
    'pclass': 1,     # first class
    'age': 25,
    'relatives': 1,  # has family
    'fare': 100
}
# Scale features and predict survival probability
```

---

## 📚 Additional Resources

**Datasets:**
- Kaggle Titanic: https://www.kaggle.com/c/titanic
- UCI ML Repository: https://archive.ics.uci.edu/ml/

**Learn More:**
- Scikit-learn docs: https://scikit-learn.org/
- TensorFlow tutorials: https://www.tensorflow.org/tutorials
- Seaborn gallery: https://seaborn.pydata.org/examples/

**Books:**
- "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" by Aurélien Géron

---

**Documentation Last Updated:** December 4, 2025  
**Notebook Version:** v1.0  
**Python Version:** 3.9+
