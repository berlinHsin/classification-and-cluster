#encoding:utf-8

import collections , time , random

class lib :

	def cosineSim(self,lstA,lstB) :
		""" (list , list) -> float """
		summation = 0.
		for i , value in enumerate(lstA) :
			summation += value*lstB[i]
		return (summation/(self.getLength(lstA)*self.getLength(lstB)),lambda x , y : True if x > y else False )	
		# if x > y , means that x gets shorter distance
		# the lambda is for check whether x shorter than y

	def euDistance(self,lstA,lstB):
		""" (list , list) -> float"""
		summation = 0.
		for i,value in enumerate(lstA) :
			summation += (value - lstB[i])**2
		return (summation**0.5,lambda x , y : True if x < y else False)
		# if x < y ,means that x gets shorter distance
		# the lambda is for check whether x shorter than y

	def getLength(self,lst) :
		""" (list) -> float """
		length = 0.
		for i in lst :
			length += i**2
		return length**0.5 
	
	def calCore(self,group) :
		summation = []
		for i in range( len(self.Datas[0]) ) :
			summation.append(0)
		for index in group :
			summation = [ (x+y) for x , y in zip(summation,self.Datas[index]) ]
		count = len(group)
		for i , value in enumerate(summation) :
			summation[i] = float(value)/count
		return summation
		
