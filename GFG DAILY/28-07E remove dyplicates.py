from collections import OrderedDict
class Solution:
	def removeDups(self, str):
		# code here
        t = OrderedDict.fromkeys(str)
        return ("".join(t.keys()))
