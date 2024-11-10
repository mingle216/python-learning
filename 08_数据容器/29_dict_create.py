# @Version  : 1.0
# @Author   : mmh
# @File     : 29_dict_create.py
# @Time     : 2024/11/5 14:16

books = ['红楼梦','三国演义','西游记','水浒传']
authors =['曹雪芹','罗贯中','吴承恩','施耐庵']

print({books:authors for books,authors in zip (books,authors)})
print(dict(zip(books,authors)))



english_list=['red','black','yellow','white']
chinese_list=['红色','黑色','黄色','白色']

print({chinese_list:english_list.upper() for chinese_list,english_list in zip(chinese_list,english_list)})