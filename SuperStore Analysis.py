
  #importing pandas as pd into the idle
import pandas as pd
   #importing matplotlib.pyplot as plt
import matplotlib.pyplot as plt
   #importing seaborn as sns
import seaborn as sns  

# Loading dataset into the idle
df = pd.read_csv(r"C:\projects\Sales.csv.xlsx")

# Converting the 'Order Date'  to datetime values
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

# Calculating the required summary for the metrics to make graph amongs sales per year
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df.shape[0]

# Printing metrics in the console
print(f"💰 Total Sales: ${total_sales:,.2f}")
print(f"📈 Total Profit: ${total_profit:,.2f}")
print(f"🧾 Total Orders: {total_orders}")

# Grouping  sales per year
df['Order Year'] = df['Order Date'].dt.year
sales_by_year = df.groupby("Order Year")["Sales"].sum()

# Ploting the graph among : Sales in Years
plt.figure(figsize=(10, 5))
ax = sales_by_year.plot(kind='line', marker='o', color='dodgerblue')
plt.title("Sales by Year")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.grid(True)
plt.gcf().set_facecolor('#e0f7fa')
ax.set_facecolor('#b2ebf2')
plt.tight_layout()
plt.show()







# Grouping the sum of sales for category as sales_by_category
sales_by_category = df.groupby("Category")["Sales"].sum()

# Ploting the Sales by Category (In Horizontal Bar)
plt.figure(figsize=(8, 6))
sales_by_category.sort_values().plot(kind='barh', color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
plt.title("Sales by Category")
plt.xlabel("Total Sales")
plt.ylabel("Category")
plt.grid(True, axis='x')
plt.gcf().set_facecolor('#f5f5f5')
plt.tight_layout()
plt.show()



























# finding top sales Top cities from the  data
top_cities = df.groupby("City")["Sales"].sum().sort_values(ascending=False).head(10)

# Plot: Top 10 Cities by Sales
plt.figure(figsize=(10, 6))
ax = top_cities.plot(kind='bar', color='skyblue')
plt.title("Top 10 Cities by Sales")
plt.ylabel("Total Sales")
plt.xlabel("City")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.gcf().set_facecolor('#fff4e6')
ax.set_facecolor('#f0f8ff')
plt.tight_layout()
plt.show()

























#ploting the graph among the sales by Region with (Heatmap)
sales_by_region_year = df.groupby(['Order Year', 'Region'])['Sales'].sum().unstack()

plt.figure(figsize=(12, 6))
sns.heatmap(sales_by_region_year, annot=True, fmt='.0f', cmap='coolwarm', cbar_kws={'label': 'Sales'})
plt.title('Sales by Region (Heatmap)')
plt.xlabel('Region')
plt.ylabel('Year')
plt.gcf().set_facecolor('#fffacd')
plt.tight_layout()
plt.show()





























# creating a Pie Chart: Profit by Discount Level (Enhanced)
df['Discount Level'] = (df['Discount'] * 10).round(0) / 10
profit_by_discount = df.groupby('Discount Level')['Profit'].sum()
profit_by_discount = profit_by_discount[profit_by_discount > 0]

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666']
explode = [0.05] * len(profit_by_discount)

fig, ax = plt.subplots(figsize=(9, 9))
wedges, texts, autotexts = ax.pie(
    profit_by_discount,
    labels=profit_by_discount.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors[:len(profit_by_discount)],
    explode=explode,
    shadow=True,
    wedgeprops={'edgecolor': 'black'}
)
# Cleaning the title without the emoji
ax.set_title('Profit Distribution by Discount Level', fontsize=16, weight='bold', color='darkblue')
ax.axis('equal')
ax.set_facecolor('#e6f2ff')
# Ploting area backgroundwith a color
fig.patch.set_facecolor('#f0fff0')
# Figure background

# Styling text with colour and font
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_weight('bold')

plt.tight_layout()
plt.show()


























#creating Area Chart among the : Top 10 Products by Profit
profit_by_product = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)
profit_by_product = profit_by_product.sort_values(ascending=True)
#applying colour for Area graph Sorted for area fill effect
plt.figure(figsize=(10, 6))
plt.fill_between(profit_by_product.index, profit_by_product.values, color='mediumseagreen', alpha=0.6)
plt.plot(profit_by_product.index, profit_by_product.values, marker='o', color='seagreen', linewidth=2)

plt.title('Top 10 Products by Profit (Area Chart)', fontsize=14, weight='bold')
plt.xlabel('Product Name')
plt.ylabel('Profit')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.gcf().set_facecolor('#f0fff0')
# applying a color for background: Soft green background
plt.tight_layout()
plt.show()


















