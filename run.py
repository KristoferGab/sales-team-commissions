"""
Program running a companies sales team commissions and salary calculations
"""
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('SalesTeamCommissions')


def get_sales_data():
    """
    Get sales figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated
    by commas. Were the first number is the week of sales given as an
    integer. The loop will repeatedly request data, until it is valid.
    """
    while True:
        print("Please enter sales data from last weeks sales per employee.")
        print("Data should be seven numbers, separated by commas.")
        print("The first number has to be the week of sales.")
        print("The following 6 numbers is the individual sales per employee.")
        print("Example: 1,30,25,24,31,28,25\n")

        data_str = input("Enter your data here:\n")

        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Data is valid!")
            break

    return sales_data


def validate_data(values):
    """
    Function to validate user input. Check for weeknumber by ensuring it is 
    higher than last week. Make sure all values entered are integers and not 
    strings. Also check so that there are 7 values given.
    """
    try:
        [int(value) for value in values]
        if len(values) != 7:
            raise ValueError(
                f"Exactly 7 values required, you provided {len(values)}"
            )
    except ValueError as error:
        print(f"Invalid data: {error}, please try again.\n")
        return False

    return True


def main():
    """
    The main function for running program
    """
    get_sales_data()


main()
