def calculate_discount(price, customer_type):
    if price < 0:
        raise ValueError("Price cannot be negative")
    
    if customer_type == "regular":
        discount = 0.05  # Regular customers get a 5% discount
    elif customer_type == "premium":
        discount = 0.10  # Premium customers get a 10% discount
    elif customer_type == "vip":
        discount = 0.20  # VIP customers get a 20% discount
    else:
        discount = 0  # No discount for other types of customers

    final_price = price - (price * discount)
    return final_price