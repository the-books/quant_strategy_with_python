import pandas as pd

def make_code(x):
    x = str(x)
    return 'A' + '0'*(6 - len(x)) + x

def make_stocks(path):
    code_data = pd.read_csv(path, sep='\t')
    code_data['종목코드'] = code_data['종목코드'].apply(make_code)

    return code_data
