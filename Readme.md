# 📧 Email/SMS Spam Detection

## 📝 Project Overview

This project focuses on classifying messages (both **email** and **SMS**) as **spam** or **ham** (non-spam) using machine learning models. The dataset contains text messages labeled accordingly, aiming to train a model that can accurately filter out spam.

---

## 🔄 Process

1. **📥 Data Loading** – Load the dataset into a Pandas DataFrame  
2. **🧹 Data Preprocessing** – Clean text data and handle missing values  
3. **🔢 Label Encoding** – Encode labels (`spam = 0`, `ham = 1`)  
4. **📊 Data Splitting** – Divide the dataset into training and testing sets  
5. **🧠 Feature Extraction** – Use **TF-IDF Vectorization** to convert text into numeric features  
6. **🤖 Model Training** – Train multiple machine learning classifiers  
7. **✅ Model Evaluation** – Measure performance using **accuracy** and **precision**  
8. **🧪 Spam Detection** – Test the final model on new message samples

---

## ⚙️ Techniques & Tools

- **📌 Feature Engineering**: TF-IDF Vectorizer  
- **🧹 Data Preprocessing**: Missing value handling and text cleaning  
- **📈 Evaluation Metrics**: Accuracy and Precision  
- **🔧 Libraries Used**:
  - `numpy`  
  - `pandas`  
  - `scikit-learn`  
  - `streamlit` (for GUI interface)

---

## 🏆 Best Performing Model

> 🎯 **Random Forest Classifier (RF)**  
- **Accuracy**: `97.67%`  
- **Precision**: `97.50%`  
- ✅ Best model for classifying both email and SMS messages

---

## ✅ Conclusion

The **Email/SMS Spam Detection** project accurately distinguishes between spam and legitimate messages using machine learning. By combining effective **TF-IDF feature extraction** and strong classifiers like **Random Forest**, the project demonstrates high accuracy in spam detection.

---

## 🚀 Future Work

- Incorporate **deep learning** techniques (e.g., RNNs, LSTMs, BERT)  
- Enable **real-time spam filtering** for email/SMS streams  
- Improve feature extraction using **advanced NLP techniques**  
- Deploy the model as a **live web or mobile app**

---

## 📸 Sample Output Visuals

![Confusion Matrix](https://github.com/user-attachments/assets/794327f2-c3f4-4c30-93f3-793f6c1c0f98)

![Model Accuracy](https://github.com/user-attachments/assets/e00cdb2d-ebd4-47bc-8608-395a03370dce)
