import streamlit as st
import pandas as pd

def load_and_harmonize_financial_data(file_path, file_type, sep='|', encoding='latin1'):
    """
    Loads and harmonizes various financial data formats into a standardized pandas DataFrame.

    Args:
        file_path (str): The path to the financial data file.
        file_type (str): The type of the financial file (e.g., 'fec', 'balance_sheet', 'income_statement').
        sep (str): The separator used in the file (default: '|').
        encoding (str): The encoding of the file (default: 'latin1').

    Returns:
        pd.DataFrame: A standardized DataFrame containing the financial data.
    """

    df = pd.DataFrame()

    if file_type == 'fec':
        # Load FEC file, ensuring specific columns are correctly typed
        df = pd.read_csv(file_path, sep=sep, encoding=encoding, dtype={'CompteNum': str})

        # Clean column names by stripping whitespace
        df.columns = df.columns.str.strip()

        # Standardize FEC specific columns to a common naming convention if desired
        # For this example, we will keep original names for now but clean and process values.
        # Example of mapping if needed:
        # column_mapping = {
        #     'CompteNum': 'AccountCode',
        #     'CompteLib': 'AccountDescription',
        #     'Debit': 'DebitAmount',
        #     'Credit': 'CreditAmount',
        #     'EcritureDate': 'TransactionDate'
        # }
        # df.rename(columns=column_mapping, inplace=True)

        # Convert 'Credit' and 'Debit' to float after replacing comma with dot
        # Handle potential missing values before conversion
        df['Credit'] = df['Credit'].replace({',': '.'}, regex=True).astype(float)
        df['Debit'] = df['Debit'].replace({',': '.'}, regex=True).astype(float)

        # Calculate 'Solde' (Credit - Debit)
        df['Solde'] = df['Credit'] - df['Debit']

    elif file_type == 'balance_sheet':
        # Placeholder for balance sheet loading and harmonization
        df = pd.read_csv(file_path, sep=sep, encoding=encoding)
        df.columns = df.columns.str.strip()
        print(f"Warning: Balance Sheet harmonization not fully implemented. Loaded data from {file_path}.")
        # Example: Map balance sheet specific columns to a unified schema
        # df.rename(columns={'OriginalBalanceColumn': 'Amount', 'OriginalAccountColumn': 'AccountCode'}, inplace=True)
        # Further processing like calculating Solde might not be directly applicable for balance sheets depending on format

    elif file_type == 'income_statement':
        # Placeholder for income statement loading and harmonization
        df = pd.read_csv(file_path, sep=sep, encoding=encoding)
        df.columns = df.columns.str.strip()
        print(f"Warning: Income Statement harmonization not fully implemented. Loaded data from {file_path}.")
        # Example: Map income statement specific columns to a unified schema
        # df.rename(columns={'OriginalRevenueColumn': 'Revenue', 'OriginalExpenseColumn': 'Expense'}, inplace=True)

    else:
        raise ValueError(f"Unsupported file_type: {file_type}. Supported types are 'fec', 'balance_sheet', 'income_statement'.")

    return df

print("Function 'load_and_harmonize_financial_data' defined.")