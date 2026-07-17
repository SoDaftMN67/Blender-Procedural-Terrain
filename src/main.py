from mesh import createMesh
from generatePlane import generatePlane
def main():
    print('Hello world')
    
    #hard coded width and height for now
    width = 100
    height = 100
    frequency = 5
    vertices, faces, colours = generatePlane(width, height, frequency)
    
    
    createMesh("Terrain", vertices, faces, colours)
    

