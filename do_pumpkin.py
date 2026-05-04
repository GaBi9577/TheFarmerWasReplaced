# 	max = 6x6 
#
#	we don't use dead list this time 
#		because the Pumpkin will 'ramdomly' decloys :(
#

change_hat(Hats.Pumpkin_Hat)
size = 6
set_world_size(size)
import betterMove, farmer
side = get_world_size()

# -----------------------
# step 1: prepare the field
farmer.prepare_field("soil")
		
while True:
	
	# step 2: growing 1st time 
	for _ in range(side):
		for _ in range(side):			
			plant(Entities.Pumpkin)
			use_item(Items.Water)
				
			move(East)
		move(South)
				
	# checking if it's merged
	betterMove.fgoto(0, size-1)
	measureA = measure()
	betterMove.fgoto(size-1, 0)
	measureB = measure()
	if measureA == measureB:
		betterMove.get_start()
		do_a_flip()
		harvest()
		#move(South)
		#move(East)
		
		
	
			
				
