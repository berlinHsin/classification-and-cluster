#encoding :utf-8

from library import lib

class Hierarchical(lib) :
	def __init__(self,K,Datas):
		self.K = K
		self.Datas = Datas
		self.Group  = {}
		self.Distance = [] 
		self.distanceType = self.cosineSim

	def calDistance(self) :
		for nId , node in enumerate(self.Datas) :
			distanceDict = {}
			for nId2 , node2 in enumerate(self.Datas) :
				if nId != nId2 :
					distance , check = self.distanceType(nId,nId2)
					distanceDict.update({nId2:distance})
			self.Distance.update({nId,distanceDict})

	def calGroupDist(self) :
		self.Distance = []
		for gId , group in enumerate(self.Group) :
			self.calDistance(group)
	
	def merge(self) :
		self.calGroupDist()

	def main(self) :
		for nodeId in range(len(self.Datas)) :
			self.Group.update({nodeId:[nodeId]})
		self.calDistance()



		while(len(self.Group)>self.K) :
			self.merge()

		print(self.Distance)

if __name__ == "__main__" :
	exampleLst = [ [0,24,5] , [24,1,0] , [0,1,0] , [0,25,2] ]
	obj = Hierarchical(2,exampleLst)
	obj.main()
