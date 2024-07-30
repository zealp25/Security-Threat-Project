import pandas as pd
import mysql.connector
from statsmodels.tsa.arima.model import ARIMA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Connect to the database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Nikunj@26',
    database='myorders'
)
cursor = connection.cursor()

# Fetch item-wise sales data
query = '''
SELECT OrderDate, ItemNumber, SUM(Quantity) as TotalQuantity
FROM Orders
GROUP BY OrderDate, ItemNumber
ORDER BY OrderDate
'''
sales_data = pd.read_sql(query, connection)

# Prepare data for ARIMA model
sales_data['OrderDate'] = pd.to_datetime(sales_data['OrderDate'])
sales_data = sales_data.set_index('OrderDate')

# Function to apply ARIMA and forecast
def forecast_sales(item_number, sales_data):
    item_sales = sales_data[sales_data['ItemNumber'] == item_number]['TotalQuantity']
    item_sales = item_sales.resample('D').sum().fillna(0)
    
    model = ARIMA(item_sales, order=(5, 1, 0))
    model_fit = model.fit()
    
    forecast = model_fit.forecast(steps=30)
    return forecast

# Predict sales for a specific item (e.g., item_number = 1)
item_number = 1
forecast = forecast_sales(item_number, sales_data)

# Plot the forecast
plt.figure(figsize=(10, 6))
plt.plot(sales_data[sales_data['ItemNumber'] == item_number]['TotalQuantity'], label='Historical Sales')
plt.plot(forecast, label='Forecast', color='red')
plt.xlabel('Date')
plt.ylabel('Sales Quantity')
plt.title(f'Item-wise Sales Forecast for Item {item_number}')
plt.legend()
plt.show()

# Fetch customer data
query = '''
SELECT CustomerNumber, SUM(Quantity) as TotalQuantity, SUM(Price * Quantity) as TotalSpent
FROM Orders
GROUP BY CustomerNumber
'''
customer_data = pd.read_sql(query, connection)

# Prepare data for clustering
X = customer_data[['TotalQuantity', 'TotalSpent']]

# Apply K-means clustering
kmeans = KMeans(n_clusters=3)
customer_data['Cluster'] = kmeans.fit_predict(X)

# Plot customer segments
plt.figure(figsize=(10, 6))
plt.scatter(customer_data['TotalQuantity'], customer_data['TotalSpent'], c=customer_data['Cluster'], cmap='viridis')
plt.xlabel('Total Quantity Purchased')
plt.ylabel('Total Amount Spent')
plt.title('Customer Segmentation')
plt.colorbar(label='Cluster')
plt.show()

# Close the database connection
cursor.close()
connection.close()
