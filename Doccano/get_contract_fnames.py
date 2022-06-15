import os
os.chdir("C:\\Users\\clark.vanlieshout\\Documents\\gsa_text_extract\\")

import pandas as pd
import numpy as np
import glob

calc_df = pd.read_csv(
        "process_contracts/contracts/CALC-pricing-results.csv",
        skiprows=2,
        usecols=["Contract #"],
    ).drop_duplicates()["Contract #"]

def find_contracts(df, number):
    fnames = []
    # corpus = []
    # contracts = []
    for idx, contract in enumerate(np.random.permutation(df)):
        # print(contract) # a check
        try:
            fname = glob.glob("process_contracts/contracts/txt/" + contract + ".*")[0]
            with open(fname, "r", encoding = "utf-8") as f:
                body = f.read()
            # Now, we use regex to clean the text.
            body = body.replace('\n', '  ').replace('\t', '  ').replace('\r', '  ').replace('\xa0', ' ')

            if 500 <= len(body) <= 11000:
                    fnames.append(fname)
                    print(contract)
                # ^ Only small contracts to help loading time (but still > 500 chars)
        except Exception as e:
            if str(e) == "list index out of range": print("Missing contract")
            else: print("File read error: " + str(e))

        if len(fnames) >= number: break
    return (fnames)

# Get 10 short contracts to test-annotate:
fnames = find_contracts(calc_df, 10)
print(fnames)