import pandas as pd
import os

class DataControl:
    def __init__(self):
        self.check_csv_file()
    
    def check_csv_file(self):
        # check if data_list.csv exists in the current dir
        if 'data_list.csv' not in os.listdir('./'):
            print('\nSystem: No data_list.csv file in dir. Creating new file')
            data = {'IMS_num' : [],
                    'Date' : [],
                    'About' : [],
                    'Comment' : []
            }
            df = pd.DataFrame(data)
            df.to_csv('./data_list.csv')
            print('System: Successfully created data_list.csv')

    def data_disp_all(self):
        self.check_csv_file()
        df = pd.read_csv('./data_list.csv', index_col=0) # index_col eliminates unnamed: 0 column
        print()

        ret = []
        comment_ret = []
        for i in df['IMS_num']:
            index = df.query(f'IMS_num == {i}').index.tolist()

            ret_index = str(index[0])
            ims_num = str(list(df.loc[index, 'IMS_num'])[0])
            date = df.loc[index, 'Date']
            about = df.loc[index, 'About']
            comment = str(df.loc[index, 'Comment'])
            comment = str(comment[:len(comment)//2] + '...')
            article = list(ret_index + " | " + ims_num + " | " + date + " | " + about)
            ret.append(article)
            comment_ret.append(comment)

        for i in range(len(ret)):
            print(ret[i][0])
            print(comment_ret[i][4:].strip()+'\n')
    
    def data_disp_single(self, num):
        if num == '':
            print('\nSystem: Empty input')
            return

        self.check_csv_file()
        df = pd.read_csv('./data_list.csv', index_col=0)

        # check if IMS num exists
        if int(num) not in list(df['IMS_num']):
            print('\nSystem: IMS number does not exist')
            return
        
        index = df.query(f'IMS_num == {num}').index.tolist()
        index = index[0]

        about = df.loc[index, 'About']
        ims_date = df.loc[index, 'Date']
        ims_comment = str(df.loc[index, 'Comment'])

        print(f'> IMS num: {num}')
        print(f'> About: {about}')
        print(f'> Update date: {ims_date}')
        print(f'> Comment: {ims_comment}\n')

    def data_add(self, num, date, comment): # **duplicate addition needs fixing !!!!!!!!!!
        self.check_csv_file()
        df = pd.read_csv('./data_list.csv', index_col=0)
        
        # check if IMS num alread exists
        if int(num) in list(df['IMS_num']):
            print('\nSystem: IMS number already exists')
            return

        about = input('What is it about?(short memo) : ')

        # execute addition
        data = {"IMS_num" : num,
                "Date" : date,
                "About" : about,
                "Comment" : comment
        }
        df = df.append(data, ignore_index=True)
        
        df.to_csv('./data_list.csv')
        print('\nSystem: Data successfully added')
    
    def data_del(self, num):
        self.check_csv_file()
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
    
    def data_to_list(self):
        self.check_csv_file()
        df = pd.read_csv('./data_list.csv', index_col=0)
        return list(df["IMS_num"])

    def data_date_check(self, num):
        self.check_csv_file()
        df = pd.read_csv('./data_list.csv', index_col=0)

        index = df.query(f'IMS_num == {num}').index.tolist()
        temp = df.loc[index, ['Date']]
        temp = temp['Date'].tolist()
        current_date = temp[0]

        return current_date

    def get_data_about(self, num):
        self.check_csv_file()
        df = pd.read_csv('./data_list.csv', index_col=0)

        index = df.query(f'IMS_num == {num}').index.tolist()
        data_index = index[0]
        return df.loc[data_index, 'About']
    
    def data_switch(self, num, date_to, comment_to):
        self.check_csv_file()
        df = pd.read_csv('./data_list.csv', index_col=0)

        index = df.query(f'IMS_num == {num}').index.tolist()
        data_index = index[0]

        # date switch
        df.loc[data_index, ['Date']] = date_to
        # comment switch
        df.loc[data_index, ['Comment']] = comment_to

        df.to_csv('./data_list.csv')