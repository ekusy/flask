# -*- coding: utf-8 -*-
import calendar
#row行,col列のテーブルを作る
#option border=int：枠線の太さ
def make_table(row,col,**option):
    source = ''
    if option.get('border') != None:
        source = '<table border=' + str(option['border']) + '>\n'
    else:
        source = '<table border=1>\n'
    th = ''
    if option.get('th_class') != None:
        th += '<th class="' + option['th_class'] + '">'
    else:
        th += '<th>'
    td = ''
    if option.get('td_class') != None:
        td += '<td class="' + option['td_class'] + '">'
    else:
        td += '<td>'

    void = False
    if option.get('blank') != None:
        if option['blank'] == True:
            void = True

    for r in range(0,row):
        source+='\t<tr>'
        for c in range(0,col):
            cell = ''
            if void == False:
                cell = str(r)+'-'+str(c)
            if r == 0:
                tag = th +cell+'</th>'
                source+=tag
            else:
                tag = td +cell+'</td>'
                source+=tag
        source+='</tr>'
        source+='\n'

    source+='</table>'
    return source

#生成したテーブルのrow,colセルのタグ、テキストを変更する
#(replace_cell(source=html_source,row=int,col=int,**text tag=str,value=str):
def replace_cell(source,row,col,**text):
    cell = str(row)+'-'+str(col)
    #result = source
    if text.get('tag') != None:
        print 'tag'
        before = '>'+cell
        after = ' '+text['tag']+'>'+cell
        source = source.replace(before,after)
    if text.get('value') != None:
        print 'value'
        source = source.replace(cell,text['value'])
    return source
    #source = result


def makeHtmlCalendar(year,month):
    c = calendar.HTMLCalendar()
    return (c.formatmonth(year,month))

# source =  make_table(4,3)
# #source = replace_cell(source,1,1,value='replace')
# source = replace_cell(source,2,1,value='replace',tag='style="color:red"')
# print source
# f = open('sample_table.html', 'w')
# f.write(source)
# f.close()
