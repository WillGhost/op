#/bin/env python3
lss = ['a','b','c',]

def permute(nums):
    res = []
    def recursion(path, cand):
        if len(cand) == 0:
            res.append(path)
        for k, v in enumerate(cand):
            recursion(path + [v], cand[:k] + cand[k+1:])
    recursion([], nums)
    return res

res = permute(lss)
for i in res:
	print(i)
