import pandas as pd
import os

class DataControl:
    def __init__(self):
        # check if data_list.csv exists in the current dir
        if 'data_list.csv' not in os.listdir('./'):
            print('\nSystem: No data_list.csv file in dir. Creating new file')
            data = {'IMS_num' : [],
                    'Title' : [],
                    'Date' : [],
                    'Update_check' : []
            }
            df = pd.DataFrame(data)
            df.to_csv('./data_list.csv')
            print('\nSystem: Successfully created data_list.csv')
    
    def data_disp(self):
        df = pd.read_csv('./data_list.csv', index_col=0) # index_col eliminates unnamed: 0 column
        print()
        print(df)
    
    def data_add(self, num, title, date):
        df = pd.read_csv('./data_list.csv', index_col=0)
        
        # check if IMS num alread exists
        if num in list(df['IMS_num']):
            print('\nSystem: IMS number already exists')
            return

        # execute addition
        data = {"IMS_num" : num,
                "Title" : title,
                "Date" : date,
                "Update_check" : 'N'}
        df = df.append(data, ignore_index=True)
        df.to_csv('./data_list.csv')
        print('\nSystem: Data successfully added')
    
    def data_del(self, num):
        if num == '':
            print('\nSystem: Empty input')
            return
        df = pd.read_csv('./data_list.csv', index_col=0)

        # check if IMS num exists
        if int(num) not in list(df['IMS_num']):
            print('\nSystem: IMS number does not exist')
            return
        
        # execute deletion
        index_names = df[df['IMS_num'] == int(num)].index
        df.drop(index_names, inplace=True)
        df.to_csv('./data_list.csv')
        print('\nSystem: Data successfully deleted')