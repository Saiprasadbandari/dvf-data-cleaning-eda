# DVF Data Cleaning and Analysis

## Project Objective

This project analyzes the French DVF (Demande de Valeurs Foncières) dataset from 2021 to 2025. The objective is to clean, prepare, and explore the data using Python and Pandas while applying data preprocessing, exploratory data analysis, and feature engineering techniques.

## Dataset

Source: DVF (Demandes de Valeurs Foncières) Open Data

Period Covered:

* 2021
* 2022
* 2023
* 2024
* 2025

## Project Workflow

### 1. Data Collection

* Downloaded five years of DVF data
* Loaded datasets using Pandas

### 2. Data Cleaning

* Missing value analysis
* Removal of columns with more than 80% missing values
* Date conversion
* Property value conversion
* Duplicate removal

### 3. Outlier Detection

* IQR (Interquartile Range) method
* Detection of extreme property values

### 4. Exploratory Data Analysis

#### 1D Analysis

* Property type distribution
* Transaction type distribution
* Property value distribution

#### 2D Analysis

* Property value vs built surface area
* Average property value by property type

### 5. Feature Engineering

Created new features:

* year
* month
* price_per_m2
* department

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook
* Git/GitHub

## Repository Structure

```text
notebooks/
src/
data/
reports/
```

## Commit History Summary

1. Initial repository setup
2. Project structure creation
3. Dependency management
4. Data loading notebook
5. Python data loading script
6. Missing value analysis
7. Data type conversion
8. Data cleaning notebook
9. Outlier detection
10. Exploratory data analysis
11. Feature engineering
12. Project documentation

## Result

The DVF dataset was successfully cleaned, analyzed, and prepared for future machine learning and real estate analytics applications.
