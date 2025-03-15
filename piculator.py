def calculate_profit_loss(start_points, sell_price, step=0.01, depth=10):
    sell_value = round(start_points * sell_price, 4)
    
    print(f"Selling price: {sell_price:.4f}, Total value: {sell_value:.4f}$\n")
     
    print("Profit if you buy back at a lower price:")
    for i in range(1, depth + 1):
        buy_price = round(sell_price - i * step, 4)
        new_units = round(sell_value / buy_price, 4)
        profit = round(new_units - start_points, 4)
        print(f"If you buy at {buy_price:.4f} -> Profit: {profit:.4f} Pi")
    
    print("\nLoss if you buy back at a higher price:")
    for i in range(1, depth + 1):
        buy_price = round(sell_price + i * step, 4)
        new_units = round(sell_value / buy_price, 4)
        loss = round(start_points - new_units, 4)
        print(f"If you buy at {buy_price:.4f} -> Loss: {loss:.4f} Pi")

def calculate_future_value(start_dollars, buy_price, step=0.01, depth=10):
    bought_units = round(start_dollars / buy_price, 4)
    
    print(f"Buying price: {buy_price:.4f}, Pi units acquired: {bought_units:.4f}\n")
    
    print("Profit if you sell at a higher price:")
    for i in range(1, depth + 1):
        sell_price = round(buy_price + i * step, 4)
        sell_value = round(bought_units * sell_price, 4)
        profit = round(sell_value - start_dollars, 4)
        print(f"If you sell at {sell_price:.4f} -> Profit: {profit:.4f}$")
    
    print("\nLoss if you sell at a lower price:")
    for i in range(1, depth + 1):
        sell_price = round(buy_price - i * step, 4)
        sell_value = round(bought_units * sell_price, 4)
        loss = round(start_dollars - sell_value, 4)
        print(f"If you sell at {sell_price:.4f} -> Loss: {loss:.4f}$")

def main():
    print("Select an option:")
    print("1: Calculate profit/loss from selling (Process A)")
    print("2: Calculate profit/loss from buying (Process B)")
    choice = input("Enter choice (1/2): ")
    
    step = float(input("Enter the step size for price variation: "))
    depth = int(input("Enter the depth of analysis: "))
    
    if choice == "1":
        start_points = float(input("Enter the number of Pi you want to sell: "))
        sell_price = float(input("Enter the selling price: "))
        calculate_profit_loss(start_points, sell_price, step, depth)
    elif choice == "2":
        start_dollars = float(input("Enter the amount in dollars you want to buy: "))
        buy_price = float(input("Enter the buying price: "))
        calculate_future_value(start_dollars, buy_price, step, depth)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()




