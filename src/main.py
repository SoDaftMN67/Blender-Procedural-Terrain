from mesh import createMesh
from generatePlane import generatePlane
def main():
    print('Hello world')
    
    #hard coded width and height for now
    width = 150
    height = 150
    frequency = 5
    vertices, faces, colours = generatePlane(width, height, frequency)
    
    
    createMesh("Terrain", vertices, faces, colours)
    

