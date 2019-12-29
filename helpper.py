# Import statements
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#def extract_from_str():
    
    
def drop_col_NA_ratio(df, ratio):
    ratio_result= df.isnull().mean()*100
    df_ratio_result = pd.DataFrame(ratio_result[ratio_result>0], columns=['NA_ratio'])
    df_ratio_result.loc[df_ratio_result['NA_ratio'] >= ratio ,'color'] = 'r'
    df_ratio_result.loc[df_ratio_result['NA_ratio'] < ratio ,'color'] = 'g'
    df_ratio_result['NA_ratio'].plot.bar(figsize = (15,5), color =  df_ratio_result['color'])
    plt.show()
    dropped_df = df.drop(df_ratio_result[df_ratio_result['color'] == 'r'].index, axis=1)
    return dropped_df
    
def calendar_updated_convert(_str):
    '''
    Convert calendar_updated column string data to number
 
    INPUT
    _str - string

    OUTPUT
    s_value - converted numberical value
    '''
    dic_units = {
        'days': 1,
        'weeks': 7,
        'months': 30
    }
    dic_special = {
        'today':0,
        'yesterday':1,
        'a week':7,
        'never':900,
        '1 week':7
    }
    for key, value in dic_units.items():
        if key in _str:
            return value * [int(p_str) for p_str in _str.split() if p_str.isdigit()][0]
        else:
            for s_key, s_value in dic_special.items():
                if s_key in _str:
                    return s_value
                
def impute_to_series(obj_pd, option):
    '''
    INPUT
    obj_pd - pandas object containing NA
    option - '0'/'mean'/'mode'

    OUTPUT
    obj_pd imputed by option
    
    '''
    if isinstance(obj_pd, pd.DataFrame):
        col_list = list(obj_pd.columns)
        new_obj_pd = obj_pd.copy()

    if option == '0':
        return obj_pd.fillna(0)
    
    elif (option == 'mean') & isinstance(obj_pd, pd.DataFrame):
        for col in col_list:
            new_obj_pd.loc[:,col] = obj_pd[col].fillna(obj_pd[col].mean()[0])
        return new_obj_pd
    
    elif (option == 'mean') & isinstance(obj_pd, pd.Series):
        return obj_pd.fillna(mean()[0])
    
    elif (option == 'mode') & isinstance(obj_pd, pd.DataFrame):
        for col in col_list:
            new_obj_pd.loc[:,col] = obj_pd[col].fillna(obj_pd[col].mode()[0])
        return new_obj_pd
    
    elif (option == 'mode') & isinstance(obj_pd, pd.DataFrame):
        return obj_pd.fillna(mode()[0])
    
    else:
        return False

def extract_from_date(series_pd, option = None):
    '''
    Get year/month/day from series containing date represented as a string
    
    INPUT
    series_pd - pandas series containing date information
    option - 'year'/'month'/'day'

    OUTPUT
    ser - extracted series as option, which contains option type information:
    1. string to datetime;
    2. series map by using lambda with year/month/day method;
    '''
    
    ser = pd.to_datetime(series_pd)
    if option == 'year': 
        return ser.map(lambda x:x.year)
    elif option == 'month':
        return ser.map(lambda x:x.month)
    elif option == 'day':
        return ser.map(lambda x:x.day)
    else:
        return ser

def create_dummies(df, columns = ['room_type', 'property_type', 'bed_type', 'cancellation_policy']):
    '''
    One Hot Encoding about specific columns
    
    INPUT
    df - pandas data frame
    columns - list containing target colums names

    OUTPUT
    df - pandas data frame joined with one hot encoding result
    1. make dummies by using get_dummies funciton for one hot encoding;
    2. concatanate df with dummies ;
    '''    
    
    for column in columns:
        dummies = pd.get_dummies(df[column], prefix = column)
        new_df = pd.concat([df,dummies], axis = 1)
    return new_df
    