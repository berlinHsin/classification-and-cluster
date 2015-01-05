#encoding :utf-8

from library import lib

class Hierarchical(lib) :
	def __init__(self,K,Datas):
		self.K = K
		self.Datas = Datas
		self.Group  = {}
		self.NodeDistance = {} 
		self.GroupDistance = {}
		self.distanceType = self.cosineSim
		self.check        = None

	def calNodeDistance(self) :
		nodeCount = len(self.Datas)
		for node1 in range(nodeCount) :
			for node2 in range(nodeCount) :
				distance,check = self.distanceType(node1,node2)
				self.NodeDistance[node1].update({node2:distance})
				self.check     = check
		""" Get distance for each two nodes """

	def calGroupDistance(self,gId1,gId2) :
		nearest = None
		for node1 in self.Group[gId1] :
			for node2 in self.Group[gId2] :
				distance = self.NodeDistance[node1][node2]
				if nearest is None or self.check(nearest,distance) :
					nearest = distance
		return nearest

	def getGroupData(self) :
		groupCount = len(self.Group)
		for gId1 in range(groupCount) :
			self.GroupDistance.update({gId:{}})
			for gId2 in range(groupCount) :
				distance = self.calGroupDistance(gId1,gId2)
				self.GroupDistance[gId1].update({gId2:distance})
	
	def merge(self) :
		self.getGroupData() # find the distace for each 2 groups 
		pass 

	def main(self) :
		for nodeId in range(len(self.Datas)) :
			self.NodeDistance.update({nodeId:{}})
			self.Group.update({nodeId:[nodeId]})
		self.calNodeDistance()

		while(len(self.Group)>self.K) :
			self.merge()

if __name__ == "__main__" :
	exampleLst = [ [0,24,5] , [24,1,0] , [0,1,0] , [0,25,2] ]
	obj = Hierarchical(2,exampleLst)
	obj.main()
