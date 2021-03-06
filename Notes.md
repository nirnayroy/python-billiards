# Ideas
A list of features that might be useful, but for which I have no time and interest to actually implement them.

## Add type hints
mypy: http://mypy-lang.org/
flake8-typing-imports(?)
https://www.bernat.tech/the-state-of-type-hints-in-python/

## Improve documentation
- More details in the module docstrings
- Every module on its own page
- spellchecker? (sphinxcontrib.spelling is deprecated, but see cookiecutter-pylibrary for setup)
- Upload documentation to ReadTheDocs and extend README.md with badges and link to documentation

## Publish on PyPi
Use twine (twine>=1.11.0 if readme in markdown), use `twine check` instead of `setup.py check`.
https://packaging.python.org/guides/making-a-pypi-friendly-readme#validating-restructuredtext-markup

## More control of plot
- Animate: draw path taken by balls
- Improve CircleCollection.datalim (somehow rendering and get_path_collection_extents don't do the same thing with transform, transData and transOffset)

## More versatile visualize.interact
- Use mouse scroll wheel for zooming
- Draw balls as solid disks, use colors like matplotlib (but for dark mode?)
- Show/hide velocities as arrows starting at the balls center
- When paused drag-and-drop balls around and edit velocites by dragging-and-dropping the arrow tips

## Better Testing
- How to write proper tests for matplotlib?
- How to write proper tests for pyglet (or GUIs in general)?
- Make pyglet work with tox, currently I can't access pyglet.gl.GL_LINES when I run the tests via tox (pyglet.canvas.xlib.NoSuchDisplayException: Cannot connect to "None"), see commented fragments in test_visualize.py and the .model methods in obstacle.
- Rearrange config settings? Put pytest.ini in setup.cfg and everything else in tox.ini or use separate files for every tool?
- Use TravisCI (and other internet services?)

## More obstacles
Reference: DynamicalBilliards.jl
- Finite wall, but collision with the endpoints will be complicated (model ball-line collision like point-stadium collision)
- Rectangle, polygon (built from finite lines)
- Semicircle, Ellipse
- Quick access to standard billiard shapes (rectangle, stadium, ...)?

## Redesign ball updates
Ball state: use ball_initial_time: 1d array of floats, ball_initial_position: (n, 2)-array of positions, ball_initial_velocity: (n, 2)-array of velocities
In Billiards._move use
    ball_position = ball_initial_position + ball_initial_velocity * (time - ball_initial_time)
Advantage: better floating point accuraccy and maybe easier collision detection (not so many move-calls that update all balls)
Disadvantage: no inplace addition (maybe slower) and more elaborate calculation for dt (array multiply and array subtract with casting instead of array multiply with casting) which is probably slower

## Gravity
Make the balls fall "downwards" i.e.
- To Billiard.__init__ add gravity: np.ndarray of size 2
- In Billiard._move:
    self.balls_position += self.balls_velocity * dt + self.gravity / 2 * dt**2
    self.balls_velocity += self.gravity * dt
- Calculate time of impact for ball-ball collisions: don't change anything because all balls fall the same way (if we switch to frame of reference that accelerates with gravity, then the balls are not accelerated anymore. Thanks Einstein!)
- Calculate time of impact for ball-obstacle collisions: I dont't know, it might be complicated since obstacles remain stationary

## (Sliding) Friction and/or drag
Imagine that the balls roll on a flat horizontal table convert in cloth (this will be inconsistent with gravity but that's OK.)
Friction is a force of size F = mu * mass with a direction opposite of velocity.
We need to integrate a = mu to find the trajectory of the ball until it stops (this is a straight line which is reperameterised by a quadratic function).
Drag is a force similar to friction, but F is proportional to velocity^2 * size of ball, this is more complicated to integrate.
We can still use time of impact calculation, but we need to take care of the reparameterisation.



# Notes about Stuff
Particles with no radius are point particles
Particles with zero mass are massless and don't push others around
Particles with infinite mass are not pushed around by other particles
Obstacles always have an inside and an outside, collision happens only when a ball comes from the inside and moves towards the outside. This is because point particles on the obstacle
Docstring style: https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html#example-google
Billiards in Julia: https://juliadynamics.github.io/DynamicalBilliards.jl/dev/
Collision handling: https://en.wikipedia.org/wiki/Elastic_collision#Two-dimensional_collision_with_two_moving_objects

https://jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/
https://dbader.org/blog/write-a-great-readme-for-your-github-project
CI: see cookiecutter-pylibrary
Makefile instead of tox: see cookiecutter-pypackage

## Unused commands
python3 setup.py sdist bdist_wheel
sphinx-apidoc -f -o {toxinidir}/docs/api_reference {toxinidir}/src/billiards


## Badges in Readme
.. image:: https://img.shields.io/pypi/v/billiards.svg
    :target: https://pypi.python.org/pypi/billiards
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/borntyping/cookiecutter-pypackage-minimal.png
   :target: https://travis-ci.org/borntyping/cookiecutter-pypackage-minimal
   :alt: Latest Travis CI build status

