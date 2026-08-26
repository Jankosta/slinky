make_grid()

k = 1.0 # Spring Constant
L0 = 4.0 # Natural Spring Length
mA = 1.0 # Block A Mass
mB = 1.0 # Block B Mass
b = 0.2 # Drag Coefficient
blockGap = 6.0 # Initial gap between blocks

delta_t = 0.01 # Update Interval
changeRate = 200 # Real time = 100
time = 0 # For Graph

blockA = box(pos=vector(-blockGap/2, 0.0, 0), velocity=vector(0, 0, 0), color=color.red, make_trail=False, force=vector(0, 0, 0))
blockB = box(pos=vector(blockGap/2, 0.0, 0), velocity=vector(0, 0, 0), color=color.green, make_trail=False, force=vector(0, 0, 0))

attach_arrow(blockA, "force", scale=1.5, color=color.yellow)
attach_arrow(blockB, "force", scale=1.5, color=color.purple)

spring = helix(pos=blockA.pos, axis=blockB.pos-blockA.pos, radius=0.8, texture=textures.metal, color=color.magenta)

blockGraph = gdisplay(title='Position vs. Time', xtitle='Time', ytitle='Position', width=520, height=230)
blockACurve = gcurve(color=color.red, label="Block A")
blockBCurve = gcurve(color=color.green, label="Block B")

while (1):
    rate(changeRate)
    
    L = L0 - abs(spring.axis.x) # Stretch from equilibrium
    Fs = (-k)  * L # Spring force
    
    dragA = (-b) * blockA.velocity.x
    dragB = (-b) * blockB.velocity.x
    
    blockA.force.x = Fs + dragA
    blockB.force.x = -Fs + dragB
    
    blockA.velocity.x += blockA.force.x * delta_t / mA
    blockB.velocity.x += blockB.force.x * delta_t / mB

    blockA.pos.x += blockA.velocity.x * delta_t
    blockB.pos.x += blockB.velocity.x * delta_t
    
    spring.pos = blockA.pos
    spring.axis = blockB.pos - blockA.pos
    
    # Update Graph
    blockACurve.plot(time, blockA.pos.x)
    blockBCurve.plot(time, blockB.pos.x)
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
  vertical_line = curve(pos=[vector(0, -xmax, 0), vector(0, xmax, 0)], color=color.black, radius=0.0)
  global ground
  return
