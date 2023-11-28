# import pandas as pd
# import streamlit as st

# # Load csv 
# data = pd.read_csv('products.csv')

# # Remove commas
# data["Product Prices"] = data["Product Prices"].str.replace(",", "")

# # Remove currency  
# data["Product Prices"] = data["Product Prices"].str.replace("₮", "")

# # Convert to float
# data["Product Prices"] = data["Product Prices"].astype(float)   

# df = pd.DataFrame(data, columns=["Product Names", "Product Prices"])


# # Helper function
# def recommend(df, budget):
#     recommendations = []
#     remaining = budget
    
#     for index, row in df.iterrows():
#         product = row["Product Names"]
#         price = row["Product Prices"]
        
#         if price <= remaining:
#             recommendations.append(product)
#             remaining -= price
            
#     return recommendations, remaining

# # Streamlit app
# st.title("Burger Recommender")
# budget = st.number_input("Enter your budget", value=10000, step=1000)   

# if budget:
#     recs, left = recommend(df, budget)
#     picks = st.multiselect("Choose items", recs)  
    
#     if picks:
#         total = df.loc[df["Product Names"].isin(picks), "Product Prices"].sum()
#         st.write(f"You will pay: {total} ₮")
        
#         remaining_recs, _ = recommend(df, left)
#         st.write("Remaining items:")
#         for item in remaining_recs:
#             st.write("- " + item)



# import pandas as pd
# import streamlit as st

# # Load csv 
# data = pd.read_csv('products.csv')

# # Remove commas
# data["Product Prices"] = data["Product Prices"].str.replace(",", "")

# # Remove currency  
# data["Product Prices"] = data["Product Prices"].str.replace("₮", "")

# # Convert to float
# data["Product Prices"] = data["Product Prices"].astype(float)   

# df = pd.DataFrame(data, columns=["Product Names", "Product Prices"])

# # Streamlit app
# st.title("Burger Recommender")
# budget = st.number_input("Enter your budget", value=10000, step=1000)   

# if budget:
#     below_budget_df = df[df["Product Prices"] <= budget]
    
#     if below_budget_df.empty:
#         st.warning("No products within budget.")
#     else:
#         st.write("Available Products Below Budget:")
#         st.write("---------------")
#         for index, row in below_budget_df.iterrows():
#             st.write(f"- {row['Product Names']}: {row['Product Prices']} ₮")






# import pandas as pd
# import streamlit as st

# # Load csv 
# data = pd.read_csv('products.csv')

# # Remove commas
# data["Product Prices"] = data["Product Prices"].str.replace(",", "")

# # Remove currency  
# data["Product Prices"] = data["Product Prices"].str.replace("₮", "")

# # Convert to float
# data["Product Prices"] = data["Product Prices"].astype(float)   

# df = pd.DataFrame(data, columns=["Product Names", "Product Prices"])

# # Streamlit app
# st.title("_Burger Recommender_")
# budget = st.number_input("Enter your budget", value=10000, step=1000)   

# if budget:
#     remaining_budget = budget
#     selected_products = []
    
#     # Split the layout into two columns
#     left_column, right_column = st.columns(2)
    
#     # Display items on the left side as checkbox selectors
#     left_column.write("Available Products:")
#     left_column.write("---------------")
    
#     # Check if the remaining budget is under 1000
#     if remaining_budget < 1000:
#         left_column.warning("Your budget is too tight. No items can be purchased.")
#     else:
#         for index, row in df.iterrows():
#             # Check if the item's price is within the remaining budget
#             if row["Product Prices"] <= remaining_budget:
#                 selected = left_column.checkbox(f"{row['Product Names']} - {row['Product Prices']} ₮")
#                 if selected:
#                     selected_products.append(row)
#                     remaining_budget -= row['Product Prices']
    
#     # Display the bill on the right side
#     right_column.write("Bill:")
#     right_column.write("---------------")
    
#     total_price = 0
    
#     for selected_product in selected_products:
#         right_column.write(f"- {selected_product['Product Names']}: {selected_product['Product Prices']} ₮")
#         total_price += selected_product['Product Prices']
    
#     right_column.write("---------------")
#     right_column.write(f"Total Price: {total_price} ₮")
#     right_column.write(f"Remaining Budget: {remaining_budget} ₮")
    
#     if remaining_budget < 0:
#         st.warning("Budget fully utilized.")











# import streamlit as st
# import pandas as pd

# # Read data from CSV file
# df = pd.read_csv("products.csv")

# # Convert Product Prices to integers
# df["Product Prices"] = df["Product Prices"].str.replace("₮", "").str.replace(",", "").astype(int)

# # Streamlit app
# st.title("Burger Online Shop")

# # Sidebar for user input
# budget = st.sidebar.number_input("Enter your budget:", min_value=1000, value=1000, step=1000)

# # Ensure minimum budget is 1000
# if budget < 1000:
#     st.warning("Minimum budget is 1000. Please enter a valid budget.")
#     st.stop()

# # Product search
# search_term = st.sidebar.text_input("Search for a product:")
# filtered_products = df[df["Product Names"].str.contains(search_term, case=False) | (df["Product Prices"] <= budget)]

