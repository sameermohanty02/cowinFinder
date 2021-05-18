import pandas as pd

def get_dataobj(csv_name, csv_data):
    data = pd.read_csv(csv_name)
    for obj in data.values:
        if str(csv_data) in obj:
            dist = obj
            return dist
        else:
            dist = None
    return dist
