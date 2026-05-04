#
#  do_cactus.py
#    workflow: till all field, plant cactus, 
#              do bubble-sort row-wise and column-wise, back to top-left corner and harvest.
#
import betterMove, sort, farmer

size = 16
set_world_size(size)
change_hat(Hats.Cactus_Hat)

farmer.prepare_field("soil")

def plant_cactus():
	if get_entity_type() != Entities.Cactus:
		plant(Entities.Cactus)
def bbsort_row():
	sort.bubble_sort("row")
def bbsort_col():
	sort.bubble_sort("column")	

while True:
			
	farmer.multi_do_all(plant_cactus)
	
	betterMove.get_start() 
	for _ in range(size):
		
		if not spawn_drone(bbsort_row):
			bbsort_row()
		move(South)
	
	while num_drones() > 1:
		pass
	
	betterMove.get_start()
	for _ in range(size):
		if not spawn_drone(bbsort_col):
			bbsort_col()
		move(East)
	
	while num_drones() > 1:
		pass
		
	betterMove.get_start()
	harvest()
