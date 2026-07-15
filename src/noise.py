
def dotProduct(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

def fade(value):
    return 6 * (value**5) - 15 * (value**4) + 10 * (value**3)

def lerp(top, bottom, spacing):
    return top + (bottom - top) * spacing

def noise(x, y, gradient, spacing):

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
    top = lerp(tl, tr, u)
    bottom = lerp(bl, br, v)

    return lerp(top, bottom, v)