sort.py
def bubble_sort(mode):
	if mode == "row":
		dir1, dir2 = East, West
	if mode == "column":
		dir1, dir2 = North, South
	n = get_world_size()

	while True:
		swapped = False

		for i in range(n-1):
			v1 = measure()
			move(dir1)
			v2 = measure()
			if v1 != None and v2 != None:
				if v1 > v2 :
					swap(dir2)
					swapped = True
				
		if not swapped: 
			break
