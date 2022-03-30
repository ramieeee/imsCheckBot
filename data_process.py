import pandas as pd
import numpy as np
import os


if 'data_list.csv' not in os.listdir('./'):
    data = {'IMS_num' : [],
            'About' : [],
            'Date' : [],
            'Comment' : []
    }
    df = pd.DataFrame(data)
    df.to_csv('./data_list.csv')