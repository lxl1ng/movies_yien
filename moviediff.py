from pyecharts.charts import Bar,Page,Pie
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

# 此处更换sql语句查询中外
sql1 = "SELECT * FROM xmx WHERE country like '%%中国%%' and time like '2021%%'"
sql2 = "SELECT * FROM xmx WHERE country not like '%%中国%%' and time like '2021%%'"
db1 = pd.read_sql(sql1, engine)


#解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

df1 = db1.sort_values(by="value", ascending=False)
dom1 = df1[['name', 'value']]

attr1 = np.array(dom1['name'][0:10])
v1 = np.array(dom1['value'][0:10])
attr = ["{}".format(i.replace('', '')) for i in attr1]
v1 = ["{}".format(float('%.2f' % (float(i)))) for i in v1]

db2 = pd.read_sql(sql2, engine)

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
df2 = db2.sort_values(by="value", ascending=False)
dom2 = df2[['name', 'value']]

attr2 = np.array(dom2['name'][0:10])
v2 = np.array(dom2['value'][0:10])
attr2 = ["{}".format(i.replace('', '')) for i in attr2]
v2 = ["{}".format(float('%.2f' % (float(i)))) for i in v2]

# 创建 Bar 类的对象 , 并指定画布的大小
# bar = Bar(init_opts=opts.InitOpts(width='2000px', height='1000px'))
# # 添加 x 轴和 y 轴的数据
# bar.add_xaxis(attr)
# bar.add_yaxis(" 电影名", v1)
# bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
# # 设置标题、 y 轴标签
# bar.set_global_opts(title_opts=opts.TitleOpts(title=" 中国电影票房榜TOP35 "),
#                     yaxis_opts=opts.AxisOpts(name=" 销售额 ( 万元 )",
#                                              name_location="center", name_gap=1, is_show=True))
# bar.render("中国电影票房榜TOP35.html")


# bar = Bar(init_opts=opts.InitOpts(width='2000px', height='1000px'))
#
# bar.add_xaxis(attr1)
# bar.add_yaxis("中国电影", v1)
# bar.add_yaxis("外国电影", v2)
#
#
# bar.set_global_opts(title_opts=opts.TitleOpts(title=" 中外电影票房榜TOP10对比柱状图 "),
#                     xaxis_opts=opts.AxisOpts(name_location="center", name_gap=1, is_show=True),
#                     yaxis_opts=opts.AxisOpts(name=" 销售额 ( 万元 )",
#                                              name_location="center", name_gap=1, is_show=True))
#
# bar.render("中外电影票房榜TOP10对比柱状图.html")


# 饼状图
y1=[int(np.sum(dom1["value"])),int(np.sum(dom2["value"]))]
x_data =['中国','外国']
y_data =y1
print(y_data)
c = (
    Pie(init_opts=opts.InitOpts(width="1700px", height="1000px",theme=ThemeType.WHITE))  # 图形的大小设置
    .add(
        series_name="拍摄国家",
        data_pair=[list(z) for z in zip(x_data, y_data)],
        radius=["15%", "50%"],  # 饼图内圈和外圈的大小比例
        center=["30%", "40%"],  # 饼图的位置：左边距和上边距
        label_opts=opts.LabelOpts(is_show=True),  # 显示数据和百分比
    )
    .set_global_opts(legend_opts=opts.LegendOpts(pos_left="center", orient="vertical"))  # 图例在左边和垂直显示
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        ),
    ))
c.render("2021年中外电影票房对比.html")