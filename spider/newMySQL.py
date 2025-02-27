# csv导入MySQL数据库
import pandas as pd
from sqlalchemy import create_engine

# 数据库信息
mysql_setting = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': '111111',
    # 数据库名称
    'db': 'maoyan',
    'charset': 'utf8'
}
# 表名
# 如果不存在表，则自动创建
table_name = 'xm9'
# 文件路径
path = r'C:\Users\86189\PycharmProjects\pythonProject10\movies111.csv'

data = pd.read_csv(path, encoding='utf-8')
print(data)
engine = create_engine("mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}".format(**mysql_setting), max_overflow=7)
data.to_sql(table_name, engine, index=True, if_exists='replace', )
print('导入成功...')
