#encoding : utf-8

from library import lib 
import random

class KMEANS(lib) :
	
	def __init__(self , K , datas , iters=50) : 
		self.K 	    = K     # for K cluster
		self.Datas  = datas # A matrix of Doc & Vocab , value can be tf or sth else . ex [ [ 1 , 2] , [0,1] ] 
		self.Seed   = []    # Core for each cluster
		self.Result = {}    # Result of KMEANS , changed at each iters 
		self.iters  = iters # iters time
		self.distanceType = self.cosineSim
	

	def randomPick(self) :
		""" 
			pick initial core at iter 1 .
			Generate K node as core , and append datas into Seed .
		"""
		randList = random.sample( range(len(self.Datas)) , self.K )
		self.Seed = [ self.Datas[index] for index in randList ]

	def nearestCore(self,data) :
		"""
			(list,function) -> (int)
			Find the nearest core for data .
			return index of the node
		"""
		core , nearest = 0 , None
		for i , seed in enumerate(self.Seed) :
			distance , check = self.distanceType(seed,data)
			if nearest is None or check(nearest,distance) :
				core , nearest = i , distance
		return core

	def clustering(self) :
		self.Result = {}
		for i , data in enumerate(self.Datas) :
			core = self.nearestCore(data)	
			if core not in self.Result :
				self.Result.update({core:[i]})
			else :
				self.Result[core].append(i)

	def main(self,showResult=None) :
		self.randomPick()
		self.clustering()
		for count in range(self.iters) :
			for i , group in enumerate(self.Result) :
				newCore = self.calCore(self.Result[group])
				self.Seed[i] = newCore
			print(" Iteration {} :".format(count))			
			print(self.Result)			
			self.clustering()
		if showResult is None :
			print("Final : {}".format(self.Result))
		else :
			showResult(self.Result)


if __name__ == "__main__" :
	exampleLst = [ [0,24,5] , [24,1,0] , [0,1,0] , [0,25,2] ]
	obj = KMEANS(2,exampleLst,10)
	obj.main()

	obj.setDistanceType(obj.euDistance)
	obj.main()
