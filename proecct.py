import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime


print(" Загрузка данных...")
df = pd.read_csv("order_10000 .csv") 

df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')


df = df.dropna(subset=['order_date'])
# Создаём год и месяц
df['year'] = df['order_date'].dt.year
df['month'] = df['order_date'].dt.to_period('M')

print(f" Загружено {len(df)} корректных заказов.")
print(f" Период: с {df['order_date'].min().date()} по {df['order_date'].max().date()}\n")
print(df.head(9).to_markdown(index=False))
total_orders = len(df)
total_revenue = df['total_amount'].sum()
avg_order_value = df['total_amount'].mean()

status_counts = df['status'].value_counts()
payment_methods = df['payment_method'].value_counts()
shipping_methods = df['shipping_method'].value_counts()

print(" ОСНОВНЫЕ МЕТРИКИ")
print(f"Всего заказов: {total_orders:,}")
print(f"Общая выручка: {total_revenue:,.2f}")
print(f"Средний чек: {avg_order_value:.2f}")
print("\nСтатусы заказов:")
print(status_counts)
print("\nПопулярные методы оплаты:")
print(payment_methods.head())
print("\nПопулярные способы доставки:")
print(shipping_methods.head())
monthly_sales = df.groupby('month')['total_amount'].sum()

