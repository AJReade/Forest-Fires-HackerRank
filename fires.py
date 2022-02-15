import copy

fLines = []
for i in range (10) :
  fLines.append(list(input()))
  fLines[i].pop()

time = 0

def getAdjacents(n, m, lines) :
  adjacent = {"above": 0, "below": 0, "right": 0, "left": 0}
  for i in range (-1, 2):
    for j in range(-1, 2):
      if i == 0 and j == 0 :
        continue
      try :
        if i == 0 and j == 1 :
          adjacent["right"] = lines[n+0][m+1]
        elif i == 0 and j == -1 :
          adjacent["left"] = lines[n+0][m-1]
        elif i == 1 and j == 0 :
          adjacent["below"] = lines[n+1][m+0]
        elif i == -1 and j == 0 :
          adjacent["above"] = lines[n-1][m+0]
      except IndexError:
        continue
  return adjacent

def getFireTrees(n,m,lines) :
  trees = []
  adjacents = getAdjacents(n,m,lines)
  for ob in adjacents :
    if adjacents[ob] == 'T':
      if ob == 'above':
        trees.append([n-1,m])
      elif ob == 'below':
        trees.append([n+1,m])
      elif ob == 'right':
        trees.append([n,m+1])
      else:
        trees.append([n,m-1])

  return trees

# def getWater(n,m) :
#   trees = []
#   adjacents = getAdjacents(i,j)
#   for ob in ajacents :
#     if adjacents[ob] == 'W':
#       if ob == 'above':
#         trees.append([n+1,m])
#       elif ob == 'below':
#         trees.append([n-1,m])
#       elif ob == 'right':
#         trees.append([n,m+1])
#       else:
#         trees.append([n,m-1])

#   return trees


def getFireWater(n,m, lines) :
  water = []
  for i in range (-1, 2):
    for j in range(-1, 2):
      try :
        obj = lines[n+i][m+j]
      except IndexError :
        continue
      if obj == 'W' or obj == 'B':
        water.append([n+i,m+j])

  return water



def containsTrees (lines):
  for i in lines:
    for j in i:
      if j == 'T':
        return True
  return False


def checkFireContained(lines) :
  for i in range(len(lines)):
    for j in range(len(lines[i])):
      if lines[i][j] == "F":
        adjacents = getAdjacents(i,j, lines)
        for ob in adjacents :
          if adjacents[ob] == 'T' :
            return False
  return True

# def replaceWater(n,m, v) :
#     lines[n][m] = v


def checkCanBurn (n,m,lines) :
  adjacents = getAdjacents(n,m,lines)
  for ob in adjacents :
    if adjacents[ob] == 'W' :
      return False
  return True

def incrementTime() :
  global time
  time += 1


def prettyPrint(lines):
  for i in lines:
    print (i)



def main() :
  if checkFireContained(fLines):
    return -1

  else:
    replacement = True
    nextToTree = True
    while(replacement and nextToTree) :
      linesTemp = copy.deepcopy(fLines)
      replacement = False
      nextToTree = False

      for n in range(len(linesTemp)):
        for m in range(len(linesTemp[n])):
          if linesTemp[n][m] == 'F':
            trees = getFireTrees(n,m,linesTemp)
            if trees != [] :
              nextToTree = True
              for tree in trees:
                if checkCanBurn(tree[0],tree[1],linesTemp) :
                  fLines[tree[0]][tree[1]] = 'F'
                  replacement = True

            water = getFireWater(n,m,linesTemp)
            if water != []:
              for w in water:
                if linesTemp[w[0]][w[1]] == 'B':
                  fLines [w[0]][w[1]] = '.'
                  replacement = True
                else:
                  fLines [w[0]][w[1]] = 'B'
                  replacement = True


      incrementTime()

    if containsTrees(fLines):
      return -1
    else:
      return (time - 1)


print(main())
