# Scene Settings
make_grid()
scene.width = 200
scene.height = 525
scene.center = vector(0, -12, 0)
scene.range = 7

k = 1.25 # Spring Constant
L0 = 3.5 # Natural Spring Length
m = 1.0 # Block Mass
g = 1.0 # Gravity
b = 0.20 # Drag Coefficient

delta_t = 0.01 # Update Interval
changeRate = 200 # Real time = 100
time = 0 # For Graph

# Create Block 1
block1 = box(pos=vector(0, 3, 0), velocity=vector(0, 0, 0), color=color.orange, make_trail=False, force=vector(0, 0, 0))
spring1 = helix(pos=vector(0, 6, 0), radius=0.8, texture=textures.metal, color=color.orange)
spring1.axis = block1.pos - spring1.pos

# Create Block 2
block2 = box(pos=vector(0, 0, 0), velocity=vector(0, 0, 0), color=color.blue, make_trail=False, force=vector(0, 0, 0))
spring2 = helix(pos=block1.pos, radius=0.8, texture=textures.metal, color=color.blue)
spring2.axis = block2.pos - spring2.pos

# Create Block 3
block3 = box(pos=vector(0, -3, 0), velocity=vector(0, 0, 0), color=color.green, make_trail=False, force=vector(0, 0, 0))
spring3 = helix(pos=block2.pos, radius=0.8, texture=textures.metal, color=color.green)
spring3.axis = block3.pos - spring3.pos

# Create Block 4
block4 = box(pos=vector(0, -6, 0), velocity=vector(0, 0, 0), color=color.black, make_trail=False, force=vector(0, 0, 0))
spring4 = helix(pos=block3.pos, radius=0.8, texture=textures.metal, color=color.black)
spring4.axis = block4.pos - spring4.pos

# Create Block 5
block5 = box(pos=vector(0, -9, 0), velocity=vector(0, 0, 0), color=color.yellow, make_trail=False, force=vector(0, 0, 0))
spring5 = helix(pos=block4.pos, radius=0.8, texture=textures.metal, color=color.yellow)
spring5.axis = block5.pos - spring5.pos

# Create CoM Sphere
comSphere = sphere(pos=vector(-2, ((block1.pos.y + block2.pos.y + block3.pos.y + block4.pos.y + block5.pos.y) / 5), 0), radius=0.5, color=color.red)

# Graph Initialization
blockPGraph = gdisplay(title='Position vs. Time', xtitle='Time', ytitle='Position', width=520, height=230)
block1PCurve = gcurve(color=color.orange)
block2PCurve = gcurve(color=color.blue)
block3PCurve = gcurve(color=color.green)
block4PCurve = gcurve(color=color.black)
block5PCurve = gcurve(color=color.yellow)

comGraph = gdisplay(title='CoM Position vs. Time', xtitle='Time', ytitle='Position', width=520, height=230)
comSpherePCurve = gcurve(color=color.red)
expectedCurve = gdots(color=color.purple)

blockVGraph = gdisplay(title='Velocity vs. Time', xtitle='Time', ytitle='Velocity', width=520, height=230)
block1VCurve = gcurve(color=color.orange)
block2VCurve = gcurve(color=color.blue)
block3VCurve = gcurve(color=color.green)
block4VCurve = gcurve(color=color.black)
block5VCurve = gcurve(color=color.yellow)

state = 2
def zPressed(press):
    global state
    if press.key == 'z':
        state -= 1
scene.bind('keydown', zPressed)        

while state == 2:
    rate(changeRate)
    
    # Block 1 Forces
    L1 = L0 - abs(spring1.axis.y) 
    drag1 = (-b) * block1.velocity.y
    Fs1 = -k * L1
    block1.force.y = Fs1 - m * g + drag1
    
    # Block 2 Forces
    spring2.pos = block1.pos 
    L2 = L0 - abs(spring2.axis.y) 
    drag2 = (-b) * block2.velocity.y
    Fs2 = -k * L2
    block2.force.y = Fs2 - m * g + drag2
    
    # Block 3 Forces
    spring3.pos = block2.pos 
    L3 = L0 - abs(spring3.axis.y) 
    drag3 = (-b) * block3.velocity.y
    Fs3 = -k * L3
    block3.force.y = Fs3 - m * g + drag3
    
    # Block 4 Forces
    spring4.pos = block3.pos 
    L4 = L0 - abs(spring4.axis.y) 
    drag4 = (-b) * block4.velocity.y
    Fs4 = -k * L4
    block4.force.y = Fs4 - m * g + drag4
    
    # Block 5 Forces
    spring5.pos = block4.pos 
    L5 = L0 - abs(spring5.axis.y) 
    drag5 = (-b) * block5.velocity.y
    Fs5 = -k * L5
    block5.force.y = Fs5 - m * g + drag5
    
    # Net Forces (Factor in tension from bottom springs)
    block1.force.y -= Fs2
    block2.force.y -= Fs3
    block3.force.y -= Fs4
    block4.force.y -= Fs5

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
    
    # Move Block 4
    block4.velocity.y += block4.force.y * delta_t / m
    block4.pos.y += block4.velocity.y * delta_t
    spring4.axis = block4.pos - spring4.pos
    
    # Move Block 5
    block5.velocity.y += block5.force.y * delta_t / m
    block5.pos.y += block5.velocity.y * delta_t
    spring5.axis = block5.pos - spring5.pos
    
    # Move CoM
    comSphere.pos.y = (block1.pos.y + block2.pos.y + block3.pos.y + block4.pos.y + block5.pos.y) / 5

    # Update Graphs
    block1PCurve.plot(time, block1.pos.y)
    block2PCurve.plot(time, block2.pos.y)
    block3PCurve.plot(time, block3.pos.y)
    block4PCurve.plot(time, block4.pos.y)
    block5PCurve.plot(time, block5.pos.y)
    
    comSpherePCurve.plot(time, comSphere.pos.y)
    
    block1VCurve.plot(time, block1.velocity.y)
    block2VCurve.plot(time, block2.velocity.y)
    block3VCurve.plot(time, block3.velocity.y)
    block4VCurve.plot(time, block4.velocity.y)
    block5VCurve.plot(time, block5.velocity.y)
    
    time += delta_t

