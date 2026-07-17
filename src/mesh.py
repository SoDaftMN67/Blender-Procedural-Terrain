import bpy 

def createMesh(name, vertices, faces, colours):
    
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
    
    
    ## All this section here is for colouring
    
    #creates vertex layer on the mesh one colour for every vertex
    colourLayer = mesh.color_attributes.new(name="Slope", type="FLOAT_COLOR", domain='POINT')
    
    #copy the generated colour into blender colour
    for i, colour, in enumerate(colours):
        colourLayer.data[i].color = colour
    
    #Access the node tree 
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    
    #create a node that reads mesh vertex colour attribute
    attributes = nodes.new("ShaderNodeVertexColor")
    attributes.layer_name = "Slope"
    
    #get default principled bsdf shader
    bsdf = nodes["Principled BSDF"]
    
    #Connects the vertex to the material base colour
    links.new(attributes.outputs["Color"], bsdf.inputs["Base Color"])
    
    #add it to the terrain object
    obj.data.materials.append(material)