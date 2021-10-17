import bpy



class data:

    def __init__(self,object,scale,use_bone_size,wireframe):
        self.object = object
        self.scale = scale
        self.use_bone_size = use_bone_size
        self.wireframe = wireframe
        return
    
    def apply_pb(self,pb):
        pb.custom_shape = self.object
        pb.custom_shape_scale = self.scale
        pb.use_custom_shape_bone_size = self.use_bone_size
     
         
    def apply_eb(self,eb):
        eb.show_wire = self.wireframe
           
  
class abstract:

    def __init__(self):
        self.object = None
        return

    def collection(self,col):      
        self.object.select_set(True)
        bpy.ops.collection.objects_remove_all()
        col.objects.link(self.object)
        
    def get(self):
        return self.object
        
    def init(self):
        bpy.ops.mesh.primitive_cube_add(enter_editmode=False, align='WORLD', location=(0, -0.075, -0.071), scale=(.06, .13, 0.001))
        bpy.ops.object.transform_apply(location=True, rotation=False, scale=True)
        cube = bpy.context.selected_objects[0]
        cube.name = "controlshape_foot"
        self.object = cube
        cube.select_set(False)
        return self
      
class foot(abstract):

    def __init__(self):
        return

    def get(self):
        return self.object
        
    def init(self):
        bpy.ops.mesh.primitive_cube_add(enter_editmode=False, align='WORLD', location=(0, -0.075, -0.071), scale=(.06, .13, 0.001))
        bpy.ops.object.transform_apply(location=True, rotation=False, scale=True)
        cube = bpy.context.selected_objects[0]
        cube.name = "controlshape_foot"
        self.object = cube
        cube.select_set(False)
        return self
    
  
class circle_solid_z(abstract):

    def __init__(self):
        return

    def get(self):
        return self.object
        
    def init(self):
        bpy.ops.mesh.primitive_cylinder_add(vertices=24,radius=.25, depth=.001, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        cube = bpy.context.selected_objects[0]
        cube.name = "controlshape_circle_solid_z"
        self.object = cube
        cube.select_set(False)
        return self
      
class circle_solid_y(abstract):

    def __init__(self):
        return

    def get(self):
        return self.object
        
    def init(self):
        bpy.ops.mesh.primitive_cylinder_add(vertices=24,radius=.25, depth=.001, enter_editmode=False, align='WORLD', rotation=(1.5708, 0, 0), location=(0, 0, 0), scale=(1, 1, 1))
        bpy.ops.object.transform_apply(location=True, rotation=False, scale=True)
        cube = bpy.context.selected_objects[0]
        cube.name = "controlshape_circle_solid_y"
        self.object = cube
        cube.select_set(False)
        return self