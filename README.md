# mlzoomcamp-projects

Predicting Customer Lifetime Value (CLV) for B2B E-Commerce Using Machine Learning

   This project predicts Customer Lifetime Value (CLV) using behavioral data from an e-commerce platform. The pipeline includes data cleaning, EDA, feature engineering, training and comparing 
   
   multiple regression models (Linear Regression, Decision Tree, XGBoost), and deploying the best model as a web service using FastAPI.



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


         Directory Structure
         ├── clv.ipynb                # Full EDA, feature engineering, model comparison
         ├── train.py                 # Script to train and export final model
         ├── main.py                  # FastAPI app for model deployment
         ├── requirements.txt         # Project dependencies
         ├── .gitignore               # Files/folders excluded from git
         ├── Dockerfile               # (Optional) for containerized deployment
         ├── README.md                # Project instructions and documentation
         └── data/                    # (Not in repo) User-downloaded CSV data files
         

      Setup Instructions

      Clone this repo:
      
            bash
            git clone <your-repo-link>
            cd <project-folder>

      Install dependencies:
            
            bash
            pip install -r requirements.txt

      Download data files and place them in the project folder.


6. Intended Use of the Solution

    Integrate CLV predictions into sales and marketing dashboards.
    
    Build targeted campaigns and optimize resource allocation for high-value accounts.
    
    Use it as a test bed for future personalization and upsell strategies.





      Exploratory Data Analysis (EDA)
      
         See clv.ipynb for:
         
         Data overview, missing values analysis
         
         Event type distribution (view, addtocart, transaction)
         
         CLV-relevant feature engineering (purchase count, product diversity, recency, etc.)
         
         Sample outputs and insights


7. Model Training and Evaluation

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



   Deployment
   
      Deploy model as FastAPI web app:

         bash
         uvicorn main:app --reload
         Visit http://localhost:8000/docs for interactive API documentation.

      (Optional) Build and run via Docker:
      
            bash
            docker build -t clv-api .
            docker run -p 80:80 clv-api




8. API Usage

        ## Running the API

        1. **Install requirements:**

            pip install -r requirements.txt


        2. **Train the model (if not done yet):**

            python train.py


        3. **Start the API:**

            uvicorn main:app --reload


        4. **Test API via Swagger UI:**

            Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.


            ### Sample API Request (JSON)

            POST to `/predict` with:
            {
            "first_purchase": 1433176736375,
            "last_purchase": 1433222276276,
            "product_diversity": 5,
            "recency": 0
            }

        
            Response:
            {
            "predicted_clv": 1.07
            }

