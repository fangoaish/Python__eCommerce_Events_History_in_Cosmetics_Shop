# eCommerce Events History in Cosmetics Shop

## Project Overview
This project aims to analyze the 2020-January eCommerce Events History in Cosmetics Shop data from [kaggle](https://www.kaggle.com/datasets/mkechinov/ecommerce-events-history-in-cosmetics-shop/data?select=2019-Dec.csv) to deep-dive into how customer journeys offer valuable insights into user engagement with digital assets and marketing campaigns. Leveraging this information can enhance the user experience, drive increased website traffic, and ultimately contribute to higher sales and revenue.

![image](https://github.com/fangoaish/Python__eCommerce-Events-History-in-Cosmetics-Shop/assets/51399519/42c7120a-9426-4cd1-8da0-88e63b6fdad2)


## Business Objectives

The main objective of this analysis is to scrutinize the store's key performance indicators, extracting actionable insights to inform strategic decisions. Explore opportunities within the data to contribute to **_enhancing the store's revenue and performance goals_**. The ultimate goal is to provide actionable intelligence for optimizing operational efficiency and fostering sustained growth.


## Data Sources
This dataset is provided from [kaggle](https://www.kaggle.com/datasets/mkechinov/ecommerce-events-history-in-cosmetics-shop/data?select=2019-Dec.csv)

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

### _1) Consumer Preferences_
- #### **Q:** Does a correlation exist between revenue and reviews?
    - Why do I want to know? 
        - Explore the strength of any correlation that may exist between a product's revenue and its reviews
    - So what?     
        - Implement initiatives to encourage and incentivize customer reviews, fostering increased engagement and potentially driving higher revenues through positive customer feedback
    - Measure by?
        - revenue // reviews

- #### **Q:** Is there an influence on a product's rating and reviews based on the length of its description?
    -  Why do I want to know?
        - Explore the potential impact of product description length on customer ratings and reviews, addressing the relationship between product information and consumer perception.
    - So what?
        - If positive, highlight product features within the optimal description length to attract and engage customers effectively
    - Measure by?
        - description // reviews // rating
     
### _1) Consumer Preferences - Findings_
1. A correlation coefficient of 0.65 could be interpreted as either a "good" or "moderate" correlation. Therefore, there is a positive correlation between revenue and reviews, suggesting that products with higher reviews tend to generate higher revenue.
2. The correlation coefficient of 0.73 indicates the strength and direction of the linear relationship between description length and the average rating.
     
![Correlation between Revenue and Reviews](https://github.com/fangoaish/Python__Analysis-of-Sportswear-Product-Sales-Adidas-vs.-Nike/assets/51399519/43de922e-bb14-4e04-8ed0-9638154a2c54)

![Correlation Between Description Length and Mean Rating](https://github.com/fangoaish/Python__Analysis-of-Sportswear-Product-Sales-Adidas-vs.-Nike/assets/51399519/23ff228c-94d6-49e5-8190-ec332522cdb2)


### _1) Consumer Preferences - Recommendations_
- Leverage the positive correlation observed between revenue and reviews to enhance marketing strategies, emphasizing the importance of customer reviews in promotional campaigns and product positioning.
- Consider optimizing product descriptions to a length that resonates well with customers. This could potentially lead to higher average ratings.



### _2) Product Offerings_
- #### **Q:** Do Nike and Adidas offer differing discount amounts?
    - Why do I want to know? 
        - Aim to investigate and compare the discount strategies employed by Nike and Adidas, providing insights into their promotional approaches.
    - So what?
        - Navigate the complexities of differing discount amounts, optimizing their strategies to achieve a balance between attracting customers, maintaining brand value, and sustaining profitable operations
    - Measure by?
        - brand // discount


- #### **Q:** What distinguishes the price points between Nike and Adidas products?
    - Why do I want to know?: 
        - Focus on understanding the comparative pricing strategies of Nike and Adidas, exploring the differences in their product price points.
    - So what? 
        - Analyze how the variations in price points may impact consumer perception, market positioning, and business strategies for Nike and Adidas
    - Measure by?
        - brand // listing_price


### _2) Product Offerings - Findings_

First, the number of offered discounts by Adidas is **5 times higher** than the ones offered by Nike. Second, both brands offer products in all price categories, but Adidas has a higher number of products in every category compared to Nike. Additionally, it reveals that the _**"Premium" category**_ has the highest average revenue. These findings suggest that Nike and Adidas have distinct price points and the amount of offered discounts for their products, with Adidas offering a higher number of products across price points and potentially generating higher average revenue.


![Distribution of Offered Discount Amounts between Adidas and Nike](https://github.com/fangoaish/Python__Analysis-of-Sportswear-Product-Sales-Adidas-vs.-Nike/assets/51399519/0b5bfc01-4bdd-4b17-a874-a0f43df0dced)

![Number of Different Products by Price Category between Adidas and Nike](https://github.com/fangoaish/Python__Analysis-of-Sportswear-Product-Sales-Adidas-vs.-Nike/assets/51399519/d0d04744-dfc4-46db-828d-1bb2540aaf8d)

![Average Revenue by Price Category between Adidas and Nike](https://github.com/fangoaish/Python__Analysis-of-Sportswear-Product-Sales-Adidas-vs.-Nike/assets/51399519/469f76fc-5173-43c1-ada9-843f919c3be6)


### _2) Product Offerings - Recommendations_
- Analyze Nike's discount ratio in comparison to Adidas and explore opportunities to optimize discount strategies, ensuring they align with market dynamics while maintaining brand value.
- Evaluate and diversify the product categories to compete more effectively with Adidas, addressing potential gaps and increasing market share.


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
