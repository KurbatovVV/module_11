import unittest

a=[1,2,4,6,12,10]

def merge_sort(a):
	if len(a)<2:
		return a[:]
	else:
		median=int(len(a)/2)
		left=merge_sort(a[:median])
		right=merge_sort(a[median:])
		return merge(left, right)

def merge(left, right):
	rez=[]
	i,j = 0, 0
	while i<len(left) and j<len(right):
		if left[i]<right[j]:
			rez.append(left[i])
			i+=1
		else:
			rez.append(right[j])
			j+=1
	while i<len(left):
		rez.append(left[i])
		i+=1
	while j<len(right):
		rez.append(right[j])
		j+=1
	return rez
print(merge_sort(a))


class TestSort(unittest.TestCase):
	def test_1(self):
		massive = [1,2,3,4,10,8,7]
		sort = sorted(massive)
		self.assertEqual(merge_sort(massive), sort)



	def test_2(self):
		massive = [6,0,0,1, -1]
		sort = sorted(massive)
		self.assertEqual(merge_sort(massive),sort)

unittest.main()