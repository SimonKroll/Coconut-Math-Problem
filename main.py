import time
base = 4
basemult = 1
newset = 0
timer = time.time()
solutions = 0

while basemult < 10000:
	newbase = base * basemult
	for i in range(5):
		newset = (newbase) * (5 / 4) + 1
		#print(newset)
		if (i) == 4:  #5 iterations
			print("solution found:", int(newset))
			elapsedtime = time.time() - timer
			print("Time elasped:", elapsedtime)
			solutions += 1
			print("Total Solutions", solutions)
		else:
			pass
		if (newset * 5) % 4 > 0:
			#print("decimal error. Starting over.")
			break
		else:
			newbase = newset
	basemult += 1
