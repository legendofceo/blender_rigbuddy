import bpy

def from_new(rba,id):
        new_bone = rigbuddy_bone()
        new_bone.set_rba(rba)
        new_bone.set_id(id)
        active_arma = rba.make_active()   
        bpy.ops.object.mode_set(mode='EDIT')
        active_arma.edit_bones.new(id)
        return new_bone

def from_link(rba,id):
        new_bone = rigbuddy_bone()
        new_bone.set_rba(rba)
        new_bone.set_id(id)        
        return new_bone
  
def from_copy_id(source_rba,source_id,rba,id):
        new_bone = rigbuddy_bone()
        new_bone.set_rba(rba)
        new_bone.set_id(id)          
        source_rbb = from_link(source_rba,source_id)
        eb_data = source_rbb.get_eb_data()
        new_rbb = from_new(rba,id)
        new_rbb.set_eb_data(eb_data)       
        return new_bone

def from_copy_rbb(source_rbb,rba,id):
        eb_data = source_rbb.get_eb_data()
        new_rbb = from_new(rba,id)      
        new_rbb.set_eb_data(eb_data)       
        return new_rbb
        
class editbone_data:
        
    def __init__(self,eb):
        self.head = eb.head
        self.tail = eb.tail
        self.roll = eb.roll
               
class rigbuddy_bone:
    
    def parent_to_rbb(self,rbb):
        active_arma = self.rba.make_active()   
        bpy.ops.object.mode_set(mode='EDIT')
        target_eb = active_arma.edit_bones[rbb.id]
        active_arma.edit_bones[self.id].parent = target_eb       
        return self
    
    def get_leader_id(self):
        return self.id
    
    def __init__(self):
        return
    
    def set_id(self,id):
        self.id = id
        return self
    
    def set_rba(self,rba):
        self.rba = rba
        return self
     
    def get_eb_data(self):
        return editbone_data(self.get_eb())
   
    def set_eb_data(self,data):
        eb = self.get_eb()
        eb.head = data.head
        eb.tail = data.tail
        eb.roll = data.roll
        return self
        
    def get_eb(self):
        bpy.context.view_layer.objects.active = bpy.data.objects[self.rba.arma.name]
        selected_object = bpy.context.view_layer.objects.active
        arma = selected_object.data    
        bpy.ops.object.mode_set(mode='EDIT')
        return arma.edit_bones[self.get_leader_id()]
        
    def match_rbb(self,rbb_to_match):
        goal_eb = rbb_to_match.get_eb()
        head = goal_eb.head
        tail = goal_eb.tail
        roll = goal_eb.roll
        
        eb = self.get_eb()
        eb.head = head
        eb.tail = tail
        eb.roll = roll
        return self  
    
    def get_pb(self):
        bpy.ops.object.mode_set(mode='POSE')
        pb = self.rba.arma.pose.bones.get(self.id)
        return pb
  
    def set_tail(self,vector):
        eb = self.get_eb()
        eb.tail = vector
        return self 
    
    def set_head(self,vector):
        eb = self.get_eb()
        eb.head = vector
        return self 
    
    def get_tail(self):
        return self.get_eb().tail.copy()
    
        
    def get_head(self):
        return self.get_eb().head.copy()
    
    def connect(self,bool):
        self.get_eb().use_connect = bool
        return self