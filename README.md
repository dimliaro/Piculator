# Piculator
A trading calculator for Pi coin. Enter a selling price to see your earnings, then check how much it would cost to buy back the same amount of Pi coins.
# Pi Coin Trading Calculator

## Description
This script allows users to calculate potential profit or loss when trading Pi Coin. It provides two main functionalities:

1. **Process A**: Calculate profit or loss when selling Pi Coin at a given price and buying back at different prices.
2. **Process B**: Calculate profit or loss when buying Pi Coin with a certain amount of dollars and selling at different prices.

Users can customize the step size for price variations and the depth of analysis.

## How to Run the Program

### Requirements
- Python 3 installed on your system

### Steps to Run
1. Download the script (`pi_coin_trading.py`).
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script using:
   ```sh
   python pi_coin_trading.py
   ```
5. Follow the on-screen instructions:
   - Choose **1** for selling Pi Coin (Process A)
   - Choose **2** for buying Pi Coin (Process B)
   - Enter the necessary values when prompted, including step size and depth of analysis.

## Example Usage
### Example 1: Selling Pi Coin
```
Select an option:
1: Calculate profit/loss from selling (Process A)
2: Calculate profit/loss from buying (Process B)
Enter choice (1/2): 1
Enter the step size for price variation: 0.01
Enter the depth of analysis: 10
Enter the number of Pi you own: 1000
Enter the selling price: 1.50
```
This will show potential profit or loss depending on different buy-back prices.

### Example 2: Buying Pi Coin
```
Select an option:
1: Calculate profit/loss from selling (Process A)
2: Calculate profit/loss from buying (Process B)
Enter choice (1/2): 2
Enter the step size for price variation: 0.01
Enter the depth of analysis: 10
Enter the amount in dollars: 1500
Enter the buying price: 1.50
```
This will show potential profit or loss depending on different selling prices.

## Notes
- The script assumes no transaction fees or market fluctuations beyond the given steps.
- The analysis depth and step size can be adjusted as needed.

Enjoy your trading calculations!
