# Email Spam Detection

## Project Overview

The Email Spam Detection project focuses on classifying emails as spam or ham (non-spam) using various machine learning models. The dataset consists of email messages labeled as spam or ham.

## Process

Data Loading – Load the dataset into a Pandas DataFrame.

1. Data Preprocessing – Handle missing values and clean the text data.

2. Label Encoding – Convert labels into numerical values (spam = 0, ham = 1).

3. Data Splitting – Split data into training and testing sets.

4. Feature Extraction – Use TF-IDF Vectorization to convert text into numerical features.

5. Model Training – Train different machine learning models for classification.

6. Model Evaluation – Compute accuracy and precision scores.

7. Spam Detection – Test the model with sample email messages.


## Techniques & Tools

1. Feature Engineering – TF-IDF Vectorization for text representation.

2. Data Preprocessing – Handling missing values and text cleaning.

3. Evaluation Metrics – Accuracy and Precision scores.

4. Libraries Used

    . numpy

    . pandas

    . scikit-learn
  
    . streamlit (for UI)

# Best Performing Model

The Random Forest (RF) model achieved the highest accuracy of 97.67% with a precision of 97.50%, making it the most effective model for email spam detection.

# Conclusion
The Email Spam Detection project successfully classifies emails as spam or ham using various machine learning models. Among the tested models, Random Forest (RF) achieved the best performance with high accuracy and precision. By leveraging TF-IDF Vectorization and effective data preprocessing, the classifier efficiently detects spam messages. This project highlights the importance of text classification in filtering unwanted emails and improving communication security.

Future enhancements can include deep learning models, improved feature engineering, and real-time spam detection for better accuracy and robustness.



![image](https://github.com/user-attachments/assets/794327f2-c3f4-4c30-93f3-793f6c1c0f98)

![image](https://github.com/user-attachments/assets/e00cdb2d-ebd4-47bc-8608-395a03370dce)
