
#importing esssential libraries
import numpy as np
import keyboard
from matplotlib import pyplot as plt
import torch
#gpu acceleration
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("Using GPU:", torch.cuda.get_device_name(0))
else:
    device = torch.device("cpu")
    print("Using CPU")
#initializing variables
#size of the map
size = 50
#distance of shot
shootindex = 0
#game map
map = []

shooting = False
#creating random map 
for i in range(size):
    map.append([])
    for j in range(size):
        map[i].append(list(np.random.uniform(0,1,3)))
#PI shortcut
pi = np.pi
#camera position and angle
cx, cy = (1, np.random.randint(1,size-1))
map[cx][cy] = 0
#enemy position and health
ex = []
hp = []

x, y = (cx, cy)
rot = pi / 4
#making better map
while True:
    testx, testy = (x, y)
    if(np.random.uniform() > 0.5):
        testx = testx + np.random.choice([-1,1]) 
    else:
        testy = testy + np.random.choice([-1,1])
    if testx > 0 and testx < size -1 and testy > 0 and testy < size -1:
        x, y = (testx, testy)
        map[x][y] = 0
        if x == size -2:
            exitx, exity = (x,y)
            break

for x in range(1,size-1):
  for y in range(1,size-1):
    if map[int(x)][int(y)] != 0:
        if map[int(x+1)][int(y)] == 0 and map[int(x-1)][int(y)] == 0 and map[int(x)][int(y+1)] == 0 and map[int(x)][int(y-1)] ==0 and [(int(x), int(y))] not in ex:
          ex.append([(int(x), int(y))])
          hp.append(10)
#main game loop
while True:
   # floor and sky lines
  plt.hlines(-0.6, 0, 60, colors= "gray", lw = 210, alpha = 0.5)
  plt.hlines(0.6, 0, 60, colors= "lightblue", lw = 210, alpha = 0.5)
  tilex, tiley, tilec = ([],[],[])
    #raytracing player fov loop
  for i in range(0,60,2):
    shooting = False
    roti = rot + np.deg2rad(i - 30)
    x, y = (cx, cy)
    sin, cos = (np.sin(roti), np.cos(roti))
    n = 0
    while True:
        #actual ray tracing
      xx, yy = (x, y)
      x, y = (x + cos * 0.025, y + sin * 0.025)
      n = n + 1
        #floor scatter plot (not used)
      if abs(int(3*xx)-int(3*x)) > 0 or abs(int(3*yy)-int(3*y)) > 0:
        tilex.append(i)
        tiley.append(-1/(n*0.02))
        if int(x) == exitx and int(y) == exity:
            #exit tile coloring
            tilec.append("b")
        else:    
            tilec.append('w')
      if map[int(x)][int(y)] != 0:
        #height of lines
        h = np.clip(1 / (n * 0.02), 0, 1)
        #random coloring
        c = np.asarray(map[int(x)][int(y)])*(0.3+0.7*h**2)
            #enemy code
        if map[int(x+1)][int(y)] == 0 and map[int(x-1)][int(y)] == 0 and map[int(x)][int(y)+1] == 0 and map[int(x)][int(y)-1] == 0:
              #checking if enemy not already registered
          if [(int(x), int(y))] in ex:    
            #setting enemy color to red 
            c = (0.65,0,0, 0.75*hp[ex.index([(int(x), int(y))])]/10)
        break
    
    #if not is_occluded(cx, cy, roti, map, increment=0.02):
           #continue
#drawing
    plt.vlines(i/2, -h, h, lw=18, colors = c)
  
  plt.axis("off")
  plt.tight_layout()
  plt.axis([0,25, -1, 1])
  plt.scatter(tilex, tiley, c = tilec)
  plt.draw()
  plt.pause(0.0005)
  
  plt.clf()
  x, y = (cx, cy)
  key = keyboard.read_key()
  #movement
  if key == 'up':
    for i in range(10):
      x, y = (x + 0.055*np.cos (rot), y + 0.055*np.sin (rot) )
    dx = exitx-x
    dy = exity-y
 
  if key == 'down':
    for i in range(10):
      x, y = (x - 0.055*np.cos (rot) , y - 0.055*np.sin(rot) )
    dx = exitx-x
    dy = exity-y

  if key == 'left':
    for i in range(10):
        rot = rot - pi/180
  if key =='right':
    for i in range(10):
        rot = rot + pi/180
  if key == 'esc':
    break
  #shooting
  if key == "space":
    shooting = True
  if shooting:
    rotx = rot
    while shootindex < 10: #shooting distance
        #shooting spread
      for j in range(0, 10):
        rotx = rot + np.deg2rad(j - 5)
        for i in range(len(ex)):
            #shooting raytracing
          if(0 != map[int(x + shootindex*np.cos (rotx))][int( y + shootindex*np.sin (rotx))] and [(int(x + shootindex*np.cos (rotx)), int( y + shootindex*np.sin (rotx)))] not in ex):
              shootindex = 10
              break
          if(ex[i] == [(int(x + shootindex*np.cos (rotx)), int( y + shootindex*np.sin (rotx)))]):
            #damaging enemies
            if hp[i] > 0:
              hp[i] = hp[i]-0.2
              shootindex == 10
              break
            else:
                #killing enemies
                ex.remove(ex[i])
                hp.remove(hp[i])
                map[int(x + shootindex*np.cos (rotx))][ int( y +shootindex*np.sin (rotx))] = 0
                plt.draw()
                break
            
      shootindex = shootindex + 0.5
    shootindex = 0
   #exit code
  if map [int (x)] [int (y) ] == 0 :
    if int(cx) == exitx and int(cy) == exity:
      break
    cx, cy = (x,y)
  
plt.close()