# # Display selected items
# selected_items = st.multiselect("Select items to add to your cart:", filtered_products["Product Names"].tolist())

# # Update cart and display remaining budget
# cart = []
# total_cost = 0

# for item in selected_items:
#     item_price = filtered_products.loc[filtered_products["Product Names"] == item, "Product Prices"].values[0]
#     if total_cost + item_price <= budget:
#         cart.append(item)
#         total_cost += item_price
#     else:
#         st.warning(f"Cannot add {item} to cart. Exceeds budget.")

# # Display cart items
# st.sidebar.title("Your Cart")
# cart_display = "\n".join(cart) if cart else "No items in your cart."
# st.sidebar.text_area("Items in your cart:", cart_display)

# # Ensure remaining budget doesn't go below 0
# remaining_budget = max(budget - total_cost, 0)
# st.sidebar.text(f"Remaining Budget: {remaining_budget} ₮")

# # Display all available items
# st.subheader("Available Items")
# st.table(filtered_products[["Product Names", "Product Prices"]])
















import streamlit as st
import pandas as pd

# Read data from CSV file
df = pd.read_csv("products.csv")

# Convert Product Prices to integers
df["Product Prices"] = df["Product Prices"].str.replace("₮", "").str.replace(",", "").astype(int)

# Initialize session state
if "cart" not in st.session_state:
    st.session_state.cart = set()  # Use a set to store unique items
    st.session_state.total_cost = 0

# Streamlit app
st.title("Burger Web App")

# Sidebar for user input
budget = st.sidebar.number_input("Enter your budget:", min_value=1000, step=1000)

# Filter products based on budget
filtered_products = df[df["Product Prices"] <= budget]

# Display selected items
selected_items = st.multiselect("Select items to add to your cart:", filtered_products["Product Names"].tolist())

# Remove canceled items from the cart
canceled_items = set(st.session_state.cart) - set(selected_items)
for canceled_item in canceled_items:
    item_price = df.loc[df["Product Names"] == canceled_item, "Product Prices"].values[0]
    st.session_state.cart.remove(canceled_item)
    st.session_state.total_cost -= item_price

# Update cart and display remaining budget
for item in selected_items:
    item_price = df.loc[df["Product Names"] == item, "Product Prices"].values[0]
    if st.session_state.total_cost + item_price <= budget:
        st.session_state.cart.add(item)  # Use add() method for sets
        st.session_state.total_cost += item_price
    else:
        st.warning(f"Cannot add {item} to cart. Exceeds budget.")

# Display cart items
st.sidebar.title("Your Cart")
cart_display = "\n".join(st.session_state.cart) if st.session_state.cart else "No items in your cart."
st.sidebar.text_area("Items in your cart:", cart_display)

# Display remaining budget
remaining_budget = budget - st.session_state.total_cost
st.sidebar.text(f"Remaining Budget: {remaining_budget} ₮")

# Display available items that can be afforded with remaining budget
affordable_products = df[df["Product Prices"] <= remaining_budget]
st.subheader("Available Items")
st.table(affordable_products[["Product Names", "Product Prices"]])

# Alert if remaining budget is below 1000
if remaining_budget < 1000:
    st.warning("Your remaining budget is below 1000. You can't buy more products.")







# import streamlit as st
# import pandas as pd

# # Read data from CSV file
# df = pd.read_csv("products.csv")

# # Convert Product Prices to integers
# df["Product Prices"] = df["Product Prices"].str.replace("₮", "").str.replace(",", "").astype(int)

# # Streamlit app
# st.title("Burger Online Shop")

# # Sidebar for user input
# budget = st.sidebar.number_input("Enter your budget:", min_value=1000)

# # Ensure minimum budget is 1000
# if budget < 1000:
#     st.warning("Minimum budget is 1000. Please enter a valid budget.")
#     st.stop()

# # Filter products based on budget
# filtered_products = df[df["Product Prices"] <= budget]

# # Display selected items
# selected_items = st.multiselect("Select items to add to your cart:", filtered_products["Product Names"].tolist())

# # Update cart and display remaining budget
# cart = []
# total_cost = 0

# for item in selected_items:
#     item_price = df.loc[df["Product Names"] == item, "Product Prices"].values[0]
#     if total_cost + item_price <= budget:
#         cart.append(item)
#         total_cost += item_price

# # Remove unselected items from the list
# filtered_products = filtered_products[filtered_products["Product Names"].isin(selected_items)]

# # Remove items with price higher than remaining budget
# remaining_budget = max(budget - total_cost, 0)
# filtered_products = filtered_products[filtered_products["Product Prices"] <= remaining_budget]

# # Display cart items
# st.sidebar.title("Your Cart")
# cart_display = "\n".join(cart) if cart else "No items in your cart."
# st.sidebar.text_area("Items in your cart:", cart_display)

# # Ensure remaining budget doesn't go below 0
# remaining_budget = max(budget - total_cost, 0)
# st.sidebar.text(f"Remaining Budget: {remaining_budget} ₮")

# # Display available items
# st.subheader("Available Items")
# st.table(filtered_products[["Product Names", "Product Prices"]])
