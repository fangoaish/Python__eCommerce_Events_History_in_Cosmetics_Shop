import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Load the dataset into a DataFrame
raw = pd.read_csv("../input/ecommerce-events-history-in-cosmetics-shop/2020-Jan.csv")
raw["event_time"] = pd.to_datetime(raw["event_time"], errors='coerce')
print(raw.shape)
# Show the first ten rows
raw.head(10)

# Show dataset information
raw.info()

# Count non-NA values
raw.count()

# Count null values
raw.isnull().sum()

# Create products table
products = raw[["product_id", "category_code", "brand", "price"]].drop_duplicates()
print(products)

# Creat users table
users = raw[["user_id", "user_session"]].drop_duplicates()
print(users)

# Creat events talbe
events = raw[["event_time", "event_type", "product_id", "user_session"]].drop_duplicates()
print(events)


# Opportunity 1: Increase more customers
# 1) Acquiring new customers: find out the best selling products


# Combine the events table and the products table with a join
event_by_product = events.merge(products, how="inner", on="product_id")

# Group all the purchase events by product_id and calculate the sum of price as total revenue
revenue_by_product = event_by_product[event_by_product["event_type"] == "purchase"].groupby("product_id", as_index = False)["price"].sum().sort_values("price", ascending=False)
print(revenue_by_product)

# Visualize categorical data
plt.figure(figsize=(10, 6))
sns.set_style('white')
colors = sns.color_palette("pastel")
sns.barplot(x="product_id", y="price", data=revenue_by_product.head(10), palette=colors, order=revenue_by_product.head(10)['product_id'])
plt.title("Top 10 Best Selling Products")
plt.xlabel("Product Id")
plt.ylabel("Total Revenue ($)")
plt.show()


# Opportunity 1: Increase more customers
# 2) Retaining existing customers: find out the cart abandonment rate


# 1) Overall conversion rate
# Conversion Rate = Number of Conversions / Total Number of Visitors
num_of_conversions = (events["event_type"] == "purchase").sum()
total_num_of_visitors = raw.shape[0]
cart_cvr = round((num_of_conversions / total_num_of_visitors) * 100, 2)
print(f"The overall conversion rate for 2020 January is : {cart_cvr}%")


# 2) Cart abandonment rate per user session
# Combine the events table and the users table with a join
event_user = events.merge(users, how="inner", on="user_session")

# Calculate the number of conversions per user
conversions_per_user = event_user[event_user["event_type"] == "purchase"].groupby("user_id")["event_type"].value_counts().shape[0]

# Calculate the number of cart per user
cart_per_user = event_user[event_user["event_type"] == "cart"].groupby("user_id")["event_type"].value_counts().shape[0]

# Calculate the cart abandonment rate per user
cart_abandonment_rate_per_user = round((1 - (conversions_per_user / cart_per_user)) * 100, 2)
print(f"The overall cart abandonment rate for 2020 January is : {cart_abandonment_rate_per_user}%")

# Display the cart abandonment rate per user
labels = ["Conversion Rate", "Other events", "Cart abandonment rate"]
event_data = [6.18, 24.27, 69.55]
sns.set_style("whitegrid")
colors = sns.color_palette("pastel")
plt.pie(event_data, labels=labels, colors=colors, autopct='%.0f%%')
plt.title("Distribution of events")
plt.show()


# Opportunity 2: Increase order frequency
# 1) Count the popular hour time


# Split event_time into date, time, weekday
events["date"] = events["event_time"].dt.date
events["time"] = events["event_time"].dt.time
events["weekday"] = events["event_time"].dt.weekday

# Add hour column
events["hour"] = events["time"].apply(lambda x: x.hour)

# Use for loop to get the event counts per hour
# Define the sorted event type first
event_type_sorted = ["view", "cart", "purchase"]

event_per_hour = {}
for event_type in event_type_sorted:
    event_count = events[events.event_type == event_type].groupby("hour")["event_type"].count()
    event_per_hour[event_type] = event_count

# Create a dataframe from a dictionary
event_per_hour_df = pd.DataFrame(event_per_hour)
print(event_per_hour_df)


#Visualize to line chart
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
colors = sns.color_palette("pastel", 3)
sns.lineplot(data=event_per_hour_df, markers=False, palette=colors)
plt.title("Event Counts Per Hour")
plt.xlabel("Hour")
plt.ylabel("Event Count")
plt.legend(title="Event Type", loc="upper right")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlim(0)
plt.ylim(0)
sns.despine()
plt.show()


# Opportunity 2: Increase order frequency
# 2) Count the popular weekday

# Use for loop to get the event counts per weekday
event_per_weekday = {}
for event_type in event_type_sorted:
    event_count = events[events.event_type == event_type].groupby("weekday")["event_type"].count()
    event_per_weekday[event_type] = event_count

# Create a dataframe from a dictionary
weekdays_index = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
event_per_weekday_df = pd.DataFrame(event_per_weekday)

# Map numeric index to day names
event_per_weekday_df.index = event_per_weekday_df.index.map(weekdays_index)
print(event_per_weekday_df)

'''
reference: https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html
I use the map() function on the DataFrame's index. This function takes a dictionary or a function as an argument. In this case, I'm passing the weekdays_index dictionary.
The map() function then iterates over each index value in the DataFrame, looks up the corresponding value in the weekdays_index dictionary, and replaces it with the mapped value (day name).
After applying map(), the DataFrame's index is updated with the day names.
So, index.map() is used here to transform the index values according to the mapping defined in the weekdays_index dictionary.
'''

# Plot the line chart
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
colors = sns.color_palette("pastel", 3)
sns.lineplot(data=event_per_weekday_df, markers=False, palette=colors)
plt.title("Event Counts Per Weekday")
plt.xlabel("Weekday")
plt.ylabel("Event Count")
plt.legend(title="Event Type", loc="upper right")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlim(0)
sns.despine()
plt.show()


# Opportunity 3: Increase order value
# 1) What is the average order value?


# Merge events table with products table
# Select only product_id and user_session columns to exclude the column which is in datetime64 type from events table
product_sold = events[events["event_type"] == "purchase"][["product_id","user_session"]]
product_sold_price = product_sold.merge(products, how="left", on="product_id")[["user_session", "price"]]

# Group by user_session and sum up the price for products purchased
sum_product_sold_price = product_sold_price.groupby("user_session").sum().sort_values("price", ascending=False)

# Calculate the average order value by summing up the amount of price and dividing by the total number of users
average_order_value = round(sum_product_sold_price["price"].sum() / sum_product_sold_price.shape[0], 2)
print(f"The Average Order Value of each purchase is: {average_order_value}$!")

# How many percentage of users fall below the average order value?
users_count = sum_product_sold_price[sum_product_sold_price["price"] < average_order_value].shape[0]
users_fall_behind = round(users_count / sum_product_sold_price.shape[0] * 100, 2)
print(f"{users_fall_behind}% of users fall below the average order value.")