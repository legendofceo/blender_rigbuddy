import bpy
RIGBUDDY_ARMA = bpy.data.texts["rigbuddy_arma.py"].as_module()

class rigshape_data:

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
        
class editbone_data():
    
    def apply(self,eb):
        eb.head = self.head
        eb.tail = self.tail
        eb.roll = self.roll
        
    def __init__(self,eb):
        self.head = eb.head
        self.tail = eb.tail
        self.roll = eb.roll    
        return

def set_bonelayer(eb,layer):
    eb.layers[layer] = True
        
def apply_eb_data(data,eb):
    data.apply(eb)  
    return eb 
 
def eb_anti(eb):
    head = eb.head.copy()
    tail = eb.tail.copy()
    dif_tail = head-tail
    eb.tail = (head+dif_tail)

def eb_flatten_z(eb):
    head = eb.head.copy()
    tail = eb.tail.copy()
    tail.z = head.z
    eb.tail = tail
    return eb 
   
def activate_arma(arma):
    bpy.context.view_layer.objects.active = bpy.data.objects[arma.name]
    selected_object = bpy.context.view_layer.objects.active
    active_arma = selected_object.data    
    return active_arma 

def new_eb(arma,id):
    active_arma = activate_arma(arma)            
    return active_arma.edit_bones.new(id)  

def copy_eb(arma,source_eb,new_id):
        active_arma = activate_arma(arma)    
        target = active_arma.edit_bones.new(new_id)
        target.head = source_eb.head
        target.tail = source_eb.tail
        target.roll = source_eb.roll
        return target
    
def copy_bone(arma,source_id,id):    
        active_arma = activate_arma(arma)
        eb = active_arma.edit_bones[source_id]
        head = eb.head
        tail = eb.tail
        roll = eb.roll
        eb = active_arma.edit_bones.new(id)
        eb.head = head
        eb.tail = tail
        eb.roll = roll
        return eb
       
def copy_bone_from_arma(source_arma,source_id,arma,id):
        
        active_arma = activate_arma(source_arma)
        eb = active_arma.edit_bones[source_id]
        head = eb.head
        tail = eb.tail
        roll = eb.roll
        active_arma = activate_arma(arma)
        eb = active_arma.edit_bones.new(id)
        eb.head = head
        eb.tail = tail
        eb.roll = roll
        return eb
                   
def duplicate_rbb_chain(rbb_chain):
    new_rbb_chain = []
    rba = rbb_chain[0].rba
    bpy.context.view_layer.objects.active = bpy.data.objects[rba.arma.name]
    selected_object = bpy.context.view_layer.objects.active
    arma = selected_object.data 
    bpy.ops.object.mode_set(mode='EDIT')
      
    for i, rbb in enumerate(rbb_chain):
        cb = arma.edit_bones.new(rbb.id)
        eb = rbb.get_eb()
        cb.head = eb.head
        cb.tail = eb.tail
        cb.matrix = eb.matrix
        if(i!=0):
            cb.parent = last_bone
        else:
            cb.parent = eb.parent
        last_bone = cb
        new_rbb = RIGBUDDY_ARMA.bone(cb.name)
        rba.reg_rbb(new_rbb)   
        new_rbb_chain.append(new_rbb)
              
    return new_rbb_chain