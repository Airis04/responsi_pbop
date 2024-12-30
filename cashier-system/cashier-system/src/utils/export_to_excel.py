import pandas as pd
from datetime import datetime

def export_transactions_to_excel(transactions, file_name='transactions.xlsx'):
    """Export transaction data to an Excel file."""
    if not transactions:
        print("No transactions to export.")
        return

    # Create a DataFrame from the transactions list
    df = pd.DataFrame(transactions, columns=['Product Name', 'Quantity', 'Total Price', 'Date'])

    # Save the DataFrame to an Excel file
    try:
        df.to_excel(file_name, index=False)
        print(f"Transactions exported successfully to {file_name}")
    except Exception as e:
        print(f"Error exporting transactions: {e}")