from enum import Enum

class TerrainTypes(Enum):
    WATER = 0
    BEACH = 1
    PLAINS = 2
    HILLS = 3
    MOUNTAINS = 4
    CLIFF = 5
    
def getTerrainType(height, slope):
    
    #place holder rules for now may or may not change in the future
    if height < -0.2:
        return TerrainTypes.WATER
    if height < -0.1:
        return TerrainTypes.BEACH
    if slope > 0.6:
        return TerrainTypes.CLIFF
    if height > 0.7:
        return TerrainTypes.MOUNTAINS
    if height > 0.3:
        return TerrainTypes.HILLS
    
    return TerrainTypes.PLAINS

def getTerrainColour(terrainType):
    
    #return a rgba value depending on terrain type
    if terrainType == TerrainTypes.WATER:
        return (0.0, 0.3, 0.8, 1.0)
    
    elif terrainType == TerrainTypes.BEACH:
        return (0.9, 0.8, 0.5, 1.0)
    
    elif terrainType == TerrainTypes.PLAINS:
        return (0.2, 0.7, 0.2, 1.0)
    
    elif terrainType == TerrainTypes.HILLS:
        return (0.1, 0.5, 0.1, 1.0)
    
    elif terrainType == TerrainTypes.MOUNTAINS:
        return (0.5, 0.5, 0.5, 1.0)
    
    elif terrainType == TerrainTypes.CLIFF:
        return (0.35, 0.25, 0.15, 1.0)