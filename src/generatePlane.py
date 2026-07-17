import random
import math
from noise import noise
from generateHeightMap import generateHeightMap

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

def generateSlopeMap(heightMap):
    slopeMap = []
    
    height = len(heightMap)
    width = len(heightMap[0])
    
    for y in range(height):
        row = []
        for x in range(width):
            slope = getSlope(x, y, heightMap)
            row.append(slope)
        slopeMap.append(row)
    
    return slopeMap

def getSlope(x, y, heightMap):
    
    if x >= len(heightMap[0]) - 1:
        return 0
    if y >= len(heightMap[0]) - 1:
        return 0
    
    
    current = heightMap[y][x]
    
    right = heightMap[y][x+1]
    
    up = heightMap[y+1][x]
    
    slopeX = abs(right - current)
    slopeY = abs(up - current)
    
    return (slopeX + slopeY) / 2

def generateTerrainHeight(x, y, heightMap):
    height = heightMap[y][x]
    
    slope = getSlope(x, y, heightMap)
    
    finalHeight = applyRules(height, slope)
    
    return finalHeight

def applyRules(height, slope):   
    
    #Rules
    if height > 0:
        height = height ** 1.5
    else:
        height = -((-height) ** 1.5)
        
    if slope > 0.3:
        height *= 1.5
        
    return height

def getSlopeColour(slopeValue):
    
    #ensures value is between 0-1
    slope = max(0, min(slopeValue, 1))
    
    #RGB value
    return (slope, 0, 1 - slope, 1)

def generatePlane(width, height, frequency):
    spacing = 5
    gradient = generateGradient(width, height, spacing)
    heightMap = generateHeightMap(width, height, gradient, spacing)
    slopeMap = generateSlopeMap(heightMap)
    
    vertices = []
    faces = []
    colours = []
    
    #for the vertices it is also (x + 1) * (x + 1) amount of vertices
    for y in range(height + 1):
        for x in range(width + 1):
            heightValue = heightMap[y][x]
            slopeValue = slopeMap[y][x]
            finalHeight = applyRules(heightValue, slopeValue)
            vertices.append((x * frequency, y * frequency, finalHeight * 20))
            colours.append(getSlopeColour(slopeValue))
    
    #
    for y in range(height):
        for x in range(width):
            i = y * (width + 1) + x
            #all the differnet faces and we are just counting the vertices of points of the faces if you will
            faces.append((i, i+1, i + (width + 1) + 1, i + (width + 1)))
    
    return vertices, faces, colours