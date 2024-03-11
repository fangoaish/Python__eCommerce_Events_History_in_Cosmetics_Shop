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

![Event Counts per Weekday](https://github.com/fangoaish/Python__eCommerce-Events-History-in-Cosmetics-Shop/assets/51399519/c8841963-7c89-4faa-b0d6-3b7687ab685d)


### _2) Opportunity 2: Increase order frequency - Recommendations_
Suggestions: By knowing the popular time and average number of purchases per user, we can introduce email marketing re-targeting to customers in view and cart events and offer promotional coupons for discounts. Offer free shipping for total purchases crossing a threshold and provide guest checkout functions with easy access to payment gateways.


### _3) Financial Performance_
- #### **Q:** How do the product categories contribute to the company's revenue? 
    - Why do I want to know? 
        - To evaluate the financial performance of different product categories and understand their contribution to overall revenue.
    - So what?
        - This information can help in adjusting inventory management strategies based on insights from each product category

- #### **Q:** How does the median revenue differ across product categories?
    - Why do I want to know? 
        - To compare the median revenue generated by different categories.
    - So what?
        - This comparison can help optimize marketing and sales efforts based on the relative performance of each category

### _3) Financial Performance - Findings_

- Contribution to Company Revenue:

Footwear dominates the company's revenue, accounting for a substantial 84.7% of the total. This suggests a strong market demand for footwear products, indicating a potential area for further investment and strategic focus.
Clothing, while contributing 15.3%, is notably lower in comparison. It's important to assess the reasons behind this lower contribution and explore opportunities for growth in the clothing segment.

![Total Number of Products Sold by Product Category](https://github.com/fangoaish/Python__Analysis-of-Sportswear-Product-Sales-Adidas-vs.-Nike/assets/51399519/b07af180-98d0-4fa5-a820-8eb875961e82)





- Median Revenue Disparity:

The median revenue for footwear is significantly **four times higher** compared to clothing. This implies that, on average, each sale in the footwear category brings in more revenue compared to the clothing category.
The wide gap in median revenue raises questions about the pricing strategy, customer preferences, and market positioning for both product categories.

![Comparison of Median Revenue - Footwear vs Clothing](https://github.com/fangoaish/Python__Analysis-of-Sportswear-Product-Sales-Adidas-vs.-Nike/assets/51399519/c058d361-2949-45f0-9da1-aff9a137a02a)


### _3) Financial Performance - Recommendations_
Given that footwear is the primary revenue driver, it is advisable to continue investing in this category. Explore opportunities to expand the footwear product line, introduce new styles, and leverage market trends to maintain or increase its market share.

While clothing contributes less to the overall revenue, it remains a valuable part of the business. Consider strategies to diversify the clothing portfolio, perhaps by introducing new designs, collaborating with influencers or designers, or identifying untapped market segments to increase its market presence.

## Challenges
The challenge was to determine the proportion of footwear products of both brands from their clothing counterparts without a specific product type column. Initially, I generated a keyword string to filter relevant rows from our primary DataFrame. Subsequently, I established a counter DataFrame to preserve data whose product IDs are absent from our initial subset, facilitating the differentiation between the two categories of sportswear.
```ruby
# 3) Financial Performance:
# 1) Q: How much of the company's stock consists of footwear items? 

# There is no column stating the type of product, so I need to rely on the "description" column
# Challenge: pattern matching -> wildcard -> https://docs.python.org/3/library/re.html#regular-expression-syntax
footwear_keyword = "shoe*|trainer*|foot*"

# Filter for footwear products
shoes = merged_df[merged_df["description"].str.contains(footwear_keyword)]

# Filter for clothing products
# How to Filter Pandas DataFrame Using Boolean Columns https://www.statology.org/pandas-filter-by-boolean-column/
clothing = merged_df[~merged_df.isin(shoes["product_id"])]
```

## Limitations
- The reliability of the findings and the efficacy of the proposed recommendations depend on the quality of the datasets provided.
- Please be aware that our merged DataFrame contains aggregated sales data for each specific product.
- Additionally, the recency of all the data remains unknown due to the absence of a datetime parameter in the datasets.

## References
- [DataCamp](https://www.datacamp.com/)
- [Statista](https://www.statista.com/statistics/254489/total-revenue-of-the-global-sports-apparel-market/)
