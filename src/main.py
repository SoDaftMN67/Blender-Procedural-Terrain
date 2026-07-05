from mesh import createMesh
from generatePlane import generatePlane
def main():
    print('Hello world')
    
    #hard coded width and height for now
    width = 10
    height = 10
    vertices, faces = generatePlane(width, height)
    
    
    createMesh("Terrain", vertices, faces)
    

