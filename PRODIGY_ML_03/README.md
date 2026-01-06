# Task 3 – Cat vs Dog Image Classification using SVM

## 📌 Objective
To implement a Support Vector Machine (SVM) model for classifying images of cats and dogs using a classical machine learning approach.

---

## 🗂 Dataset
- **Dataset Name:** Dogs vs Cats
- **Source:** Kaggle  
- **Link:** https://www.kaggle.com/c/dogs-vs-cats/data  

⚠️ The dataset is **not included** in this repository due to its large size.

---

## 🛠️ Methodology
1. Images are resized to **32×32 pixels**
2. Pixel values are normalized
3. Images are flattened into feature vectors
4. Dataset is shuffled to avoid class-order bias
5. A subset of images is used to handle memory limitations
6. A **Linear Support Vector Machine (SVM)** is trained for classification

---

## ⚙️ Model Details
- **Algorithm:** Support Vector Machine (SVM)
- **Kernel:** Linear
- **Train/Test Split:** 80% / 20%
- **Evaluation Metric:** Accuracy

---

## 📊 Results

> Note: Classical SVMs using raw pixel features are not optimal for large-scale image classification tasks.  
> This project focuses on demonstrating the complete machine learning pipeline rather than achieving high accuracy.

---

## 🚀 How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
