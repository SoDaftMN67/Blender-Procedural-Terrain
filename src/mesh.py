import bpy 

def createMesh(name, vertices, faces):
    
    terrain = bpy.data.objects.get(name)
    
    if terrain is not None:
        print('Deleting terrain...')
        meshData = terrain.data
        bpy.data.objects.remove(terrain)
        bpy.data.meshes.remove(meshData)
      
        
    #creating the mesh  
    mesh = bpy.data.meshes.new(name)
    
    #assigning mesh data to an object
    obj = bpy.data.objects.new(name, mesh)
    
    #connecting the object to a scene, this is jsut the current active scene
    bpy.context.scene.collection.objects.link(obj)
    
    #assign vertex colours
    material = bpy.data.materials.new("Slope Material")
    material.use_nodes = True
    
    #for now passing no edges
    mesh.from_pydata(vertices, [], faces)
    
    mesh.update()
    