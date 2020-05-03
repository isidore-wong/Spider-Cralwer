该程序运行过程中的报错和解决

1.line65中针对属性为数字类型的li标签，采用正则表达式re.compile函数进行处理

tags = anchor_tag.find_all('li', attrs={'media': re.compile(r'\d{6}')})

2.line78报错“TypeError: unsupported operand type(s) for %: 'NoneType' and 'tuple'”

原因在于python3.x与python2.x有一点区别，
原来%(变量名,...)应该是加在print括号里的
如：print("who is the murder? %s or %s" % (a, b))
并非print("who is the murder? %s or %s") % (a, b)
