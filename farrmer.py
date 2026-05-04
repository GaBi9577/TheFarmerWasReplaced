import betterMove
size = get_world_size()

def do_all(f):
	for _ in range(get_world_size()):
		for _ in range(get_world_size()):
			f()
			move(East)
		move(South)
		
def multi_do_all(f, mode="row"):
	ws = get_world_size()
	
	if mode == "row":
		dir1, dir2 = East, South	
	elif mode == "column":
		dir1, dir2 = North, East

	def task():
		for j in range(ws):
			f()
			if j < ws :
				move(dir1)
					
	for i in range(ws):
		if not spawn_drone(task):
			task()
		move(dir2)

	
def prepare_field(type):
	# type: soil / grass
	
	betterMove.get_start()
	
	def do_work():
		prepare_single_field(type)
	
	multi_do_all(do_work)

def prepare_single_field(type):
	harvest()
	if type == "soil":
		type = Grounds.Soil	
	elif type == "grass":
		type = Grounds.Grassland
	if get_ground_type() != type:
		till()
		
