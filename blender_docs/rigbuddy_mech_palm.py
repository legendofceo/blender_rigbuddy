import bpy

RBS = bpy.data.texts["rigbuddy_statics.py"].as_module()


class rigbuddy_mech_palm:
        
    def __init__(self,arma,axis_index,axis):    
        self.arma = arma
        self.axis_index = axis_index
        self.axis = axis 
        
        self.n_palm = "palm"
        self.palm_finger_num = 4
        
        self.abr_control = "c_"
        self.abr_mechanism = "m_"
        
        
        self.rigshape_c_palm = RBS.rigshape_data(bpy.data.objects['rigshape_palm'],24.0,True,True)        
        return    
        
    def init(self):
        
        self.id_palms = []
        
        for i in range(self.palm_finger_num):
            self.id_palms.append(self.n_palm+str(i+1)+self.axis)
        
        self.id_c_palm = self.abr_control+self.n_palm+self.axis
        return self
        
        
    def set_source(self,arma):         
        active_arma = RBS.activate_arma(arma) 
        bpy.ops.object.mode_set(mode='EDIT')        
        self.ebd_arr= []
        for i, f in enumerate(self.id_palms):
                self.ebd_arr.append(RBS.editbone_data(active_arma.edit_bones[f]))
        return self
                 
    def set_layers(self,bone_basic,control_basic):
        self.layer_bone_basic = bone_basic
        self.layer_control_basic = control_basic
        return self
    
    def set_bonegroups(self,bonegroup_control):
        self.bonegroup_control = bonegroup_control
        return self
                
    def set_palm_parent_id(self,id):
        self.id_palm_parent = id
        return
    
    def set_control_scale(self,control_scale):
        self.control_scale = control_scale    
        return
        
    def go(self):
        print("Creating Palm Mech")
        header = "Palm Mech > "
        
        arma = self.arma
        active_arma = RBS.activate_arma(arma) 
        bpy.ops.object.mode_set(mode='EDIT')
        
        eb_palm_parent =  active_arma.edit_bones[self.id_palm_parent]
        
        eb_arr = []
        
        for i, f in enumerate(self.id_palms):
            print(f)
            eb = RBS.new_eb(self.arma, f)
            self.ebd_arr[i].apply(eb)
            RBS.set_bonelayer(eb, self.layer_bone_basic)
            eb.parent = eb_palm_parent
            eb_arr.append(eb) 
            
            
        
        eb_c_palm = RBS.copy_eb(arma, eb_arr[self.palm_finger_num-1], self.id_c_palm)
        RBS.set_bonelayer(eb_c_palm , self.layer_control_basic) 
        eb_c_palm.parent = eb_palm_parent
        self.rigshape_c_palm.apply_eb(eb_c_palm.parent)
        
        
            
    
        #POSE BONE PHASE
    
    
        bpy.ops.object.mode_set(mode='POSE')
        
        
        
        pb = arma.pose.bones.get(self.id_c_palm)
        self.rigshape_c_palm.apply_pb(pb)
        pb.bone_group = self.bonegroup_control
                
        id = self.id_palms[len(self.id_palms)-1]
        
        pb = arma.pose.bones.get(id)
        pb.lock_location = [True,True,True]
        pb.lock_rotation = [True,True,True]
        pb.lock_scale = [True,True,True]  
        c = pb.constraints.new('COPY_TRANSFORMS')
        c.name = "Copy Transforms"
        c.target = arma
        c.subtarget = self.id_c_palm 
        c.target_space = 'LOCAL'
        c.owner_space = 'LOCAL'        
        c = pb.constraints.new('COPY_SCALE')
        c.name = "Copy Scale"
        c.target = arma
        c.subtarget = self.id_palm_parent 
        
        
        id = self.id_palms[len(self.id_palms)-2]
        pb = arma.pose.bones.get(id)
        pb.lock_location = [True,True,True]
        pb.lock_rotation = [True,True,True]
        pb.lock_scale = [True,True,True]  
        c = pb.constraints.new('COPY_TRANSFORMS')
        c.name = "Copy Transforms"
        c.target = arma
        c.subtarget = self.id_c_palm 
        c.target_space = 'LOCAL'
        c.owner_space = 'LOCAL'
        c.influence = .667
        c = pb.constraints.new('COPY_SCALE')
        c.name = "Copy Scale"
        c.target = arma
        c.subtarget = self.id_palm_parent 
        c = pb.constraints.new('COPY_ROTATION')
        c.name = "Copy Rotation"
        c.target = arma
        c.subtarget = self.id_c_palm 
        c.euler_order = 'YXZ'
        c.use_y = False
        c.use_z = False
        c.mix_mode = 'ADD'
        c.target_space = 'LOCAL'
        c.owner_space = 'LOCAL'
        c.influence = .278
        
        id = self.id_palms[len(self.id_palms)-3]
        pb = arma.pose.bones.get(id)
        pb.lock_location = [True,True,True]
        pb.lock_rotation = [True,True,True]
        pb.lock_scale = [True,True,True]  
        c = pb.constraints.new('COPY_TRANSFORMS')
        c.name = "Copy Transforms"
        c.target = arma
        c.subtarget = self.id_c_palm 
        c.target_space = 'LOCAL'
        c.owner_space = 'LOCAL'
        c.influence = .333
        c = pb.constraints.new('COPY_SCALE')
        c.name = "Copy Scale"
        c.target = arma
        c.subtarget = self.id_palm_parent 
        c = pb.constraints.new('COPY_ROTATION')
        c.name = "Copy Rotation"
        c.target = arma
        c.subtarget = self.id_c_palm 
        c.euler_order = 'YXZ'
        c.use_y = False
        c.use_z = False
        c.mix_mode = 'ADD'
        c.target_space = 'LOCAL'
        c.owner_space = 'LOCAL'
        c.influence = .266
        
        c = pb.constraints.new('COPY_SCALE')
        c.name = "Copy Scale"
        c.target = arma
        c.subtarget = self.id_palm_parent 
        
        