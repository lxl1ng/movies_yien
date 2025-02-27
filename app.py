from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# 首页分页
@app.route('/index')
def home():
    return index()


@app.route('/inner1')
def inner1():
    return render_template('inner-page1.html')


@app.route('/inner2')
def inner2():
    return render_template('inner-page2.html')


@app.route('/inner3')
def inner3():
    return render_template('inner-page3.html')


@app.route('/inner4')
def inner4():
    return render_template('inner-page4.html')


# 年度票房榜分页
@app.route('/2022')
def year_22():
    return render_template('2022.html')


@app.route('/2021')
def year_21():
    return render_template('2021.html')


@app.route('/2020')
def year_20():
    return render_template('2020.html')


@app.route('/2019')
def year_19():
    return render_template('2019.html')


@app.route('/2018')
def year_18():
    return render_template('2018.html')


@app.route('/2017')
def year_17():
    return render_template('2017.html')


@app.route('/2016')
def year_16():
    return render_template('2016.html')


# 类型分布图分页
@app.route('/typePie')
def typePie():
    return render_template('typePie.html')


@app.route('/typeLine')
def typeLine():
    return render_template('typeLine.html')


# 总票房榜分页
@app.route('/avgman')
def avgman():
    return render_template('avgman.html')


@app.route('/avgtval')
def avgtval():
    return render_template('avgtval.html')


# 中外票房榜分页
@app.route('/diff_2023')
def diff_2023():
    return render_template('diff_2023.html')


@app.route('/diff_2022')
def diff_2022():
    return render_template('diff_2022.html')


@app.route('/diff_2021')
def diff_2021():
    return render_template('diff_2021.html')


@app.route('/tuijian')
def tuijian():
    return render_template('tuijian.html')

if __name__ == '__main__':
    app.run()
