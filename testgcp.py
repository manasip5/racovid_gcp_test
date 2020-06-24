'''
Module to test GCP functionality for RA project on COVID

Usage

import testgcp as tg

timenow()
'''

##--------------------------------------------------##
##          Import libraries
##--------------------------------------------------##


import pandas as pd


def timenow():
    '''
    Function creates a csv file with timestamp
    
    Output:
        Returns a csv file
    '''
    
    #Create data for updating dataframe
    d= {"Time": pd.Timestamp.now()}
    
    df = pd.DataFrame(data=d, index=range(1))

    return df.to_csv("test_gcp.csv", index=False)


if __name__ == "__main__":
    timenow()
