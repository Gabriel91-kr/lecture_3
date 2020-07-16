import func_module

# func_module.module_show()

nowdate = func_module.date_now()
now_year = nowdate.year
date_today = '{}년 {}월 {}일'.format(nowdate.year , nowdate.month ,nowdate.day)
# print(nowdate)
print(date_today)

X_mas = nowdate.replace(month = 12, day=25)

date_xmas = '{}년 {}월 {}일'.format(X_mas.year , X_mas.month ,X_mas.day)
print(date_xmas)