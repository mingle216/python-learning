# @Version  : 1.0
# @Author   : mmh
# @File     : 02_seq_search.py
# @Time     : 2024/11/6 14:58

name_list = ['白眉鹰王', '金毛狮王', '紫杉龙王', '青翼蝠王', '白眉鹰王', '白眉鹰王']
find_name = '白眉鹰王9'

# 使用list.index完成查找
# print("list.index完成查找".center(46, '='))
# print(name_list.index(find_name))
print("顺序查找".center(46, '='))


# 使用顺序查找完成查找
def seq_search():
    find_index = []
    for i in range(len(name_list)):
        if find_name == name_list[i]:
            find_index.append(i)

        return find_index


print(seq_search())
