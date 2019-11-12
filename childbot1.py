import pandas as pd
df = pd.read_csv('location_child.csv', names=['customer_id','storage_location'])
def check_id_storage_location(customer_pass_id):
    if(df['customer_id'].values.tolist().index(customer_pass_id)):
        index_cust_id = df['customer_id'].values.tolist().index(customer_pass_id)
        return df['storage_location'][index_cust_id]
