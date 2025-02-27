import pandas as pd
from sqlalchemy import create_engine
import pyecharts.options as opts
from pyecharts.charts import Bar, Pie, Line
from pyecharts.globals import ThemeType

MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '111111'
MYSQL_DB = 'maoyan'

engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8'
                       % (MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DB))

sql = 'SELECT * FROM xmx'

df = pd.read_sql(sql, engine)

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
print(df)

dom1 = []
for i in df['type']:
    type1 = i.split(',')
    for j in range(len(type1)):
        if type1[j] in dom1:
            continue
        else:
            dom1.append(type1[j])

dom2 = []
for item in dom1:
    num = 0
    for i in df['type']:
        type2 = i.split(',')
        for j in range(len(type2)):
            if type2[j] == item:
                num += 1
            else:
                continue
    dom2.append(num)


def message():
    for k in range(len(dom2)):
        data = {}
        data['name'] = dom1[k]
        yield data


data1 = message()
dom3 = []
for item in data1:
    dom3.append(item)

print(dom1)
print(dom2)

# # 柱状图
# # 创建 Bar 类的对象 , 并指定画布的大小
# bar = Bar(init_opts=opts.InitOpts(width='2000px', height='1000px'))
# # 添加 x 轴和 y 轴的数据
# bar.add_xaxis(dom1)
# bar.add_yaxis(" 电影类型", dom2)
# bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
# # 设置标题、 y 轴标签
# bar.set_global_opts(title_opts=opts.TitleOpts(title=" TOP25电影类型柱状图"),
#                     yaxis_opts=opts.AxisOpts(name=" 销售额 ( 万元 )",
#                                              name_location="center", name_gap=1, is_show=True))
# bar.render("TOP25电影类型柱状图.html")

# # 饼状图
# x_data = dom1
# y_data = dom2
#
# c = (
#     Pie(init_opts=opts.InitOpts(width="1700px", height="1000px",theme=ThemeType.WHITE))  # 图形的大小设置
#     .add(
#         series_name="电影类型",
#         data_pair=[list(z) for z in zip(x_data, y_data)],
#         radius=["15%", "50%"],  # 饼图内圈和外圈的大小比例
#         center=["30%", "40%"],  # 饼图的位置：左边距和上边距
#         label_opts=opts.LabelOpts(is_show=True),  # 显示数据和百分比
#     )
#     .set_global_opts(legend_opts=opts.LegendOpts(pos_left="center", orient="vertical"))  # 图例在左边和垂直显示
#     .set_series_opts(
#         tooltip_opts=opts.TooltipOpts(
#             trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
#         ),
#     ))
# c.render("TOP25电影类型饼状图.html")


attr = dom1
v1 = dom2
line = (
    Line(init_opts=opts.InitOpts(width="1700px", height="1000px"))
    .add_xaxis(attr)
    .add_yaxis('电影类型', v1,
               markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_='max')]),

               )
    .set_global_opts(title_opts=opts.TitleOpts(title="TOP25电影类型折线图"))
)
# line.render("TOP25电影类型折线图.html")
