def calculate_price(toppings):
    total_price = 25
    topping_price = {"ไข่มุก": 5, "เฉาก๊วย": 10, "ถั่วแดง": 15, "วิปครีม": 15}
    num_toppings = len(toppings)
    if num_toppings == 0:
        return total_price
    elif num_toppings > 2:
        raise ValueError("Cannot select more than 2 toppings")
    else:
        for topping in toppings:
            if topping not in topping_price:
                raise ValueError(f"Invalid topping: {topping}")
            total_price += topping_price[topping]
        return total_price    