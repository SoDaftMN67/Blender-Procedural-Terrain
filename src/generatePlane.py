def generatePlane(width, height):
    vertices = []
    faces = []
    
    #
    for y in range(height + 1):
        for x in range(width + 1):
            vertices.append((x, y, 0))
    
    #
    for y in range(height):
        for x in range(width):
            i = y * (width + 1) + x
            
            faces.append((i, i+1, i + (width + 1) + 1, i + (width + 1)))
    
    return vertices, faces