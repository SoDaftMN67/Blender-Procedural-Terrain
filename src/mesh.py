import bpy 

def createMesh(name, vertices, faces):
    
    #creating the mesh  
    mesh = bpy.data.meshes.new(name)
    
    #assigning mesh data to an object
    obj = bpy.data.objects.new(name, mesh)
    
    #connecting the object to a scene, this is jsut the current active scene
    bpy.context.scene.collection.objects.link(obj)
    
    #for now passing no edges
    mesh.from_pydata(vertices, [], faces)
    
    mesh.update()
    