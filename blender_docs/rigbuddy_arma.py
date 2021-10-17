import bpy

class armature:

    
    def set_armature(self,arma):
        self.arma = arma
        return self
    
    def reg_rbb(self,rbb):
        rbb.set_rba(self)
        self.bones_dict[rbb.id] = rbb
        self.bones.append(rbb)
        return rbb
        
    def get_rbb(self,id):
        return self.bones_dict[id]
     
    def make_active(self):
        bpy.context.view_layer.objects.active = bpy.data.objects[self.arma.name]
        selected_object = bpy.context.view_layer.objects.active
        active_arma = selected_object.data    
        return active_arma
               
    def __init__(self):
        self.bones_dict = {}
        self.bones = [] 
 
class editbone_data:
        
    def __init__(self,eb):
        self.head = eb.head
        self.tail = eb.tail
        self.roll = eb.roll
               
class bone:

    def new(self,rba,id):
        self.set_rba(rba)
        self.set_id(id)
        active_arma = rba.make_active()   
        bpy.ops.object.mode_set(mode='EDIT')
        active_arma.edit_bones.new(self.id)
        return self

    def link(self,rba,id):
        self.set_rba(rba)
        self.set_id(id)        
        return self
    
    def copy(self,source_rba,source_id,rba,id):
        self.set_rba(rba)
        self.set_id(id)          
        source_rbb = bone().link(source_rba,source_id)
        eb_data = source_rbb.get_eb_data()
        new_rbb = bone().new(rba,id)
        new_rbb.set_eb_data(eb_data)       
        return self
    
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