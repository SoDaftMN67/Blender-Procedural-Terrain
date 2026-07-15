from noise import noise

def generateHeight(x, y, gradient, spacing):
    
    height = 0
    frequency = 1
    amplitude = 1
    
    octaves = 2
    
    for i in range(octaves):
        height += noise(x * frequency, y * frequency, gradient, spacing) * amplitude
        frequency *= 2
        amplitude *= 0.5
    
    return height

def generateHeightMap(width, height, gradient, spacing):
    
    heightMap = []
    
    for y in range(height + 1):
        row = []
        for x in range(width + 1):
            height = generateHeight(x, y, gradient, spacing)
            row.append(height)
            
        heightMap.append(row)
     
    return heightMap