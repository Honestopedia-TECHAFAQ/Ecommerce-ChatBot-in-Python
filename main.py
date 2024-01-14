import streamlit as st

# Mock data for product recommendations
product_recommendations = {
    "electronics": ["Laptop", "Smartphone", "Headphones"],
    "clothing": ["T-shirt", "Jeans", "Sneakers"],
    "books": ["Python Crash Course", "The Art of War", "To Kill a Mockingbird"]
}

def main():
    st.title("E-commerce Chatbot")

    # User input box
    user_input = st.text_input("You:", "")

    # Bot response
    bot_response = get_bot_response(user_input)

    # Display bot response
    st.text_area("Bot:", bot_response, height=100)

def get_bot_response(user_input):
    # Simple rule-based responses
    if "hello" in user_input.lower():
        return "Hi there! How can I assist you today?"
    elif "product" in user_input.lower():
        return "We have a variety of products available. What category are you interested in? (e.g., electronics, clothing, books)"
    elif any(category in user_input.lower() for category in product_recommendations.keys()):
        category = next((category for category in product_recommendations.keys() if category in user_input.lower()), None)
        recommendations = product_recommendations.get(category, [])
        return f"Here are some {category} recommendations: {', '.join(recommendations)}"
    elif "order" in user_input.lower():
        return "If you have any questions about your order, please provide your order number."
    elif "add to cart" in user_input.lower():
        # Simple shopping cart functionality
        product = user_input.split("add to cart ")[1]
        add_to_cart(product)
        return f"{product} has been added to your cart. You can view your cart by asking 'View my cart'."
    elif "view my cart" in user_input.lower():
        cart_contents = get_cart_contents()
        return f"Your shopping cart contains: {', '.join(cart_contents)}" if cart_contents else "Your shopping cart is empty."
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask another question?"

def add_to_cart(product):
    if "cart" not in st.session_state:
        st.session_state.cart = []
    st.session_state.cart.append(product)

def get_cart_contents():
    return st.session_state.cart if "cart" in st.session_state else []

if __name__ == "__main__":
    main()
