from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql://postgres:postgres@localhost:5432/ecommerce_db')

print('='*50)
print('Top 1 Category')
print('='*50)
print('Which product category made the most money?')

df = pd.read_sql('SELECT "Category", SUM("Final_Price(Rs.)") as highest_revenue FROM sales GROUP BY "Category" ORDER BY highest_revenue DESC LIMIT 1', engine)
print(df)

print('='*50)
print('top 5 category')
print('Who are the top 5 customers by total spending?')

df1=pd.read_sql('SELECT "User_ID",SUM("Final_Price(Rs.)") as total_spending from sales GROUP BY "User_ID" ORDER BY total_spending DESC LIMIT 5',engine)
print(df1)


print('='*50)
print('Payment method')
print('Which payment method is used most frequently?')

df2=pd.read_sql('SELECT "Payment_Method",COUNT(*) AS count_of_orders,SUM("Final_Price(Rs.)") AS TOTAL FROM sales GROUP BY "Payment_Method" ORDER BY TOTAL DESC',engine)
print(df2)


print('='*50)
print('highest discount amount')
print('Which product got the highest discount amount?')

df3=pd.read_sql('SELECT "Product_ID",SUM("Discount_Amount") AS DISCOUNT FROM sales GROUP BY "Product_ID" ORDER BY DISCOUNT DESC LIMIT 1',engine)

print(df3)

print('='*50)
print('MONTHLY SALES TREND')
print('Which month had the highest sales?')



print("\n4. MONTHLY SALES TREND")
print("-" * 40)
df4 = pd.read_sql("""
SELECT
    DATE_TRUNC('month', CAST("Purchase_Date" AS DATE)) AS month,
    SUM("Final_Price(Rs.)") AS revenue
FROM sales
GROUP BY DATE_TRUNC('month', CAST("Purchase_Date" AS DATE))
ORDER BY month;
""", engine)

print(df4)
