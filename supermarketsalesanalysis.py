# Import the pandas library and alias it as 'pd' for data manipulation and analysis
import pandas as pd

# Import the matplotlib.pyplot library to create various types of plots and visualizations
import matplotlib.pyplot as plt

df=pd.read_csv("C:/Users/sariy/Downloads/supermarket_sales - Sheet1.csv")#reading csv file using pandas


def create_city_gross_income_pie_chart(df):
    # Calculate the total gross income for each city
    city_gross_income = df.groupby('City')['gross income'].sum()

    # Create a pie chart
    plt.figure(figsize=(5, 5))  # Set the figure size (width, height) in inches

    # Create the pie chart
    plt.pie(city_gross_income, labels=city_gross_income.index, autopct="%1.1f%%", startangle=45)

    # Set the title of the pie chart
    plt.title('Gross Income Distribution by City')

    # Add a legend based on the city names
    plt.legend(city_gross_income.index, title='City', loc='upper right')

    # Show the pie chart
    plt.show()

# Define a function to create a bar chart for payment method distribution
def create_payment_method_bar_chart(df):
    # Define a list of colors to be used for the bars in the bar chart
    colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'magenta']

    # Calculate the value counts for the 'Payment' column in the DataFrame
    value_counts = df['Payment'].value_counts()

    # Create a new figure and axis for the bar chart
    ax = value_counts.plot(kind="bar", color=colors)

    # Set the title of the bar chart
    plt.title('Payment Method Distribution')

    # Iterate over the value counts to add labels above each bar in the chart
    for i, v in enumerate(value_counts):
        ax.text(i, v, str(v), ha='center', va='bottom')

    # Display the bar chart
    plt.show()


# Define a function to create a bar chart for total quantity by product line
def create_total_quantity_by_product_line_bar_chart(df):
    # Group the DataFrame by 'Product line', calculate the sum of 'Quantity' for each group,
    # and plot the result as a bar chart
    (df.groupby('Product line').sum()['Quantity']).plot(kind='bar')

    # Set the title of the bar chart
    plt.title('Total Quantity by Product Line')

    # Display the bar chart
    plt.show()
    
def create_monthly_sales_multiline_chart(df):
    df['Month'] = pd.to_datetime(df['Date']).dt.strftime('%b %Y')

    # Get unique product categories
    product_categories = df['Product line'].unique()

    # Create a multiline chart to visualize sales for each product category by month
    plt.figure(figsize=(6, 4))  # Set the figure size (width, height) in inches

    # Plot separate lines for each product category
    for category in product_categories:
        # Filter data for the current category
        category_data = df[df['Product line'] == category]

        # Group the data by 'Month' and sum the 'Total' column
        monthly_sales = category_data.groupby('Month')['Total'].sum()

        # Plot the line for the current category with markers
        plt.plot(monthly_sales.index, monthly_sales.values, label=category, marker='o')

    # Customize the plot
    plt.title('Monthly Sales by Product Category')  # Set the title of the chart
    plt.xlabel('Month')  # Label for the x-axis
    plt.ylabel('Total Sales')  # Label for the y-axis
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.legend()  # Display the legend for product categories

    
    plt.show()# Show the plot


# Call the function to create a pie chart for city gross income using the DataFrame 'df'
create_city_gross_income_pie_chart(df)

# Call the function to create a bar chart for payment method distribution using the DataFrame 'df'
create_payment_method_bar_chart(df)

# Call the function to create a bar chart for total quantity by product line using the DataFrame 'df'
create_total_quantity_by_product_line_bar_chart(df)

# Call the function to create a multiline chart for monthly sales using the DataFrame 'df'
create_monthly_sales_multiline_chart(df)