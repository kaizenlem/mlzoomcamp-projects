# mlzoomcamp-projects

Predicting Customer Lifetime Value (CLV) for B2B E-Commerce Using Machine Learning

1. Business Context & Motivation
   
    For B2B e-commerce companies, understanding which customers will generate the most long-term revenue is critical for resource allocation, account management, and retention marketing. By predicting Customer Lifetime Value (CLV), the business can:
   
     a. Prioritize high-potential clients for account management     
  
     b. Design targeted retention offers for at-risk, high-value clients  
   
     c. Optimize marketing spending and sales effort.


2. Problem Statement

    The objective of this project is to develop a machine learning model that predicts the Customer Lifetime Value (CLV) of B2B accounts based on their historical purchase behavior. The CLV prediction allows the company to forecast the future value each business client brings.


3. How ML Solves This Problem

    Machine learning can find non-obvious patterns in purchase frequency, recency, average spend, and product mix to produce an accurate CLV estimate per client. This insight can drive smarter business decisions, focusing effort where it maximizes impact.


4. Dataset

    For this project, we use the Retailrocket Recommender System Dataset, which consists of:
    
    User sessions and events: purchases, views, and other interactions;
    
    Item details and metadata.
    
    Note: In this B2B simulation, each “visitorid” is treated as a business customer account.

    
    Data Access
        This repository does not include raw data files due to their size.

        Please download the dataset(s) manually from https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset

        Place the datasets below in the project root before running code.

                events.csv

                item_properties_part1.csv

                item_properties_part2.csv

                category_tree.csv




5. Intended Use of the Solution

    Integrate CLV predictions into sales and marketing dashboards.
    
    Build targeted campaigns and optimize resource allocation for high-value accounts.
    
    Use it as a test bed for future personalization and upsell strategies.


6. Model Training and Evaluation

   Evaluated three regression models for predicting Customer Lifetime Value (CLV) as the number of purchases per customer:

    Linear Regression

    Decision Tree Regressor

    XGBoost Regressor


    Evaluation Metrics
    Model performance was measured using:

    | Model             | RMSE | R2R^2R2 |
    | ----------------- | ---- | ------- |
    | Linear Regression | 0.53 | 1.00    |
    | Decision Tree     | 1.52 | 0.97    |
    | XGBoost           | 0.81 | 0.99    |



    Model Selection

    Linear Regression achieved the best results in terms of both RMSE and 

    R2. This model has been selected for deployment.



    Model Training Code

    The logic and steps for data loading, feature engineering, and model training are provided in both the notebook and the dedicated train.py script for reproducibility.