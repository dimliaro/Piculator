# PiCulator - Pi Coin Trading Calculator

## Description
PiCulator is a simple Python-based trading calculator for Pi Coin. It helps users estimate potential profits and losses when selling or buying Pi Coin at different price points. The tool provides two modes:

1. **Selling Mode**: Calculates potential profits/losses if you sell Pi Coin at a given price and buy it back at different lower/higher prices.
2. **Buying Mode**: Calculates potential profits/losses if you buy Pi Coin at a given price and later sell it at different higher/lower prices.

## Features
- Allows users to choose between selling and buying calculations.
- Provides a step-based price variation analysis.
- Customizable depth of analysis.
- Input validation to ensure valid numerical values.

## Requirements
- Python 3.x

## Installation
Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/dimliaro/Piculator.git
cd Piculator
```

## Running the Program
### Method 1: Running as a Python Script
Execute the script using Python:
```bash
python piculator.py
```
Follow the on-screen instructions to input values.

### Method 2: Running in Jupyter Notebook
If you prefer to run it in a Jupyter Notebook:
1. Install Jupyter Notebook if you haven't already:
   ```bash
   pip install notebook
   ```
2. Open Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
3. Create a new notebook and copy-paste the code into a cell.
4. Run the cell and follow the prompts.

## Example Usage
### Selling Mode Example:
```
Enter choice (1/2): 1
Enter the number of Pi you want to sell: 1000
Enter the selling price: 1.50
Enter the step size for price variation: 0.01
Enter the depth of analysis: 10
```

### Buying Mode Example:
```
Enter choice (1/2): 2
Enter the amount in dollars you want to invest: 500
Enter the buying price: 1.20
Enter the step size for price variation: 0.01
Enter the depth of analysis: 10
```

## Contributing
Feel free to submit issues or pull requests for improvements.
## License
This project is the exclusive property of dimliaro. You may use, modify, and distribute this software only with explicit written permission.

