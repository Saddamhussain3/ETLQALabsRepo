#from pymysql import connect
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('mysql+pymysql://root:Heena%402001@localhost:3306/kodnest')
connection = engine.connect()
query='select * from customer'
df = pd.read_sql(query,connection)
print(df)
