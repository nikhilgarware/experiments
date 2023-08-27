import pandas as pd
import matplotlib.pyplot as plt


pd.options.mode.chained_assignment = None  # default='warn'

columns_to_check = ["DATE", "NARRATION", "CHQ.NO.", "WITHDRAWAL(DR)", "DEPOSIT(CR)", "BALANCE(INR)"]
columns_to_convert_to_float = ["DEPOSIT(CR)", "BALANCE(INR)"]


def menu_selection():
    print("Select operation to perform")
    print("1 - Plot Transaction Records")
    print("2 - Analyze Transaction")
    print("3 - Date Selection")
    choice = int(input("Select the choice "))
    if choice == 1:
        plot_line_chart()
    if choice == 2:
        analyse_transactions()
    if choice == 3:
        analyze_data_for_specific_date("2023-01-01", "2023-01-30")


def read_transaction_records_and_clean_data():
    data_frame = pd.read_excel('data/large.xls')
    updated_dataframe = data_frame[columns_to_check]
    updated_dataframe["DATE"] = pd.to_datetime(updated_dataframe["DATE"],dayfirst=True)
    # removing cr from sheet
    updated_dataframe["BALANCE(INR)"] = updated_dataframe["BALANCE(INR)"].str.rstrip("_Cr")

    # converting string to float for mathemetical operations
    updated_dataframe["BALANCE(INR)"] = (updated_dataframe["BALANCE(INR)"].str.split()).apply(
        lambda x: float(x[0].replace(',', '')))
    # appending 0 where transaction are null
    updated_dataframe["DEPOSIT(CR)"] = updated_dataframe["DEPOSIT(CR)"].fillna(0)
    # converting string to float
    updated_dataframe["DEPOSIT(CR)"] = updated_dataframe["DEPOSIT(CR)"].replace(',', '', regex=True).astype(float)

    # appending 0 where transaction are 0
    updated_dataframe["WITHDRAWAL(DR)"] = updated_dataframe["WITHDRAWAL(DR)"].fillna(0)
    # converting string to float
    updated_dataframe["WITHDRAWAL(DR)"] = updated_dataframe["WITHDRAWAL(DR)"].replace(',', '', regex=True).astype(float)
    # plotting line chart

    return updated_dataframe


def analyze_data_for_specific_date(start_date, end_date):
    data_frame = read_transaction_records_and_clean_data()
    #under development
    print(data_frame)

def plot_line_chart():
    data_frame = read_transaction_records_and_clean_data()
    data_frame.plot(kind="line")
    plt.show()


def analyse_transactions():
    records = read_transaction_records_and_clean_data()
    # printing analysis
    print("Total Income", records["DEPOSIT(CR)"].sum())
    print("Total Expense", records["WITHDRAWAL(DR)"].sum())
    print("Balance", records["DEPOSIT(CR)"].sum() - records["WITHDRAWAL(DR)"].sum() + 13488)
    print("Total Transaction", records["DATE"].count())


if __name__ == '__main__':
    menu_selection()
