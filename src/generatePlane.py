import random
import math

def getHeight(x, y):
    return (math.sin(x * 0.5) * 2 + math.cos(y * 0.5) * 2)

def generatePlane(width, height):
    
    vertices = []
    faces = []
    
    #for the vertices it is also (x + 1) * (x + 1) amount of vertices
    for y in range(height + 1):
        for x in range(width + 1):
            vertices.append((x, y, getHeight(x, y)))
    
    #
    for y in range(height):
        for x in range(width):
            i = y * (width + 1) + x
            #all the differnet faces and we are just counting the vertices of points of the faces if you will
            faces.append((i, i+1, i + (width + 1) + 1, i + (width + 1)))
    
    return vertices, faces