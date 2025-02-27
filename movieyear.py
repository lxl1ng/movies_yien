from pyecharts.charts import Bar
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from pyecharts import options as opts
from pyecharts.globals import ThemeType

MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '111111'
MYSQL_DB = 'maoyan'

engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8'
                       % (MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DB))

sql = 'SELECT * FROM xmx'

db = pd.read_sql(sql, engine)

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
# df = db.sort_values(by="value", ascending=False)
dom = db[['name', 'value']]

# 改变这里获取不同年份！
attr = np.array(dom['name'][175:200])
v1 = np.array(dom['value'][175:200])
attr = ["{}".format(i.replace('', '')) for i in attr]
v1 = ["{}".format(float('%.2f' % (float(i)))) for i in v1]

# 创建 Bar 类的对象 , 并指定画布的大小
bar = Bar(init_opts=opts.InitOpts(width='2000px', height='1000px',theme=ThemeType.ROMANTIC))
# 添加 x 轴和 y 轴的数据
bar.add_xaxis(attr)
bar.add_yaxis(" 电影名", v1)
bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
# 设置标题、 y 轴标签
bar.set_global_opts(title_opts=opts.TitleOpts(title=" 2016年年度票房榜TOP25 "),
                    yaxis_opts=opts.AxisOpts(name=" 销售额 ( 万元 )",
                                             name_location="center", name_gap=1, is_show=True))
bar.render("2016年年度票房榜.html")
