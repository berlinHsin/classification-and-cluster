#encoding :utf-8

from library import lib

class Hierarchical(lib) :
	def __init__(self,K,Datas):
		self.K = K
		self.Datas = Datas
		self.Result = []
		self.Group  = {}
	
	def merge(self) :
		randLst = random.sample( range(len(self.Group)) , len(self.Group))
		removeLst = []
		for groupId in randLst :
			nearest = self.getNearest(self.Group[groupId],randLst)
			randLst.remove(nearest)
