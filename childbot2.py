import pandas as pd
df = pd.read_csv('time_child.csv', names=['customer_id','time'])
def check_id_time(customer_pass_id):
    if(df['customer_id'].values.tolist().index(customer_pass_id)):
        index_cust_id = df['customer_id'].values.tolist().index(customer_pass_id)
        return df['time'][index_cust_id]
