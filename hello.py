# -*- coding: utf-8 -*-
from flask import Flask,render_template, request, redirect, url_for
import numpy as np
import random
from tools.make_html import make_table,makeHtmlCalendar


app = Flask(__name__)

def picked_up():
    messages = [
    'message1',
    'message2',
    'message3',
    'message4'
    ]
    return np.random.choice(messages);

@app.route("/")
def index():
    title = 'welcome hello world'
    message = picked_up()
    return render_template('index.html',title=title,message=message)

@app.route('/tools/')
def tools():
    title = u'ツール置き場'
    message = u'作成中'
    return render_template('tools.html',title=title,message=message)

@app.route("/tools/order",methods=['GET','POST'])
def order():
    line = ''
    result = ''

    form =u'\
    <form action="/tools/order" method="post">\n\
        <p>参加者<input type="text" name="name" size="80" value="POST"></p>\n\
        <input type="submit" value="順番決め"><input type="reset" value="リセット">\n\
    </form>'

    if request.method == 'POST':
        string = ''
        line = request.form['name'].encode('utf-8')
        form = form.replace('POST',unicode(line,'utf-8'))
        s = line.split('、')
        while len(s) > 1:
            num = random.randint(0,len(s)-1)
            string+=s[num]
            string+='、'
            s.pop(num)
        string+=s[0]
        result = unicode(string,'utf-8')
    else:
        form = form.replace('POST','')

    title = u'順番決めツール'
    message = u'参加者の名前を全角カンマ区切りで入力してください'
    return render_template('order.html',
                            title=title,
                            message=message,
                            result=result,
                            form = form,
                            names=unicode(line,'utf-8'))

@app.route("/tools/calendar",methods=['GET','POST'])
def calendar():
    title = u'カレンダー'
    message = u'西暦、月を選択してください'
    form =u'\
    <form action="/tools/calendar" method="post">\
      <p>西暦、月を選択してください<input type="month" name="month" size="80"></p>\
      <input type="submit" value="順番決め"><input type="reset" value="リセット">\
    </form>'
    result = ''
    if request.method == 'POST':
        #result = make_table(5,7)
        date = request.form['month']
        time = date.split('-')
        result = makeHtmlCalendar(int(time[0]),int(time[1]) )
        result = result.replace('border="0"','border="1"')
        #テーブルにボタン追加するところ
        # for num in range(1,31):
        #     cell = '>'+str(num)
        #     after = cell
        #     cell+=''
        #     result = result.replace(cell)
        #result+=u'<br />'+ request.form['month']

    return render_template('tool.html',
                            title=title,
                            message=message,
                            form = form,
                            result=result,
                            )



@app.route('/form_test',methods=['GET','POST'])
def form_test():
    title = 'form test'
    if request.method == 'POST':
        message = request.form['name']+' POST'
    else:
        message = request.args.get('name','')
        if message != '':
            message+=' GET'
    return render_template('index.html',title=title,message=message)


if __name__ == "__main__":
    app.run(debug=True)
