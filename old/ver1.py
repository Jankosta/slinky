make_grid()

k = 1.0 # Spring Constant
L0 = 4.0 # Natural Spring Length
m = 1.0 # Block Mass
g = 1.0 # Gravity
b = 0.2 # Drag Coefficient

delta_t = 0.01 # Update Interval
changeRate = 200 # Real time = 100
time = 0 # For Graph

block = box(pos=vector(0, 0.0, 0), velocity=vector(0, 0, 0), color=color.orange, make_trail=False, force=vector(0, 0, 0))
attach_arrow(block, "force", scale=2, color=color.red)
spring = helix(pos=vector(0, 6, 0), radius=0.8, texture=textures.metal, color=color.blue)
spring.axis = block.pos - spring.pos

# Graph Initialization
blockGraph = gdisplay(title='Position vs. Time', xtitle='Time', ytitle='Position', width=520, height=230)
blockCurve = gcurve(color=color.orange)

while (1):
    rate(changeRate)
    L = L0 - abs(spring.axis.y)  # Stretch from equilibrium
    drag = (-b) * block.velocity.y
    block.force.y = -k * L - m * g + drag 
    block.velocity.y += block.force.y * delta_t / m  # Change in velocity
    block.pos.y += block.velocity.y * delta_t  # Distance traveled gets added to block's pos
    spring.axis = block.pos - spring.pos

    # Update Graph
    blockCurve.plot(time, block.pos.y)
    time += delta_t

def make_grid():
  scene.background = color.white
  thickness = 0.02
  dx = 1
  xmax = 6
  x = -xmax
  while (x <= xmax):
    y = -xmax
    gridline = curve(pos=[vector(x,y,-thickness)],color=color.black,radius=thickness)
    while (y <= xmax):
      gridline.append(vector(x,y,-thickness))
      y = y + dx
    x = x + dx
  y = -xmax
  while (y <= xmax):
    x = -xmax
    gridline = curve(pos=[vector(x,y,-thickness)],color=color.black,radius=thickness)
    while (x <= xmax):
      gridline.append(vector(x,y,-thickness))
      x = x + dx
    y = y + dx
  global ground
  return
