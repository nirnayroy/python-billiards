#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import billiards

print(os.getcwd())  # print current working directory


# Quickstart
bld = billiards.Billiard()

fig_name = "_images/quickstart_1.svg"
bld.add_ball((2, 0), (4, 0), radius=1)
bld.evolve(end_time=10.0)
fig = billiards.visualize.plot(bld)
fig.savefig(fig_name)
print(fig_name)

fig2_name = "_images/quickstart_2.svg"
bld.add_ball((50, 18), (0, -9), radius=1, mass=2)
bld.evolve(14.0)
fig2 = billiards.visualize.plot(bld)
fig2.savefig(fig2_name)
print(fig2_name)


# Usage: Newton's cradle
anim_name = "_static/newtons_cradle.mp4"
bld = billiards.Billiard()
bld.add_ball((0, 0), (1, 0), 1)
bld.add_ball((3, 0), (0, 0), 1)
bld.add_ball((5.1, 0), (0, 0), 1)
bld.add_ball((7.2, 0), (0, 0), 1)
bld.add_ball((9.3, 0), (0, 0), 1)

anim = billiards.visualize.animate(bld, end_time=5)
anim.save(anim_name)
print(anim_name)
