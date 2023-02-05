#coding:utf-8
"""测试ChoiceRandomLs.ReUnitLs方法。输入一个列表，输出一个随机打乱顺序的列表"""
import ChoiceRandomLs

def main():
	ls = []
	ls_r1 = []
	ls_r2 = []
	ls.append('a')
	ls.append('b')
	ls.append('c')
	ls.append('d')
	ls.append('e')
	ls.append('f')
	ls.append('g')
	ls.append('h')
	ls.append('i')
	ls.append('j')
	print "Before random:" + str(ls)
	ls_r1 = ChoiceRandomLs.ReUnitLs(ls)
	print "User exchange,After random:" + str(ls_r1)
	ls_r2 = ChoiceRandomLs.ReUnitLs2(ls)
	print "User range,After random:" + str(ls_r2)

if __name__=='__main__':
	main()