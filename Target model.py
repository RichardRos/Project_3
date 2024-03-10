import csv

def load_file():
    with open("stock_data.csv", "r") as f:
        csv_file= csv.DictReader(f)
        csv_dict={}
        for line in csv_file:
            key= line["ticker"]
            csv_dict[key]= line

    return csv_dict
def check_targets(tickers, targets):
    stock_data = load_file()
    meet_criteria= []
    for ticker in tickers:
        if stock_data[ticker]["gross_profit_margin"] == targets[0] and \
                stock_data[ticker]["return_on_equity"] == targets[1]:
            meet_criteria.append(stock_data[ticker]["ticker"])
    return meet_criteria

tickers= ["SUMCF", "NOVT", "SUOPY"]
target_gross_profit_margin= '-209439000000.0'
target_return_on_equity= '0.11165661113402639'
meet_criteria= check_targets(tickers, [target_gross_profit_margin,target_return_on_equity])
print(meet_criteria)