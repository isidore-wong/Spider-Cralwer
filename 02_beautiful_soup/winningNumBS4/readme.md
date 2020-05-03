知识点：

1、getpass模块：

getpass模块提供了平台无关的在命令行下输入密码的方法; 该模块主要提供: 两个函数: getuser, getpass

一个报警: GetPassWarning(当输入的密码可能会显示的时候抛出，该报警为UserWarning的一个子类)

getpass.getuser()该函数返回登陆的用户名,不需要参数

getpass.getpass([prompt[, stream]])会显示提示字符串, 关闭键盘的屏幕回显，然后读取密码

通过IDLE中来调getpass函数，会显示输入的密码，必须在Python Shell或Windows下的CMD才不会显示密码

2、sys.argv[]：

sys.argv: 实现从程序外部向程序传递参数,sys.argv[0]表示代码本身文件路径

3、logging模块：


