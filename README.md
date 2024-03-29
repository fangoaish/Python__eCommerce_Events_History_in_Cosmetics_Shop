# eCommerce Events History in Cosmetics Shop

## Project Overview
This project aims to analyze the 2020-January eCommerce Events History in Cosmetics Shop data from [kaggle](https://www.kaggle.com/datasets/mkechinov/ecommerce-events-history-in-cosmetics-shop/data?select=2019-Dec.csv) to deep-dive into how customer journeys offer valuable insights into user engagement with digital assets and marketing campaigns. Leveraging this information can enhance the user experience, drive increased website traffic, and ultimately contribute to higher sales and revenue.

![image](https://github.com/fangoaish/Python__eCommerce-Events-History-in-Cosmetics-Shop/assets/51399519/42c7120a-9426-4cd1-8da0-88e63b6fdad2)


## Business Objectives

The main objective of this analysis is to scrutinize the store's key performance indicators, extracting actionable insights to inform strategic decisions. Explore opportunities within the data to contribute to **_enhancing the store's revenue and performance goals_**. The ultimate goal is to provide actionable intelligence for optimizing operational efficiency and fostering sustained growth.


## Data Sources
This dataset is provided from [kaggle](https://www.kaggle.com/datasets/mkechinov/ecommerce-events-history-in-cosmetics-shop/data?select=2019-Dec.csv)


## Data Preparation
Currently, this raw_events_data stores all of the information from products, website sessions, and website events. Unfortunately, the way this raw data is structured leads to a lot of redundant data being stored, thus making our analysis a lot slower and making it harder for us to make sense of the data.

So before I began looking for insights, I transformed this big clunky raw data into 3 smaller ones by applying a few normalizing principles.

- **products**:
    - product_id
    - category_code
    - brand
    - price
- **users**:
    - user_id
    - user_session
- **events**:
    - event_time
    - event_type
    - product_id
    - user_session
```ruby
# Create products table
products = raw[["product_id", "category_code", "brand", "price"]].drop_duplicates()
print(products)

# Creat users table
users = raw[["user_id", "user_session"]].drop_duplicates()
print(users)

# Creat events talbe
events = raw[["event_time", "event_type", "product_id", "user_session"]].drop_duplicates()
print(events)
```

## Analysis Framework
**Objective**: Increase the cosmetics shop's total sales revenue and performance goals.

- Sales Revenue ($) = **_# of Units Sold_** x Avg. Selling Price

    
Business opportunities to increase the number of Units Sold:
1. Increase customers (acquire new customers + retain existing customers)
2. Increase order frequency (more orders per person per month)
3. Increase order value (more products per order)

(**Note**: In this analysis, the focus is only on how to increase sales volume, so the strategy for selling price is not included.)


## Exploratory Data Analysis
Before diving into the data sea, I'll categorize the hypotheses systematically based on our goal, establishing a structured and logical framework for thoughtful analysis.

### _1) Opportunity 1: Increase more customers_
- #### 1-1. Acquiring new customers
    - What do I want to know?
        - The best-selling products
    - Why do I want to know? 
        - Knowing the best-selling products indicates the highest demand
    - So what?     
        - The best-selling products with high demand can guide the allocation of marketing and advertising spend/effort to acquire new users and sustain existing momentum
    - Measured by?
        - event_type // product_id // price
     
- #### 1-2. Retaining existing customers
    - What do I want to know?
        -  Overall conversion rate
        -  Cart abandonment rate per user
    - Why do I want to know?
        - The shopping cart abandonment rate is the overall percentage of shoppers who added some items to the cart but abandoned it before purchase, depicting potential customers who were able to reach the end of the funneling model but gave up due to some reason.
    - So what?
        - A heightened abandonment rate might signal a less streamlined checkout experience, increased shipping costs, ineffective remarketing promotions, or the absence of a guest check-out option. By addressing the purchasing flow issues and improving the customer experience, we can turn lost sales into fresh opportunities.
    - Measured by?
        - Conversion Rate = Number of Conversions / Total Number of Visitors
        - Cart Abandonment Rate = 1 - Cart Conversion Rate (Conversion Rate = Number of Conversions / Shopping Carts Created)
        - event_type // user_id
     
     
![Top 10 Best Selling Products](https://github.com/fangoaish/Python__eCommerce-Events-History-in-Cosmetics-Shop/assets/51399519/2578e789-4226-40fb-bf75-b714dad86f29)

![Distribution of events](https://github.com/fangoaish/Python__eCommerce-Events-History-in-Cosmetics-Shop/assets/51399519/c2aa58f1-8fe7-4e68-9002-8161f05c54c6)


### _2) Opportunity 2: Increase order frequency_
- What do I want to know?
  -  Customer behavior -> What time does order volume tend to be high?
- Why do I want to know?
  - To identify the most popular time when people complete their orders and the average purchase number per user.
- So what?
  - By knowing the time when order volume is high, we can send email or push notifications around that time to further incentivize users to complete their purchase at that specific time.
- Measured by?
  - event_type (view, cart, purchase) // event_time (weekday & hour)
    

### _2) Opportunity 2: Increase order frequency - Findings_

The view and cart events per hour in a day have reached their peak at around **6 p.m. - 8 p.m.** with a near plateau in the morning between **8 a.m. - 12 p.m.** On the other hand, the purchase event reached its peak around **9 a.m. to 12 p.m.** and gradually decreased afterward until its second peak at roughly **6 p.m. - 7 p.m.** It's obvious that the weekday has a strong effect on customers buying behavior: the numbers of view and cart events are higher from Tuesday to Thursday, while purchase events have higher numbers on **Sunday and Monday**.

![Event Counts per Hour](https://github.com/fangoaish/Python__eCommerce-Events-History-in-Cosmetics-Shop/assets/51399519/130d1817-d28f-4fbf-a090-5265d9679838)

![Event Counts per Weekday](https://github.com/fangoaish/Python__eCommerce-Events-History-in-Cosmetics-Shop/assets/51399519/30a32d73-e7d8-4465-b534-1048cb593d27)



### _2) Opportunity 2: Increase order frequency - Recommendations_
Suggestions: By knowing the popular time and average number of purchases per user, we can introduce email marketing re-targeting to customers in view and cart events and offer promotional coupons for discounts. Offer free shipping for total purchases crossing a threshold and provide guest checkout functions with easy access to payment gateways.


### _3) Opportunity 3: Increase order value_
- What do I want to know?
    - Customer behavior -> What is the average order value?
- Why do I want to know? 
    - Incentivize users whose order value is less than the average to order more products.
- So what?
    - suggestions:
        1. Set up a free shipping threshold
        2. Bundle complementary products
        3. Make time-sensitive offers
- Measured by?
    -  event_type // user_session // price


### _3) Opportunity 3: Increase order value - Findings_

- The Average Order Value of each purchase is: 43.03$!
- 63.89% of users fall below the average order value.

## Key Recommendations
1. **Increase customers**: Increase marketing/advertising efforts in the best-selling products, while optimizing purchasing flow issues and improving the customer experience to drive acquisition and retention.
    - Increase marketing/advertising efforts in the best-selling products to acquire new users given its high demand and revenue.
    - Conduct a deep-dive in checkout experience, increased shipping costs, ineffective remarketing promotions, or the absence of a guest check-out option to improve the customer experience.
2. **Increase order frequency**: Leverage communication capabilities (promotion email, push notifications) to increase order frequency.
    - Send email/push notifications around two order peak time( 9AM - 12PM, 6PM - 7PM) on Sunday and Monday to increase order frequency.
3. **Increase order value**: Test benefits/promotions to increase average order value 
    - Incentivize users: whose avo falls below 43.03$ via benefits/promotions to increase the number of products sold per order.


## Chanllenge

The challenge in this coding task lies in converting numeric indices representing days of the week (0-6) into their corresponding day names (Monday-Sunday) within a pandas DataFrame. Initially, the DataFrame's index defaults to numeric values, making it less intuitive to interpret at a glance. 

To address this, I utilize the ***map() function*** provided by pandas. By leveraging a dictionary named weekdays_index, which maps numeric indices to their respective day names, I employ the ***map() function*** to iterate through the DataFrame's index and replace each numeric index with its corresponding day name. 

This approach seamlessly transforms the DataFrame's index into a more descriptive format, facilitating easier interpretation and analysis of the data based on the days of the week. Ultimately, by employing ***index.map()***, the code efficiently resolves the challenge of converting numeric indices into their corresponding day names within the DataFrame.

```ruby
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
```


## Limitations
**Neglect of Pricing Strategy**: By excluding pricing strategy from the analysis, there is a limitation in understanding how price elasticity affects sales volume. Different pricing strategies could impact consumer behavior and ultimately affect sales volume. Ignoring this aspect may lead to missed opportunities for revenue optimization.

**Incomplete Revenue Optimization**: Focusing solely on increasing sales volume without considering pricing strategies may overlook potential avenues for revenue optimization. Maximizing revenue involves a combination of increasing sales volume and optimizing pricing to achieve the highest possible profit margin.

