def calculate_discount(price, discount_percentage):
    if  discount_percentage > 20:
        return price * (1 - discount_percentage / 100)
    else:
        return price 
print(calculate_discount(100, 25) ) # Example usage