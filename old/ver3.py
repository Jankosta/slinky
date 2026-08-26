make_grid()

k = 1.0 # Spring Constant
L0 = 3.0 # Natural Spring Length
m = 1.0 # Block Mass
g = 1.0 # Gravity
b = 0.2 # Drag Coefficient

delta_t = 0.01 # Update Interval
changeRate = 200 # Real time = 100
time = 0 # For Graph

# Create Block 1
block1 = box(pos=vector(0, 3, 0), velocity=vector(0, 0, 0), color=color.red, make_trail=False, force=vector(0, 0, 0))
#attach_arrow(block1, "force", scale=2, color=color.red)
spring1 = helix(pos=vector(0, 6, 0), radius=0.8, texture=textures.metal, color=color.red)
spring1.axis = block1.pos - spring1.pos

# Create Block 2
block2 = box(pos=vector(0, 0, 0), velocity=vector(0, 0, 0), color=color.blue, make_trail=False, force=vector(0, 0, 0))
#attach_arrow(block2, "force", scale=2, color=color.red)
spring2 = helix(pos=block1.pos, radius=0.8, texture=textures.metal, color=color.blue)
spring2.axis = block2.pos - spring2.pos

# Create Block 3
block3 = box(pos=vector(0, -3, 0), velocity=vector(0, 0, 0), color=color.yellow, make_trail=False, force=vector(0, 0, 0))
#attach_arrow(block3, "force", scale=2, color=color.red)
spring3 = helix(pos=block2.pos, radius=0.8, texture=textures.metal, color=color.yellow)
spring3.axis = block3.pos - spring3.pos

# Graph Initialization
blockPGraph = gdisplay(title='Position vs. Time', xtitle='Time', ytitle='Position', width=520, height=230)
block1PCurve = gcurve(color=color.red)
block2PCurve = gcurve(color=color.blue)
block3PCurve = gcurve(color=color.yellow)

blockVGraph = gdisplay(title='Velocity vs. Time', xtitle='Time', ytitle='Position', width=520, height=230)
block1VCurve = gcurve(color=color.red)
block2VCurve = gcurve(color=color.blue)
block3VCurve = gcurve(color=color.yellow)

blockFGraph = gdisplay(title='Force vs. Time', xtitle='Time', ytitle='Position', width=520, height=230)
block1FCurve = gcurve(color=color.red)
block2FCurve = gcurve(color=color.blue)
block3FCurve = gcurve(color=color.yellow)


state = 2

def keyPressed(evt):
    global state
    if evt.key == 'z':
        state -= 1
        
scene.bind('keydown', keyPressed)        

while state == 2:
    rate(changeRate)
    
    # Block 1 Forces
    L1 = L0 - abs(spring1.axis.y) 
    drag1 = (-b) * block1.velocity.y
    force_spring1 = -k * L1
    block1.force.y = force_spring1 - (3*m) * g + drag1
    
    # Block 2 Forces
    spring2.pos = block1.pos 
    L2 = L0 - abs(spring2.axis.y) 
    drag2 = (-b) * block2.velocity.y
    force_spring2 = -k * L2
    block2.force.y = force_spring2 - (2*m) * g + drag2
    
    # Block 3 Forces
    spring3.pos = block2.pos 
    L3 = L0 - abs(spring3.axis.y) 
    drag3 = (-b) * block3.velocity.y
    force_spring3 = -k * L3
    block3.force.y = force_spring3 - m * g + drag3
    
    # Net Forces (Add tension from other springs)
    block1.force.y += -force_spring2
    block2.force.y += -force_spring3

    # Move Block 1
    block1.velocity.y += block1.force.y * delta_t / m
    block1.pos.y += block1.velocity.y * delta_t
    spring1.axis = block1.pos - spring1.pos
    
    # Move Block 2
    block2.velocity.y += block2.force.y * delta_t / m
    block2.pos.y += block2.velocity.y * delta_t
    spring2.axis = block2.pos - spring2.pos
    
    # Move Block 3
    block3.velocity.y += block3.force.y * delta_t / m
    block3.pos.y += block3.velocity.y * delta_t
    spring3.axis = block3.pos - spring3.pos

    # Update Graphs
    block1PCurve.plot(time, block1.pos.y)
    block2PCurve.plot(time, block2.pos.y)
    block3PCurve.plot(time, block3.pos.y)
    
    block1VCurve.plot(time, block1.velocity.y)
    block2VCurve.plot(time, block2.velocity.y)
    block3VCurve.plot(time, block3.velocity.y)
    
    block1FCurve.plot(time, block1.force.y)
    block2FCurve.plot(time, block2.force.y)
    block3FCurve.plot(time, block3.force.y)
    
    time += delta_t

spring1.visible = False

while state == 1:
    rate(changeRate)
    
    # Block 1 Forces
    drag1 = (-b) * block1.velocity.y
    force_spring1 = 0
    block1.force.y = force_spring1 - (3*m) * g + drag1
    
    # Block 2 Forces
    spring2.pos = block1.pos 
    L2 = L0 - abs(spring2.axis.y) 
    drag2 = (-b) * block2.velocity.y
    force_spring2 = -k * L2
    block2.force.y = force_spring2 - (2*m) * g + drag2
    
    # Block 3 Forces
    spring3.pos = block2.pos 
    L3 = L0 - abs(spring3.axis.y) 
    drag3 = (-b) * block3.velocity.y
    force_spring3 = -k * L3
    block3.force.y = force_spring3 - m * g + drag3
    
    # Net Forces (Add tension from other springs)
    block1.force.y += -force_spring2
    block2.force.y += -force_spring3

    # Move Block 1
    block1.velocity.y += block1.force.y * delta_t / m
    block1.pos.y += block1.velocity.y * delta_t
    spring1.axis = block1.pos - spring1.pos
    
    # Move Block 2
    block2.velocity.y += block2.force.y * delta_t / m
    block2.pos.y += block2.velocity.y * delta_t
    spring2.axis = block2.pos - spring2.pos
    
    # Move Block 3
    block3.velocity.y += block3.force.y * delta_t / m
    block3.pos.y += block3.velocity.y * delta_t
    spring3.axis = block3.pos - spring3.pos
  
    # Update Graphs
    block1PCurve.plot(time, block1.pos.y)
    block2PCurve.plot(time, block2.pos.y)
    block3PCurve.plot(time, block3.pos.y)
    
    block1VCurve.plot(time, block1.velocity.y)
    block2VCurve.plot(time, block2.velocity.y)
    block3VCurve.plot(time, block3.velocity.y)
    
    block1FCurve.plot(time, block1.force.y)
    block2FCurve.plot(time, block2.force.y)
    block3FCurve.plot(time, block3.force.y)
    
    time += delta_t

def make_grid():
    scene.background = color.white
    thickness = 0.02
    dx = 1
    xmax = 6
    x = -xmax
    
    # Create grid lines in the x direction
    while (x <= xmax):
        y = -15 
        gridline = curve(pos=[vector(x, y, -thickness)], color=color.black, radius=thickness)
        while (y <= xmax):
            gridline.append(vector(x, y, -thickness))
            y += dx
        x += dx

    # Create grid lines in the y direction
    y = -15
    while (y <= xmax):
        x = -xmax
        gridline = curve(pos=[vector(x, y, -thickness)], color=color.black, radius=thickness)
        while (x <= xmax):
            gridline.append(vector(x, y, -thickness))
            x += dx
        y += dx

    global ground
    return
