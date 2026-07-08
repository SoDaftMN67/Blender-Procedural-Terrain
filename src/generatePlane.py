import random
import math

def generateGradient(width, height, spacing):
    cols = width // spacing + 1
    rows = height // spacing + 1
    
    gradientList = []
    
    for y in range(rows):
        row = []
        for x in range(cols):
            angle = random.uniform(0, 2 * math.pi)
            gradient = (math.cos(angle), math.sin(angle))
            row.append(gradient)
            
        gradientList.append(row)
        
    return gradientList

def dotProduct(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

def fade(value):
    return 6 * (value**5) - 15 * (value**4) + 10 * (value**3)

def getHeight(x, y, gradient, spacing):

    #get location of cells
    gridX = x // spacing
    gridY = y // spacing
    
    #clamping
    maxX = len(gradient[0]) - 2
    maxY = len(gradient) - 2
    
    gridX = max(0, min(gridX, maxX))
    gridY = max(0, min(gridY, maxY))
    
    #find how far it is into face
    localX = (x % spacing) / spacing
    localY = (y % spacing) / spacing
    
    #find the 4 points
    topLeft = gradient[gridY][gridX]
    topRight = gradient[gridY][gridX + 1]
    bottomLeft = gradient[gridY + 1][gridX]
    bottomRight = gradient[gridY + 1][gridX + 1]
    
    #Get distance from points
    distanceTL = (localX, localY)
    distanceTR = (localX - 1, localY)
    distanceBL = (localX, localY - 1)
    distanceBR = (localX-1,localY-1)
    
    tl = dotProduct(topLeft, distanceTL)
    tr = dotProduct(topRight, distanceTR)
    bl = dotProduct(bottomLeft, distanceBL)
    br = dotProduct(bottomRight, distanceBR)
    
    print(tl, tr, bl, br)
    print(localX, localY)
    
    #interloping
    u = fade(localX)
    v = fade(localY)
    top = tl + (tr - tl) * u
    bottom = bl + (br - bl) * v

    return x * 0.1 + (top + (bottom - top) * v) * 2


def generatePlane(width, height):
    spacing = 5
    scale = 1
    gradient = generateGradient(width, height, spacing)
    
    vertices = []
    faces = []
    
    #for the vertices it is also (x + 1) * (x + 1) amount of vertices
    for y in range(height + 1):
        for x in range(width + 1):
            vertices.append((x, y, getHeight(x, y, gradient, spacing)))
    
    #
    for y in range(height):
        for x in range(width):
            i = y * (width + 1) + x
            #all the differnet faces and we are just counting the vertices of points of the faces if you will
            faces.append((i, i+1, i + (width + 1) + 1, i + (width + 1)))
    
    return vertices, faces