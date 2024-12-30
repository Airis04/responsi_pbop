# Cashier System

This is a simple cashier system application designed for small stores. It provides functionalities for product management, transaction processing, and exporting transaction data to Excel. The application is built using Python's Tkinter library for the GUI and connects to a MySQL database named "responsi_npm".

## Features

- **Product Management**: 
  - Add, edit, delete, and view products.
  
- **Transaction Processing**: 
  - Select products, input quantities, calculate total prices, and save transactions to the database.
  
- **Export to Excel**: 
  - Export transaction data to an Excel file for reporting and analysis.

## Project Structure

```
cashier-system
├── src
│   ├── __init__.py
│   ├── app.py
│   ├── database.py
│   ├── gui
│   │   ├── __init__.py
│   │   ├── main_window.py
│   │   ├── product_management.py
│   │   └── transaction_processing.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── product.py
│   │   └── transaction.py
│   └── utils
│       ├── __init__.py
│       └── export_to_excel.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Install Dependencies**: 
   - Ensure you have Python installed. 
   - Install the required packages listed in `requirements.txt` using pip:
     ```
     pip install -r requirements.txt
     ```

2. **Database Setup**: 
   - Create a MySQL database named `responsi_npm`.
   - Ensure the necessary tables for products and transactions are created as defined in `database.py`.

3. **Run the Application**: 
   - Execute the main application file:
     ```
     python src/app.py
     ```

## Usage Guidelines

- Launch the application to access the main window.
- Use the product management features to maintain your inventory.
- Process transactions through the transaction processing interface.
- Export transaction data to Excel for further analysis.

## License

This project is open-source and available for modification and distribution under the MIT License.