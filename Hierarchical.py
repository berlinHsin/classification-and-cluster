#encoding :utf-8

from library import lib

class Hierarchical(lib) :
	def __init__(self,K,Datas):
		self.K = K
		self.Datas = Datas
		self.Group  = {}
		self.Distance = [] 
		self.distanceType = self.cosineSim

	def calDistance(self,nodeId) :
		distanceLst = []
		for curNode , data in enumerate(self.Datas) :
			distance = 0
			if nodeId < curNode :
				distance , check = self.distanceType(data,self.Datas[nodeId])
			elif curNode != nodeId :
				distance = self.Distance[curNode][nodeId][1]
			distanceLst.append( [curNode,distance] )

		distance , check = self.distanceType([1],[2])
		reverseFlag = check(10,0)
		return sorted(distanceLst,key=lambda x :x[1],reverse=reverseFlag)

	def merge(self):
		distance = []
		for groupId , group in enumerate(self.Group)
			pass
	
	def main(self) :
		for nodeId in range(len(self.Datas)) :
			self.Distance.append(self.calDistance(nodeId))
			self.Group.update({nodeId:[nodeId]})

		while(len(self.Group)>self.K) :
			self.merge()

		print(self.Distance)

if __name__ == "__main__" :
	exampleLst = [ [0,24,5] , [24,1,0] , [0,1,0] , [0,25,2] ]
	obj = Hierarchical(2,exampleLst)
	obj.main()
