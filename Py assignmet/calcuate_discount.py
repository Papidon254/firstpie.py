def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        return price

def main():
    try:
        # Prompt the user for the original price and discount percentage
        original_price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))

        # Calculate the final price after applying the discount
        final_price = calculate_discount(original_price, discount_percent)

        # Print the final price after applying the discount
        print("Final price after discount:", final_price)
    except ValueError:
        print("Please enter valid numeric values for the price and discount percentage.")

if __name__ == "__main__":
    main()
