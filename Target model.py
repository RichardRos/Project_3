


import csv

def load_file():
    with open("stock_data.csv", "r") as f:
        csv_file= csv.DictReader(f)
        csv_dict={}
        for line in csv_file:
            key= line["ticker"]
            csv_dict[key]= line

    return csv_dict
def check_targets(tickers, target_gross_range, target_return_range):
    stock_data = load_file()
    meet_criteria = []

    for ticker in tickers:
        ### Converting the strings of the CSV into a Float ###
        gross_profit_margin = float(stock_data[ticker]["gross_profit_margin"])
        return_on_equity = float(stock_data[ticker]["return_on_equity"])

        ### Range of floats check ###
        if target_gross_range[0] <= gross_profit_margin <= target_gross_range[1] and \
                target_return_range[0] <= return_on_equity <= target_return_range[1]:
            meet_criteria.append(stock_data[ticker]["ticker"])

    return meet_criteria


tickers = ["COHR"]
## Variables converted to a float ##
target_gross_range = (-1923534000.0, -1923534000.0)
target_return_range = (-0.05202112219002870, -0.05202112219002870)

check_targets(tickers, target_gross_range, target_return_range)
print(tickers, target_gross_range, target_return_range)