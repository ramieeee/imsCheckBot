import pandas as pd
import os

class DataControl:
    def __init__(self):
        # check if data_list.csv exists in the current dir
        if 'data_list.csv' not in os.listdir('./'):
            data = {'IMS_num' : [],
                    'About' : [],
                    'Date' : [],
                    'IMS_Comment' : [],
                    'Update_check' : []
            }
            df = pd.DataFrame(data)
            df.to_csv('./data_list.csv')
            print('Created new csv file')
    
    def data_disp(self):
        df = pd.read_csv('./data_list.csv', index_col=0) # index_col eliminates unnamed: 0 column
        print(df)
    
    def data_add(self, num, about, date, comment, update_check):
        df = pd.read_csv('./data_list.csv', index_col=0) # index_col eliminates unnamed: 0 column
        
        # check if IMS num alread exists
        if num in list(df['IMS_num']):
            print('**IMS number already exists**')
            return

        data = {"IMS_num" : num,
                "About" : about,
                "Date" : date,
                "IMS_Comment" : comment,
                "Update_check" : update_check}
        df = df.append(data, ignore_index=True)
        print(df)
        df.to_csv('./data_list.csv')
        print('Data successfully added')
        print(len(df['IMS_num']))
    
    def data_del(self, num):
        df = pd.read_csv('./data_list.csv', index_col=0) # index_col eliminates unnamed: 0 column

        # check if IMS num exists
        if num not in list(df['IMS_num']):
            print('**IMS number does not exist**')
            return
        
        # execute deletion
        index_names = df[df['IMS_num'] == num].index
        df.drop(index_names, inplace=True)
        df.to_csv('./data_list.csv')
        print('Data successfully deleted')