import bpy

RBS = bpy.data.texts["rigbuddy_statics.py"].as_module()


class rigbuddy_mech_hand:
        
    def __init__(self,arma,axis_index,axis,finger_num=5,joint_num=3):    
        self.arma = arma
        self.axis_index = axis_index
        self.axis = axis 
        
        self.finger_num = finger_num
        self.joint_num = joint_num
        
        self.n_finger = "finger"
        self.n_fingers = ["thumb","index","middle","ring","pinky"]
        
        
        self.abr_control = "c_"
        self.abr_tweak = "t_"
        self.abr_mechanism = "m_"
        
        self.rigshape_c_finger = RBS.rigshape_data(bpy.data.objects['rigshape_finger'],6.0,True,True)
        self.rigshape_t_finger = RBS.rigshape_data(bpy.data.objects['rigshape_tweak_small'],7.0,True,True)
        
        #self.rigshape_c_clavicle = RBS.rigshape_data(circle_solid_y,4.0,True,True)        
        return    
        
    def init(self):        
        self.id_fingers  = []        
        for f in range(self.finger_num):
            self.id_fingers.append([])
            
            for j in range(self.joint_num):
                self.id_fingers[f].append(self.n_finger+"_"+self.n_fingers[f]+str(j+1)+self.axis)
        return self
        
    def set_source(self,arma):         
        active_arma = RBS.activate_arma(arma) 
        bpy.ops.object.mode_set(mode='EDIT')        
        self.ebd_arr= []
        for f in range(self.finger_num):
            self.ebd_arr.append([])
            for j in range(self.joint_num):
                 self.ebd_arr[f].append(RBS.editbone_data(active_arma.edit_bones[self.n_finger+"_"+self.n_fingers[f]+str(j+1)+self.axis]))
        return self
                 
    def set_layers(self,bone_basic,control_basic):
        self.layer_bone_basic = bone_basic
        self.layer_control_basic = control_basic
        return self
    
    def set_bonegroups(self,bonegroup_control):
        self.bonegroup_control = bonegroup_control
        return self
                
    def set_finger_parent_ids(self,parent_ids):
        self.id_parents = parent_ids
        return
    
    def set_control_scale(self,control_scale):
        self.control_scale = control_scale    
        return
        
    def go(self):
        print("Creating Hand Mech")
        header = "Hand Mech > "
        
        arma = self.arma
        active_arma = RBS.activate_arma(arma) 
        bpy.ops.object.mode_set(mode='EDIT')
        
            
        eb_finger_parents_arr = []
        for f in range(self.finger_num):
            eb_finger_parents_arr .append(active_arma.edit_bones[self.id_parents[f]])
        
        eb_arr = []
        eb_c_arr = []
        eb_t_arr = []
        
        for f in range(self.finger_num):
            eb_arr.append([])
            eb_c_arr.append([])
            eb_t_arr.append([])
            
            for j in range(self.joint_num):
                eb = RBS.new_eb(self.arma, self.id_fingers[f][j])
                self.ebd_arr[f][j].apply(eb)
                RBS.set_bonelayer(eb, self.layer_bone_basic)

            
                ebc = RBS.copy_eb(arma, eb, self.abr_control+self.id_fingers[f][j])
                RBS.set_bonelayer(ebc, self.layer_control_basic) 
                          
        
                ebt = RBS.copy_eb(arma, eb, self.abr_tweak+self.id_fingers[f][j])
                RBS.set_bonelayer(ebt, self.layer_control_basic) 
                
                eb_c_arr[f].append(ebc)
                eb_t_arr[f].append(ebt) 
                eb_arr[f].append(eb)
                
                if(j==0):
                    eb.parent = eb_finger_parents_arr [f]
                    ebt.parent = ebc
                    ebc.parent = eb.parent
                else:
                    eb.parent = eb_arr[f][j-1]
                    ebt.parent = ebc
                    ebc.parent = eb.parent
                    
                 
                                
                
        bpy.ops.object.mode_set(mode='POSE')
    
        #POSE BONE PHASE
    
    
        for f in range(self.finger_num):            
            for j in range(self.joint_num):
                                
                id = self.id_fingers[f][j]
                id_t = self.abr_tweak+self.id_fingers[f][j]
                id_c = self.abr_control+self.id_fingers[f][j]
                pb = arma.pose.bones.get(id)
                pb_t = arma.pose.bones.get(id_t)
                pb_c = arma.pose.bones.get(id_c)
                pb.lock_location = [True,True,True]
                pb.lock_rotation = [True,True,True]
                pb.lock_scale = [True,True,True]  
                c = pb.constraints.new('COPY_TRANSFORMS')
                c.name = "Copy Transforms"
                c.target = arma
                c.subtarget = id_t   
                
                self.rigshape_c_finger.apply_pb(pb_c)
                pb_c.bone_group = self.bonegroup_control
                
                
                self.rigshape_t_finger.apply_pb(pb_t)
                pb_t.bone_group = self.bonegroup_control
                                
        return     