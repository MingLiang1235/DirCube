#coding:utf-8
# def DevideRec(L,n):
	# """ input//
	# L:list
	# n:length of L
	# output//
	# L: sorted L of input
	# """
	# #print "from 0 to "+ str(n-1)+" :"
	# recMergeSort(L,0,n-1)
import math

posInit = 65    #起始位置（y轴）
def devideRec(L,w,h):
	""" wrap function.
	input//
	L:list that length is n
	w:the rectangle area's width
	h:the rectangle area's height
	s:the first element's index of L
	t:the last element's index of L
	//output
	L[s...t],mean sorted L[s]...L[t]
	lsRec, the output rectangles' list data structure
	"""
	#global lsRec
	#lsRec = []
	
	pos = [0,posInit]
	for j in range(len(L)):
		L[j]["w"]=0
		L[j]["h"]=0
		L[j]["pos"]=pos
	print "Initial L with zero value:" + str(L)
	recurseDevide(L,w,h,pos)
	print "\n The output L is : " + str(L)
	return L
	
def recurseDevide(L,w,h,pos):
	"""L的组成：
	   pos:元组，新锚点的坐标
	   w:每次迭代的宽度范围
	   h:每次迭代的高度范围
	   L:每次待迭代的部分列表数据"""
	#global lsRec
	i = len(L)
	
	if i>=2 :
		#print "from "+str(s) + "  "+str(t)
		#devided = [0,0]                 #初始化一个元组（不好，待改进）
		devided = [None]
		#print "in iteration ,devided = [] : "+ str(devided)
		devided = devideLto2(L,w,h,pos)  # 将L分成两个devide，用于进一步递归。
		
		# rec1 = [0,0,[0,0]]    #w1,h1,pos1,初始化，待改进   
		# rec2 = [0,0,[0,0]]    #w2,h2,pos2 初始化，待改进
		# rec = [rec1,rec2]     #初始化，待改进 
		# rec = getDevidedWHP(L,w,h,pos)  #觉得这个函数和devideLto2最好合并起来比较好。
		#print "m=" + str(m)
		recurseDevide(devided[0],devided[0][0]['w'],devided[0][0]['h'],devided[0][0]['pos'])  #因为devided[0][0]和devided[0][1]以及接下来的[0][2]等数据相同，所以取[0][0]的数据
		recurseDevide(devided[1],devided[1][0]['w'],devided[1][0]['h'],devided[1][0]['pos'])

	else :
		# entityRec = {'pos'=[0,0],'w'=0,'h'=0}  #初始化嵌套元素，待改进
		# entityRec['pos']=pos
		# entityRec['w']=w
		# entityRec['h']=h
		L[0]['pos'] = pos   #这里要用L[0]因为只有一个项目，那么就是第一个项目
		L[0]['w'] = w
		L[0]['h'] = h
		#SlsRec.append(entityRec)
		return 
def devideLto2(L,w,h,pos):
	""" //input
	L: list with data  each element is {'isDir':true,'size':num,'name':string}
	return: List: List with data each element is {'list':L,'w':width of devided rec,'h':height of devided rectangle,'pos':position of devided rectangle}.
	"""
	allSize = 0L
	for m in range(len(L)):
		allSize += L[m]['size']
	part = 0L
	i=0
	rate = 0.0
	for i in range(0,len(L)):  #i=0,1,2,3,4,5,6,7,8,9
		part += L[i]['size']
		rate = part*1.0/allSize
		if rate >0.25:
			L1 = L[:i+1]   #如果到第10个，就是i=9的时候才超过0.3，那么L[:10]索引为0到9
			L2 = L[i+1:]   #此时这个L[10:]内容为空数列。
			break
		if i==len(L)-1:
			L1 = L[:i+1]   #如果到第10个，就是i=9的时候才超过0.3，那么L[:10]索引为0到9
			L2 = L[i+1:]   #此时这个L[10:]内容为空数列。
	# pos = [0,0]
	# rec1 = {'list':L1,'w':0L,'h':0L,'pos':pos}  # 产生的两个元素之一（列表devided的元素1）
	# rec2 = {'list':L2,'w':0L,'h':0L,'pos':pos}  # 产生的两个元素之二（列表devided的元素2）
	List = []
	List.append(L1)
	List.append(L2)
	#print "List= "+str(List)
	
	#以下是使用所有的规则得出的结果
	#print "i="+str(i)+"; rate="+str(rate)
	for i in range(len(List[0])):    #或取消迭代仅将数据写入List[0][0]，可提高速度
		if w>h:
			List[0][i]['w'] = math.floor(w*rate)
			List[0][i]['h'] = h
			List[0][i]['pos'] = pos
		else:
			List[0][i]['h'] = math.floor(h*rate)
			List[0][i]['w'] = w
			List[0][i]['pos'] = pos
	for i in range(len(List[1])):
		if w>h:
			List[1][i]['w'] = math.floor(w-w*rate)
			List[1][i]['h'] = h
			List[1][i]['pos'] = [pos[0]+math.floor(w*rate),pos[1]]
		else:
			List[1][i]['h'] = math.floor(h-h*rate)
			List[1][i]['w'] = w
			List[1][i]['pos'] = [pos[0],pos[1]+math.floor(h*rate)]
	#print "Devided List[0] = " + str(List[0]) + '\n'
	#print "Devided List[1] = " + str(List[1]) + '\n'
	return List

	
		
		
		
		
		
		
