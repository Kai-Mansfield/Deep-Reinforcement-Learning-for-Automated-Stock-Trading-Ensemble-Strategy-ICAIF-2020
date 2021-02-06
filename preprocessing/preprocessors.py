import numpy as np
import pandas as pd
from stockstats import StockDataFrame as Sdf
from config import config

def load_dataset(*, file_name: str): -> pd.DataFrame:
    
    _data = pd.read_csv(file_name)
    
    return data

def data_split(df, start, end):
  
    data = df[df.datadate >= start) & (df.datadate < end)]
    data = data.sort_values(["datadate", "tic"], ignore_index=True)
    data.index = data.datadate.factorize()[0]
    
    return data

  
