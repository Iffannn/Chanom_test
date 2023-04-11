from calculate_price import calculate_price

if __name__ == "__main__":
    print("Welcome to IFFAN's Boba Shop!")
    print("Here are our available toppings and their prices:")
    print("- ไข่มุก: 5 บาท")
    print("- เฉาก๊วย: 10 บาท")
    print("- ถั่วแดง: 15 บาท")
    print("- วิปครีม: 15 บาท")
    toppings_input = input("Please enter your selected toppings (separated by commas, e.g. ไข่มุก,เฉาก๊วย): ").strip()
    if not toppings_input:
        total_price = 25
        print("Your total price is:", total_price, "บาท")
    else:
        toppings_list = toppings_input.split(",")
        try:
            total_price = calculate_price(toppings_list)
            print("Your total price is:", total_price, "บาท")
        except ValueError as e:
            print("Error:", e)