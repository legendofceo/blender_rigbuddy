import bpy

RBS = bpy.data.texts["rigbuddy_statics.py"].as_module()


class rigbuddy_mech_arm:
        
    def __init__(self,arma,axis_index,axis):    
        self.arma = arma
        self.axis_index = axis_index
        self.axis = axis 
        
        self.n_clavicle = "clavicle"
        self.n_upperarm = "upperarm"
        self.n_lowerarm = "lowerarm"
        self.n_hand = "hand"
        self.abr_fk = "_fk"
        self.abr_ik = "_ik"
        self.abr_control = "c_"
        self.abr_mechanism = "m_"
        
        circle_solid_y = bpy.data.objects['controlshape_circle_solid_y']
        
        self.rigshape_c_clavicle = RBS.rigshape_data(circle_solid_y,4.0,True,True)
        self.rigshape_c_upperarm_fk = RBS.rigshape_data(circle_solid_y,2.0,True,True)
        self.rigshape_c_lowerarm_fk = RBS.rigshape_data(circle_solid_y,2.0,True,True)
        self.rigshape_c_hand_fk = RBS.rigshape_data(circle_solid_y,8.0,True,True)
        self.rigshape_c_hand_ik = RBS.rigshape_data(circle_solid_y,8.0,True,True)

        
        return    
        
    def init(self):
        self.id_clavicle = self.n_clavicle+self.axis
        self.id_upperarm = self.n_upperarm+self.axis
        self.id_lowerarm = self.n_lowerarm+self.axis
        self.id_hand = self.n_hand+self.axis    
        
        self.id_upperarm_ik = self.abr_mechanism+self.n_upperarm+self.abr_ik+self.axis
        self.id_lowerarm_ik = self.abr_mechanism+self.n_lowerarm+self.abr_ik+self.axis

        
        self.id_c_clavicle = self.abr_control+self.n_clavicle+self.axis
        self.id_c_upperarm_fk = self.abr_control+self.n_upperarm+self.abr_fk+self.axis
        self.id_c_lowerarm_fk = self.abr_control+self.n_lowerarm+self.abr_fk+self.axis
        self.id_c_hand_fk = self.abr_control+self.n_hand+self.abr_fk+self.axis
        
        self.id_c_hand_ik = self.abr_control+self.n_hand+self.abr_ik+self.axis
        
        
    def set_source(self,arma):         
        active_arma = RBS.activate_arma(arma) 
        bpy.ops.object.mode_set(mode='EDIT')
        
        self.ebd_clavicle = RBS.editbone_data(active_arma.edit_bones[self.id_clavicle])
        self.ebd_upperarm = RBS.editbone_data(active_arma.edit_bones[self.id_upperarm])
        self.ebd_lowerarm = RBS.editbone_data(active_arma.edit_bones[self.id_lowerarm])
        self.ebd_hand = RBS.editbone_data(active_arma.edit_bones[self.id_hand])
        return self
                 
    def set_layers(self,bone_basic,bone_mech,control_basic,control_ik,control_fk):
        self.layer_bone_basic = bone_basic
        self.layer_bone_mech = bone_mech
        self.layer_control_basic = control_basic
        self.layer_control_fk = control_fk
        self.layer_control_ik = control_ik
        return self
    
    def set_bonegroups(self,bonegroup_clavicle, bonegroup_fk, bonegroup_ik):
        self.bonegroup_clavicle = bonegroup_clavicle
        self.bonegroup_fk = bonegroup_fk
        self.bonegroup_ik = bonegroup_ik
        return self
                
    def set_arm_parent_id(self,id):
        self.id_arm_parent = id
        return
    
    def set_control_scale(self,clavicle_fk,upperarm_fk,lowerarm_fk,hand_fk,hand_ik,elbow_ik):
        return
        
    def go(self):
        print("Creating Arm Mech")
        header = "Arm Mech > "
        
        arma = self.arma
        active_arma = RBS.activate_arma(arma) 
        bpy.ops.object.mode_set(mode='EDIT')
        
        eb_arm_parent =  active_arma.edit_bones[self.id_arm_parent]
        
        eb_clavicle = RBS.new_eb(self.arma, self.id_clavicle)
        self.ebd_clavicle.apply(eb_clavicle)
        RBS.set_bonelayer(eb_clavicle, self.layer_bone_basic)
        eb_clavicle.parent = eb_arm_parent 
         
        eb_upperarm = RBS.new_eb(self.arma, self.id_upperarm)
        self.ebd_upperarm.apply(eb_upperarm)
        RBS.set_bonelayer(eb_upperarm, self.layer_bone_basic)
        eb_upperarm.use_connect = True
        eb_upperarm.parent = eb_clavicle
        
        eb_lowerarm = RBS.new_eb(self.arma, self.id_lowerarm)
        self.ebd_lowerarm.apply(eb_lowerarm)
        RBS.set_bonelayer(eb_lowerarm, self.layer_bone_basic)
        eb_lowerarm.use_connect = True
        eb_lowerarm.parent = eb_upperarm
        
        eb_hand = RBS.new_eb(self.arma, self.id_hand)
        self.ebd_hand.apply(eb_hand)
        RBS.set_bonelayer(eb_hand, self.layer_bone_basic)
        eb_hand.use_connect = True
        eb_hand.parent = eb_lowerarm
        
        
        
        #FK
        
                
        eb_c_clavicle = RBS.copy_eb(arma, eb_clavicle, self.id_c_clavicle)
        RBS.set_bonelayer(eb_c_clavicle, self.layer_control_basic) 
        self.rigshape_c_clavicle.apply_eb(eb_c_clavicle)
        eb_c_clavicle.parent = eb_arm_parent 
        
        eb_c_upperarm_fk = RBS.copy_eb(arma, eb_upperarm, self.id_c_upperarm_fk)
        RBS.set_bonelayer(eb_c_upperarm_fk, self.layer_control_fk) 
        self.rigshape_c_upperarm_fk.apply_eb(eb_c_upperarm_fk)
        eb_c_upperarm_fk.use_connect = True
        eb_c_upperarm_fk.parent = eb_clavicle 
        
        eb_c_lowerarm_fk = RBS.copy_eb(arma, eb_lowerarm, self.id_c_lowerarm_fk)
        RBS.set_bonelayer(eb_c_lowerarm_fk, self.layer_control_fk) 
        self.rigshape_c_lowerarm_fk.apply_eb(eb_c_lowerarm_fk)
        eb_c_lowerarm_fk.use_connect = True
        eb_c_lowerarm_fk.parent = eb_c_upperarm_fk 
        
        eb_c_hand_fk = RBS.copy_eb(arma, eb_hand, self.id_c_hand_fk)
        RBS.set_bonelayer(eb_c_hand_fk, self.layer_control_fk) 
        self.rigshape_c_hand_fk.apply_eb(eb_c_hand_fk)
        eb_c_hand_fk.use_connect = True
        eb_c_hand_fk.parent = eb_c_lowerarm_fk
        
        eb_upperarm_ik = RBS.copy_eb(arma, eb_upperarm, self.id_upperarm_ik)
        RBS.set_bonelayer(eb_upperarm_ik, self.layer_bone_mech) 
        eb_upperarm_ik.use_connect = True
        eb_upperarm_ik.parent = eb_c_clavicle
        
        
        eb_lowerarm_ik = RBS.copy_eb(arma, eb_lowerarm, self.id_lowerarm_ik)
        RBS.set_bonelayer(eb_lowerarm_ik, self.layer_bone_mech) 
        eb_lowerarm_ik.parent = eb_upperarm_ik 
        eb_lowerarm_ik.use_connect = True
        
        
        eb_c_hand_ik = RBS.copy_eb(arma, eb_hand, self.id_c_hand_ik)
        RBS.set_bonelayer(eb_c_hand_ik, self.layer_control_ik) 
        self.rigshape_c_hand_ik.apply_eb(eb_c_hand_ik)

    
    
    
        #POSE BONE PHASE
    
    
        bpy.ops.object.mode_set(mode='POSE')
        
        
        
        #BASE BONES
        
        pb = arma.pose.bones.get(self.id_clavicle)
        pb.lock_location = [True,True,True]
        pb.lock_rotation = [True,True,True]
        pb.lock_scale = [True,True,True]  
        c = pb.constraints.new('COPY_TRANSFORMS')
        c.name = "Copy Transforms FK"
        c.target = arma
        c.subtarget = self.id_c_clavicle 
        
        pb = arma.pose.bones.get(self.id_upperarm)
        pb.lock_location = [True,True,True]
        pb.lock_rotation = [True,True,True]
        pb.lock_scale = [True,True,True]  
        c = pb.constraints.new('COPY_TRANSFORMS')
        c.name = "Copy Transforms FK"
        c.target = arma
        c.subtarget = self.id_c_upperarm_fk 
        c = pb.constraints.new('COPY_TRANSFORMS')
        c.name = "Copy Transforms IK"
        c.target = arma
        c.subtarget = self.id_upperarm_ik 
        
        
        pb = arma.pose.bones.get(self.id_lowerarm)
        pb.lock_location = [True,True,True]
        pb.lock_rotation = [True,True,True]
        pb.lock_scale = [True,True,True]  
        c = pb.constraints.new('COPY_TRANSFORMS')
        c.name = "Copy Transforms FK"
        c.target = arma
        c.subtarget = self.id_c_lowerarm_fk 
        c = pb.constraints.new('COPY_TRANSFORMS')
        c.name = "Copy Transforms IK"
        c.target = arma
        c.subtarget = self.id_lowerarm_ik 
        
        pb = arma.pose.bones.get(self.id_hand)
        pb.lock_location = [True,True,True]
        pb.lock_rotation = [True,True,True]
        pb.lock_scale = [True,True,True]  
        c = pb.constraints.new('COPY_TRANSFORMS')
        c.name = "Copy Transforms FK"
        c.target = arma
        c.subtarget = self.id_c_hand_fk 
        c = pb.constraints.new('COPY_TRANSFORMS')
        c.name = "Copy Transforms IK"
        c.target = arma
        c.subtarget = self.id_c_hand_ik 
        
        #FK
        pb = arma.pose.bones.get(self.id_c_clavicle) 
        pb.bone_group = self.bonegroup_clavicle
        self.rigshape_c_clavicle.apply_pb(pb)
        
        pb = arma.pose.bones.get(self.id_c_upperarm_fk) 
        pb.bone_group = self.bonegroup_fk 
        self.rigshape_c_upperarm_fk.apply_pb(pb)
        
        pb = arma.pose.bones.get(self.id_c_lowerarm_fk) 
        pb.bone_group = self.bonegroup_fk 
        self.rigshape_c_lowerarm_fk.apply_pb(pb)
        
        pb = arma.pose.bones.get(self.id_c_hand_fk)
        pb.bone_group = self.bonegroup_fk 
        self.rigshape_c_hand_fk.apply_pb(pb)
        
        
        #IK 
        print(header+"IK Constraints")
        pb = arma.pose.bones.get(self.id_upperarm_ik)
        pb.ik_stretch = .1
        pb.rotation_mode = 'ZXY'
        pb.lock_rotation = [True,False,True] 
        
        pb = arma.pose.bones.get(self.id_lowerarm_ik)       
        pb.ik_stretch = .1
        pb.lock_ik_y = True
        pb.lock_ik_z = True
        pb.lock_location = [True,True,True]
        pb.lock_rotations_4d = True
        pb.lock_scale = [True,True,True]
        c = pb.constraints.new('IK')
        c.name = "IK Rotate"
        c.target = arma
        c.subtarget = self.id_c_hand_ik
        c.chain_count = 2
        
        c = pb.constraints.new('IK')
        c.name = "IK Pole"
        c.target = arma
        c.subtarget = self.id_c_hand_ik
        #DRIVER
        c.mute = True
        c.chain_count = 2
        c.pole_angle = -90
        c.pole_target = arma
        #c.pole_subtarget = None
        
        pb = arma.pose.bones.get(self.id_c_hand_ik) 
        pb.bone_group = self.bonegroup_ik
        self.rigshape_c_hand_ik.apply_pb(pb)
        
        return