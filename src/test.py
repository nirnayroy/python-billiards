from math import cos, pi, sin, sqrt
import numpy as np
import billiards
from billiards.obstacles import Square, InfiniteWall
 
obs = [
     InfiniteWall((-2, -2), (2, -2)),  # bottom side
     InfiniteWall((2, -2), (2, 2)),  # right side
     InfiniteWall((2, 2), (-2, 2)),  # top side
     InfiniteWall((-2, 2), (-2, -2)),  # left side
    ]
'''bld = billiards.Billiard(obstacles=obs)



pos = [1.5, 1.6]
angle = np.random.uniform(0, 2 * pi)
vel = 0.2 * np.asarray([cos(angle), sin(angle)])
bld.add_ball(pos, vel, radius=0)
print(bld.balls_position)
print(bld.balls_velocity)
print(bld.obstacles_toi)
[(fl, _)] = bld.obstacles_toi
bld.evolve(fl)
print(bld.balls_position)
print(bld.balls_velocity)
print(bld.obstacles_toi)
[(fl, _)] = bld.obstacles_toi
bld.evolve(fl)
print(bld.balls_position)
print(bld.balls_velocity)
print(bld.obstacles_toi)'''

def make_data(obs):
	ics = []
	Xs = []
	Ys = []
	tss = []
	angle = np.random.uniform(low=0, high=(2 * pi), size=(10,))
	vels = 0.2 * np.vstack(([np.cos(angle), np.sin(angle)])).T
	positions = np.vstack(([np.random.uniform(low=-2, high=2, size=(10,)), 
				np.random.uniform(low=-2, high=2, size=(10,))])).T
	for i in positions:
		for j in vels:
			ic = []
			ts = [0]
			bld = billiards.Billiard(obstacles=obs)
			#print(i.shape, j.shape)
			bld.add_ball(i, j, radius=0)
			for k in range(10):
				[(fl, _)] = bld.obstacles_toi
				bld.evolve(fl)
				p, v = bld.balls_position, bld.balls_velocity
				#print(p.shape, v.shape, fl.shape)
				ic.append(np.hstack((p, v)))
				ts.append(fl.reshape(1, 1))

			tss.append(ts)
			#print(np.asarray(ic).shape)
			ics.append(ic)

	for i in ics:
		X = i[:-1]
		Y = i[1:]
		Xs.append(X)
		Ys.append(Y)
	Xs , Ys = np.asarray(Xs).reshape((100, 9, 4)), np.asarray(Ys).reshape((100, 9, 4)) 
	Ts = np.asarray(tss)
	
	np.save("time_steps.npy", Ts, allow_pickle=True)
	np.save("input.npy", Xs, allow_pickle=True)
	np.save("output.npy", Ys, allow_pickle=True)
	print(Ts)
	print(Xs.shape)
	print(Ys.shape)
make_data(obs)





