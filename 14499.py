d = [[0]*3 for _ in range(4)]

def right():
  temp = d[1][2]
  d[1][2] = d[1][1]
  d[1][1] = d[1][0]
  d[1][0] = d[3][1]
  d[3][1] = temp
def left():
  temp = d[1][0]
  d[1][0] = d[1][1]
  d[1][1] = d[1][2]
  d[1][2] = d[3][1]
  d[3][1] = temp
def up():
  temp = d[0][1]
  d[0][1] = d[1][1]
  d[1][1] = d[2][1]
  d[2][1] = d[3][1]
  d[3][1] = temp

def down():
  temp = d[3][1]
  d[3][1] = d[2][1]
  d[2][1] = d[1][1]
  d[1][1] = d[0][1]
  d[0][1] = temp

m, n, x, y, t = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]
dir = list(map(int, input().split()))


for i in range(t):
  if dir[i] == 1:
    if y+1 == n:
      continue
    right()
    y += 1
  elif dir[i] == 2:
    if y-1 == -1:
      continue
    left()
    y -= 1
  elif dir[i] == 3:
    if x-1 == -1:
      continue
    up()
    x -= 1
  else:
    if x+1 == m:
      continue
    down()
    x += 1

  if b[x][y] == 0:
    b[x][y] = d[3][1]
  else:
    d[3][1] = b[x][y]
    b[x][y] = 0

  print(d[1][1])
