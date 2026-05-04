# betterMove.py
#
#	collections of ways of moving
#
def goto(x,y):

	x0,y0 = get_pos_x(), get_pos_y()
	dx = x - x0
	dy = y - y0
	
	if dx > 0: 
		for _ in range(dx):
			rmove(East)		
	elif dx < 0:
		for _ in range(-dx):
			rmove(West)
	if dy > 0: 
		for _ in range(dy):
			rmove(North)
	elif dy < 0:
		for _ in range(-dy):
			rmove(South)
			
def fgoto(x,y):
	
	x0 = get_pos_x()
	y0 = get_pos_y()
	size = get_world_size()
	dx = (x - x0) % size
	dy = (y - y0) % size
	
	if dx <= size / 2:
		for _ in range(dx):
			move(East)
	else:
		for _ in range(size - dx):
			move(West)
			
	if dy <= size / 2:
		for _ in range(dy):
			move(North)
	else:
		for _ in range(size - dy):
			move(South)
			
def get_start():
	fgoto(0,get_world_size()-1)
	
RT = {North: East, East: South, South: West, West: North}
LT = {North: West, West: South, South: East, East: North}
OP = {North: South, South: North, East: West, West: East}
last_dir = North

def rmove(target_dir):
	global last_dir
	
	# 防回頭 -> 右轉
	if target_dir == OP[last_dir]:
		target_dir = RT[last_dir]
	
	# 碰撞檢查 執行移動
	if can_move(target_dir):
		move(target_dir)
		last_dir = target_dir
		return True
	else:
		# 前方有障礙 往右側閃避
		escape_dir = RT[last_dir]
		if can_move(escape_dir):
			move(escape_dir)
			last_dir = escape_dir
			return True
	return False