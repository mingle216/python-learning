# @Version  : 1.0
# @Author   : mmh
# @File     : 30_dict_exercise.py
# @Time     : 2024/11/5 14:42

clerks = {
    '0001': {
        'age': 20,
        'name': '贾宝玉',
        'entry_time': '2011-11-11',
        'sal': 12000
    }, '0002': {
        'age': 21,
        'name': '薛宝钗',
        'entry_time': '2015-11-12',
        'sal': 10000
    }, '0010': {
        'age': 18,
        'name': '林黛玉',
        'entry_time': '2018-11-16',
        'sal': 18000
    }
}

print(f"查询员工号(0010)的员工信息为： "
      f"名字 {clerks['0010']['name']} "
      f" 入职时间 {clerks['0010']['entry_time']}"
      f" 年龄 {clerks['0010']['age']}"
      f" 薪水 {clerks['0010']['sal']}")
clerks['0006'] = {
    'age': 35,
    'name': '贾政',
    'entry_time': '2010-11-16',
    'sal': 14000
}
print(clerks)
del clerks['0002']

clerks['0006']['sal'] = 16000
clerks['0006']['name'] = '迎春'
clerks['0006']['time'] = '2016-08-30'
print(clerks)

keys=clerks.keys()
print(keys)
for key in keys:
    clerks[key]['sal'] *= 1.2
    print(f"员工号为：{key}的信息如下："
          f"年龄为：{clerks[key]['age']}"
          f"入职时间为：{clerks[key]['entry_time']}"
          f"薪水为：{clerks[key]['sal']}")