spring1.visible = False

block1PCurve.delete()
block2PCurve.delete()
block3PCurve.delete()
block4PCurve.delete()
block5PCurve.delete()

comSpherePCurve.delete()

block1VCurve.delete()
block2VCurve.delete()
block3VCurve.delete()
block4VCurve.delete()
block5VCurve.delete()

y_i = comSphere.pos.y
v_i = (block1.velocity.y + block2.velocity.y + block3.velocity.y + block4.velocity.y + block5.velocity.y) / 5

time = 0
counter = 0

while state == 1:
    rate(changeRate)
    
    scene.center.y = comSphere.pos.y
    
    # Block 1 Forces
    drag1 = (-b) * block1.velocity.y
    Fs1 = 0
    block1.force.y = Fs1 - m * g
    
    # Block 2 Forces
    spring2.pos = block1.pos 
    L2 = L0 - abs(spring2.axis.y) 
    drag2 = (-b) * block2.velocity.y
    Fs2 = -k * L2
    block2.force.y = Fs2 - m * g
    
    # Block 3 Forces
    spring3.pos = block2.pos 
    L3 = L0 - abs(spring3.axis.y) 
    drag3 = (-b) * block3.velocity.y
    Fs3 = -k * L3
    block3.force.y = Fs3 - m * g
    
    # Block 4 Forces
    spring4.pos = block3.pos 
    L4 = L0 - abs(spring4.axis.y) 
    drag4 = (-b) * block4.velocity.y
    Fs4 = -k * L4
    block4.force.y = Fs4 - m * g
    
    # Block 5 Forces
    spring5.pos = block4.pos 
    L5 = L0 - abs(spring5.axis.y) 
    drag5 = (-b) * block5.velocity.y
    Fs5 = -k * L5
    block5.force.y = Fs5 - m * g
    
    # Net Forces (Factor in tension from other springs)
    block1.force.y -= Fs2
    block2.force.y -= Fs3
    block3.force.y -= Fs4
    block4.force.y -= Fs5

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
    
    # Move Block 4
    block4.velocity.y += block4.force.y * delta_t / m
    block4.pos.y += block4.velocity.y * delta_t
    spring4.axis = block4.pos - spring4.pos
    
    # Move Block 5
    block5.velocity.y += block5.force.y * delta_t / m
    block5.pos.y += block5.velocity.y * delta_t
    spring5.axis = block5.pos - spring5.pos
    
    # Move CoM and Calculate Expected CoM
    comSphere.pos.y = (block1.pos.y + block2.pos.y + block3.pos.y + block4.pos.y + block5.pos.y) / 5
    comExpected = y_i + v_i * time - 0.5 * g * time ** 2

    # Update Graphs
    block1PCurve.plot(time, block1.pos.y)
    block2PCurve.plot(time, block2.pos.y)
    block3PCurve.plot(time, block3.pos.y)
    block4PCurve.plot(time, block4.pos.y)
    block5PCurve.plot(time, block5.pos.y)
    
    comSpherePCurve.plot(time, comSphere.pos.y)
    if counter % int(0.5 / delta_t) == 0:
        expectedCurve.plot(time, comExpected)
    
    block1VCurve.plot(time, block1.velocity.y)
    block2VCurve.plot(time, block2.velocity.y)
    block3VCurve.plot(time, block3.velocity.y)
    block4VCurve.plot(time, block4.velocity.y)
    block5VCurve.plot(time, block5.velocity.y)
    
    if comSphere.pos.y <= -120:
        state = 0
    
    time += delta_t
    counter += 1

def make_grid():
    scene.background = color.white
    thickness = 0.02
    dx = 2
    xmax = 6
    x = -xmax
    while (x <= xmax):
        y = -30
        gridline = curve(pos=[vector(x, y, -thickness)], color=color.black, radius=thickness)
        while (y <= xmax):
            gridline.append(vector(x, y, -thickness))
            y += dx
        x += dx
    y = -30
    while (y <= xmax):
        x = -xmax
        gridline = curve(pos=[vector(x, y, -thickness)], color=color.black, radius=thickness)
        while (x <= xmax):
            gridline.append(vector(x, y, -thickness))
            x += dx
        y += dx
    for h in range(-120, 1, 10): 
        horizontal_line = curve(pos=[vector(-xmax, h, -thickness)], color=color.red, radius=thickness)
        for x in range(-xmax, xmax + 1): 
            horizontal_line.append(vector(x, h, -thickness))
    global ground
    return

