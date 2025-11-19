import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import numpy as np

# 1. Load data
events = pd.read_csv('events.csv')

# 2. Keep only transactions (purchases)
purchases = events[events['event'] == 'transaction']

# 3. Group features for CLV modeling
clv = purchases.groupby('visitorid').agg(
    purchase_count=('itemid', 'size'),
    first_purchase=('timestamp', 'min'),
    last_purchase=('timestamp', 'max'),
    product_diversity=('itemid', 'nunique')
).reset_index()
clv['recency'] = purchases['timestamp'].max() - clv['last_purchase']

# 4. Split into features (X) and target (y)
X = clv.drop(['visitorid', 'purchase_count'], axis=1)
y = clv['purchase_count']

# 5. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6. Train Linear Regression model
lr = LinearRegression()
lr.fit(X_train, y_train)

# 7. Evaluate
y_pred = lr.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"Linear Regression RMSE: {rmse:.2f}")
print(f"Linear Regression R^2: {r2:.2f}")

# 8. Save model and features for deployment
joblib.dump(lr, "clv_model.joblib")
joblib.dump(X.columns.tolist(), "feature_columns.joblib")
