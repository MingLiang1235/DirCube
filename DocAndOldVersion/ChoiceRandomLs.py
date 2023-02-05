#coding:utf-8
# def devideRec(L):
	# """ input//
	# L: sourcelist
	# 
	# output//
	# L: random sort(arrange) of L
	# """
	# #print "from 0 to "+ str(n-1)+" :"
	# recMergeSort(L,0,n-1)
import random

def ReUnitLs(L):
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

	length = len(L)
	jumpseed = []
	jump = []
	ls = []
	#print "Empty ls is :"+ str(ls)+'\n'
	for i in range(length):
		jumpseed.append(random.randint(0,length-1))  
		jump.append(i)
	for i in range(length):
		temp = jump[i]
		jump[i] = jump[jumpseed[i]]
		jump[jumpseed[i]] = temp
	j = 0
	#print "jump[i]: "+str(jump)+'\n'
	for i in jump:
		ls.append(L[i])
		j+=1
	#print "L:  "+str(L)+'\n'
	#print "return ls : "+str(ls)+'\n'
	return ls
	
	
	
	
	
		
