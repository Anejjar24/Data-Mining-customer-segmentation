# Customer Segmentation -- Data Mining Project

## 📌 Overview

This project focuses on **customer segmentation** using classical **data
mining techniques**.\
The goal is to identify meaningful customer groups based on purchasing
behaviors and demographic features, helping businesses improve marketing
strategies and decision‑making.

The project includes: - A complete **Jupyter Notebook** explaining the
data preprocessing, clustering steps, and evaluation. - A **Streamlit
web application** for interactive visualization of clusters. - A
detailed **PDF report** summarizing the methodology and results.

<img width="408" height="421" alt="Image" src="https://github.com/user-attachments/assets/7874ee96-03ae-42b0-9780-c317c9bb1844" />

------------------------------------------------------------------------

## 🔍 Methods & Techniques

### **1. Data Mining Techniques**

-   **K-Means Clustering**\
    Used to partition customers into distinct segments based on feature
    similarity.

### **2. Evaluation Metric**

-   **Silhouette Score**\
    Evaluates cluster quality and helps determine the optimal number of
    clusters.

### **3. Visualization**

-   Cluster plots (2D & 3D)
-   Feature distribution graphs
-   Summary statistics\
    These visual insights help interpret and explain the segmentation
    results.

### **4. Streamlit Interface**

An interactive dashboard allowing users to: - Upload or view dataset -
Select number of clusters - Visualize segmentation results in
real-time - Inspect cluster-level insights

------------------------------------------------------------------------

## 📁 Project Structure

    project-customer-segmentation/
    │
    ├── notebook/
    │   └── customer_segmentation.ipynb
    │
    ├── streamlit_app/
    │   ├── app.py
    │   ├── requirements.txt
    │   └── assets/
    │
    ├── report/
    │   └── customer_segmentation_report.pdf
    │
    ├── data/
    │   └── dataset.csv   (optional if not sensitive)
    │
    └── README.md

------------------------------------------------------------------------

## 🚀 How to Run the Streamlit App

### **1. Install Dependencies**

``` bash
pip install -r streamlit_app/requirements.txt
```

### **2. Run the App**

``` bash
streamlit run streamlit_app/app.py
```

------------------------------------------------------------------------

## 🛠 Technologies Used

-   Python\
-   Pandas, NumPy\
-   Scikit-learn\
-   Matplotlib, Seaborn\
-   Streamlit

------------------------------------------------------------------------

## 📄 Report

The full project analysis is available in the PDF report:\
**`report/customer_segmentation_report.pdf`**

------------------------------------------------------------------------

## 📬 Author

**Ihsane**\
Data Mining & Machine Learning Enthusiast
