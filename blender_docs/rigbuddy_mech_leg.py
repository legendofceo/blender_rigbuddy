import bpy

RBS = bpy.data.texts["rigbuddy_statics.py"].as_module()


    
class rigbuddy_mech_leg():

   def __init__(self,arma,axis_index,axis):   
        self.arma = arma
        self.axis_index = axis_index
        self.axis = axis 
        
        self.n_thigh = "thigh"
        self.n_shin = "shin"
        self.n_foot = "foot"
        self.n_toe = "toe"
        self.n_heel = "heel"
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
        self.id_thigh = self.n_thigh+self.axis
        self.id_shin = self.n_shin+self.axis
        self.id_foot = self.n_foot+self.axis
        self.id_toe = self.n_toe+self.axis    
        
        self.id_c_thigh_fk = self.abr_control+self.n_thigh+self.abr_fk+self.axis
        self.id_c_shin_fk = self.abr_control+self.n_shin+self.abr_fk+self.axis
        self.id_c_foot_fk = self.abr_control+self.n_foot+self.abr_fk+self.axis


        
        self.id_c_clavicle = self.abr_control+self.n_clavicle+self.axis
        self.id_c_upperarm_fk = self.abr_control+self.n_upperarm+self.abr_fk+self.axis
        self.id_c_lowerarm_fk = self.abr_control+self.n_lowerarm+self.abr_fk+self.axis
        self.id_c_hand_fk = self.abr_control+self.n_hand+self.abr_fk+self.axis
        
        self.id_c_hand_ik = self.abr_control+self.n_hand+self.abr_ik+self.axis
                           
    def go(self):
        print("Creating Leg Mech")
        header = "Leg Mech > "
        
        bpy.ops.object.mode_set(mode='EDIT')
            
        arma = self.arma
        active_arma = RBS.activate_arma(arma)  
                    
        eb_rig_root =  active_arma.edit_bones[self.rig_root]
        eb_leg_parent = active_arma.edit_bones[self.leg_parent]
        
        ebd_thigh = self.ebd_thigh
        ebd_shin = self.ebd_shin
        ebd_foot = self.ebd_foot
        ebd_toe = self.ebd_toe
        
        #eb_d_thigh = RBS.new_eb(arma,self.d_thigh)
        #RBS.apply_eb_data(ebd_thigh,eb_d_thigh)
        #eb_d_thigh.parent = eb_leg_parent
        #eb_d_shin = RBS.new_eb(arma,self.d_shin)
        #RBS.apply_eb_data(ebd_shin,eb_d_shin)
        #eb_d_foot = RBS.new_eb(arma, self.d_foot)
        #RBS.apply_eb_data(ebd_foot,eb_d_foot)
        #eb_d_toe = RBS.new_eb(arma,self.d_toe)
        #RBS.apply_eb_data(ebd_toe,eb_d_toe)
         

        eb_o_thigh = RBS.new_eb(arma, self.o_thigh)
        RBS.apply_eb_data(ebd_thigh,eb_o_thigh)
        RBS.set_bonelayer(eb_o_thigh, self.bonelayer_bone_basic)
        eb_o_thigh.parent = eb_leg_parent 
          
        eb_o_shin = RBS.new_eb(arma, self.o_shin)
        RBS.apply_eb_data(ebd_shin,eb_o_shin)
        RBS.set_bonelayer(eb_o_shin, self.bonelayer_bone_basic)
        eb_o_shin.parent = eb_o_thigh 
        eb_o_shin.use_connect = True
          
        eb_o_foot = RBS.new_eb(arma, self.o_foot)
        RBS.apply_eb_data(ebd_foot,eb_o_foot)
        RBS.set_bonelayer(eb_o_foot, self.bonelayer_bone_basic)
        eb_o_foot.parent = eb_o_shin
        eb_o_foot.use_connect = True
        
        eb_o_toe = RBS.new_eb(arma, self.o_toe)
        RBS.set_bonelayer(eb_o_toe, self.bonelayer_bone_basic)
        RBS.apply_eb_data(ebd_toe,eb_o_toe)
        eb_o_toe.parent = eb_o_foot
        
        
        eb_m_thigh_tweak = RBS.copy_eb(arma, eb_o_thigh, self.m_thigh_tweak)
        RBS.set_bonelayer(eb_m_thigh_tweak, self.bonelayer_mech)  
        eb_m_thigh_tweak.parent = eb_leg_parent
        eb_m_thigh_tweak.inherit_scale = "FIX_SHEAR"
        
        eb_thigh_tweak = RBS.copy_eb(arma, eb_o_thigh, self.thigh_tweak) 
        RBS.set_bonelayer(eb_thigh_tweak, self.bonelayer_tweak) 
        eb_thigh_tweak.parent = eb_m_thigh_tweak 
        
        #Make Parent and Parent Mechanism      
        eb_m_thigh_parent = RBS.copy_eb(arma,eb_o_thigh, self.m_thigh_parent)    
        RBS.set_bonelayer(eb_m_thigh_parent, self.bonelayer_mech) 
        eb_m_thigh_parent.parent = eb_leg_parent
        vec_head = eb_m_thigh_parent.head.copy()
        vec_head.y+=.1
        eb_m_thigh_parent.tail = vec_head
        eb_m_thigh_parent.inherit_scale = "FIX_SHEAR"
        eb_m_thigh_parent.roll = 0
        
        eb_m_thigh_parent_socket = RBS.copy_eb(arma, eb_o_thigh, self.m_thigh_parent_socket)
        RBS.set_bonelayer(eb_m_thigh_parent_socket, self.bonelayer_mech) 
        eb_m_thigh_parent_socket.parent = eb_m_thigh_parent
        eb_m_thigh_parent_socket.length = .05
        
        eb_thigh_parent = RBS.copy_eb(arma, eb_o_thigh, self.thigh_parent)
        RBS.set_bonelayer(eb_thigh_parent, self.bonelayer_mech)
        eb_thigh_parent.parent = eb_m_thigh_parent_socket
        eb_thigh_parent.length = .1

        eb_m_thigh_twist1_tweak = RBS.copy_eb(arma, eb_o_thigh, self.m_thigh_twist1_tweak) 
        RBS.set_bonelayer(eb_m_thigh_twist1_tweak, self.bonelayer_mech)
        eb_m_thigh_twist1_tweak.parent = eb_o_thigh
        eb_m_thigh_twist1_tweak.length = (eb_m_thigh_twist1_tweak.length/2)
        tail_vec = eb_m_thigh_twist1_tweak.tail.copy()
        eb_m_thigh_twist1_tweak.length = (eb_m_thigh_twist1_tweak.length+.05)
        eb_m_thigh_twist1_tweak.head = tail_vec
        
        eb_thigh_twist1_tweak = RBS.copy_eb(arma, eb_m_thigh_twist1_tweak, self.thigh_twist1_tweak)
        RBS.set_bonelayer(eb_thigh_twist1_tweak, self.bonelayer_tweak)
        eb_thigh_twist1_tweak.parent = eb_m_thigh_twist1_tweak    
        
        #Make FK
        eb_thigh_fk = RBS.copy_eb(arma,eb_o_thigh,self.thigh_fk)    
        RBS.set_bonelayer(eb_thigh_fk, self.bonelayer_control_legfk)
        eb_thigh_fk.parent = eb_m_thigh_parent
        self.controlshape_thigh_fk.apply_eb(eb_thigh_fk)
        
        eb_shin_fk = RBS.copy_eb(arma,eb_o_shin,self.shin_fk)    
        RBS.set_bonelayer(eb_shin_fk, self.bonelayer_control_legfk)
        eb_shin_fk.parent = eb_thigh_fk
        eb_shin_fk.use_connect = True
        self.controlshape_shin_fk.apply_eb(eb_shin_fk)
        
        eb_m_foot_fk = RBS.copy_eb(arma,eb_o_foot,self.m_foot_fk)  
        eb_m_foot_fk.parent = eb_shin_fk
        eb_m_foot_fk.use_connect = True
        eb_m_foot_fk.inherit_scale = "NONE"
        
        
        eb_foot_fk = RBS.copy_eb(arma,eb_o_foot,self.foot_fk)    
        RBS.set_bonelayer(eb_foot_fk, self.bonelayer_control_legfk)  
        eb_foot_fk.parent = eb_m_foot_fk
        self.controlshape_foot_fk.apply_eb(eb_foot_fk)
       
       
       
       
       
        #Make IK
        eb_thigh_ik = RBS.copy_eb(arma,eb_o_thigh,self.thigh_ik)  
        RBS.set_bonelayer(eb_thigh_ik, self.bonelayer_mech)  
        eb_thigh_ik.parent = eb_m_thigh_parent
        
        eb_shin_ik = RBS.copy_eb(arma,eb_o_shin,self.shin_ik)
        RBS.set_bonelayer(eb_shin_ik, self.bonelayer_mech) 
        eb_shin_ik.parent = eb_thigh_ik
        
        eb_thigh_stretch_ik = RBS.copy_eb(arma,eb_o_thigh,self.thigh_stretch_ik)
        RBS.set_bonelayer(eb_thigh_stretch_ik, self.bonelayer_mech)
        eb_thigh_stretch_ik.parent = eb_m_thigh_parent
        eb_thigh_stretch_ik.tail = eb_o_foot.head.copy()
         
        
        eb_foot_parent_ik = RBS.copy_eb(arma,eb_o_foot,self.foot_parent_ik)
        RBS.set_bonelayer(eb_foot_parent_ik, self.bonelayer_mech)
        RBS.eb_anti(eb_foot_parent_ik)
        RBS.eb_flatten_z(eb_foot_parent_ik)
        eb_foot_parent_ik.roll = 0
        eb_foot_parent_ik.length = 0.04
        
        
        eb_c_foot_ik = RBS.copy_eb(arma,eb_foot_parent_ik,self.c_foot_ik)
        RBS.set_bonelayer(eb_c_foot_ik, self.bonelayer_control_legik)
        eb_c_foot_ik.parent = eb_foot_parent_ik
        eb_c_foot_ik.length = .1
        eb_c_foot_ik.inherit_scale = "AVERAGE"
        self.controlshape_foot_ik.apply_eb(eb_c_foot_ik)
        
        eb_m_t_foot = RBS.copy_eb(arma,eb_o_foot,self.t_foot)
        RBS.set_bonelayer(eb_m_t_foot, self.bonelayer_mech)
        eb_m_t_foot .length = 0.03
        eb_m_t_foot.parent = eb_o_foot
        
        eb_t_foot = RBS.copy_eb(arma,eb_o_foot,self.t_foot)
        RBS.set_bonelayer(eb_t_foot, self.bonelayer_tweak)
        eb_t_foot .length = 0.05
        eb_t_foot.parent = eb_m_t_foot
        
        
        eb_m_toe = RBS.copy_eb(arma,eb_o_toe,self.m_toe)
        RBS.eb_anti(eb_m_toe)
        RBS.set_bonelayer(eb_m_toe, self.bonelayer_mech)
        eb_m_toe.use_connect = True
        eb_m_toe.length = 0.04
        eb_m_toe.parent = eb_o_foot
        
        
        eb_foot_spin = RBS.copy_eb(arma,eb_m_toe,self.foot_spin)
        RBS.set_bonelayer(eb_foot_spin, self.bonelayer_mech)
        eb_foot_spin.length = 0.1
        eb_foot_spin.parent = eb_c_foot_ik
        
        
        

                  
        eb_m_heel_rock2 = RBS.copy_eb(arma,eb_m_toe,self.m_heel_rock2)
        RBS.set_bonelayer(eb_m_heel_rock2, self.bonelayer_mech)
        eb_m_heel_rock2.length = 0.05
        eb_m_heel_rock2 = eb_foot_spin
    
        eb_m_heel_rock1 = RBS.copy_eb(arma,eb_m_toe,self.m_heel_rock1)
        RBS.set_bonelayer(eb_m_heel_rock1, self.bonelayer_mech)
        eb_m_heel_rock1.length = 0.05
        eb_m_heel_rock1 = eb_m_heel_rock2
        
        eb_m_heel_roll2 = RBS.copy_eb(arma,eb_m_toe,self.m_heel_roll2)
        RBS.set_bonelayer(eb_m_heel_roll2, self.bonelayer_mech)
        eb_m_heel_roll2.length = 0.05
        eb_m_heel_roll2 = eb_m_heel_rock1
        
        eb_m_heel_roll1 = RBS.copy_eb(arma,eb_m_toe,self.m_heel_roll1)
        RBS.set_bonelayer(eb_m_heel_roll1, self.bonelayer_mech)
        eb_m_heel_roll1.length = 0.05
        eb_m_heel_roll1 = eb_m_heel_roll2
                                        
        eb_c_toe = RBS.copy_eb(arma,eb_o_toe,self.c_toe)
        RBS.set_bonelayer(eb_c_toe, self.bonelayer_control_legik)
        eb_c_toe.parent = eb_m_toe
 
        m_foot_roll = RBS.copy_eb(arma,eb_o_foot,self.m_foot_roll)
        RBS.set_bonelayer(m_foot_roll, self.bonelayer_mech)
        m_foot_roll.length = 0.07
        m_foot_roll.parent = eb_m_heel_roll1
           
        eb_foot_ik = RBS.copy_eb(arma,eb_o_foot,self.foot_ik)
        RBS.set_bonelayer(eb_foot_ik, self.bonelayer_mech)
        eb_foot_ik.parent = m_foot_roll
         
           
                   
        eb_c_heel_ik = RBS.copy_eb(arma,eb_foot_parent_ik,self.c_heel_ik)
        RBS.set_bonelayer(eb_c_heel_ik, self.bonelayer_control_legik)
        eb_c_heel_ik.inherit_scale = "AVERAGE"
        eb_c_heel_ik.length = 0.07
        eb_c_heel_ik.parent = eb_foot_spin
        
        
        
        
        
        
        
        
        
        
        
        #BEGIN POSEMODE
        
        
        
        
        
        bpy.ops.object.mode_set(mode='POSE')
        
        ##ORIGINAL THIGH CONSTRAINTS
        print(header+"Creating Original Thigh Constraints")
        
        pb_o_thigh = arma.pose.bones.get(self.o_thigh)
        con = pb_o_thigh.constraints.new('COPY_TRANSFORMS')
        con.name = "Copy Transforms FK"
        con.target = arma
        con.subtarget = self.thigh_fk 
        
        con = pb_o_thigh.constraints.new('COPY_TRANSFORMS')
        con.name = "Copy Transforms IK"
        con.target = arma
        con.subtarget = self.thigh_ik 
        
        #ORIGINAL SHIN CONSTRAINTS
        print(header+"Creating Original Shin Constraints")
        pb = arma.pose.bones.get(self.o_shin)
        con = pb.constraints.new('COPY_TRANSFORMS')
        con.name = "Copy Transforms FK"
        con.target = arma
        con.subtarget = self.shin_fk 
        
        con = pb.constraints.new('COPY_TRANSFORMS')
        con.name = "Copy Transforms IK"
        con.target = arma
        con.subtarget = self.shin_ik 
        
        
        #ORIGINAL FOOT CONSTRAINTS
        print(header+"Creating Original Foot Constraints")
        pb = arma.pose.bones.get(self.o_foot)
        con = pb.constraints.new('COPY_TRANSFORMS')
        con.name = "Copy Transforms FK"
        con.target = arma
        con.subtarget = self.foot_fk 
        
        con = pb.constraints.new('COPY_TRANSFORMS')
        con.name = "Copy Transforms IK"
        con.target = arma
        con.subtarget = self.foot_ik 
        
        
        #FK LEG
        print(header+"FK Leg")
        pb = arma.pose.bones.get(self.thigh_fk)
        pb.bone_group = self.bonegroup_control_basic_local1
        self.controlshape_thigh_fk.apply_pb(pb)
        
        pb = arma.pose.bones.get(self.shin_fk)
        pb.bone_group = self.bonegroup_control_basic_local1
        self.controlshape_shin_fk.apply_pb(pb)
        
        pb = arma.pose.bones.get(self.foot_fk)
        pb.bone_group = self.bonegroup_control_basic_local1
        self.controlshape_foot_fk.apply_pb(pb)
        
        #IK LEG
        print(header+"Creating LegIK Constraints")
        pb = arma.pose.bones.get(self.thigh_ik)
        pb.ik_stretch = .1
        pb.rotation_mode = 'ZXY'
        pb.lock_rotation = [True,False,True]  
         
        pb = arma.pose.bones.get(self.shin_ik)
        
        pb.ik_stretch = .1
        pb.lock_ik_y = True
        pb.lock_ik_z = True
        pb.lock_location = [True,True,True]
        pb.lock_rotations_4d = True
        pb.lock_scale = [True,True,True]
        con = pb.constraints.new('IK')
        con.name = "IK Rotate"
        con.target = arma
        con.subtarget = self.foot_ik
        con.chain_count = 2
        
        con = pb.constraints.new('IK')
        con.name = "IK Pole"
        con.target = arma
        con.subtarget = self.foot_ik
        #DRIVER
        con.mute = True
        con.chain_count = 2
        con.pole_angle = -90
        con.pole_target = arma
        #con.pole_subtarget = None
        
        
        pb_m_thigh_parent = arma.pose.bones.get(self.m_thigh_parent)
        con = pb_m_thigh_parent.constraints.new('COPY_SCALE')
        con.name = "Copy Scale"
        con.target = arma
        con.subtarget = self.rig_root
        con.use_make_uniform = True
        
        pb_m_thigh_parent_socket = arma.pose.bones.get(self.m_thigh_parent_socket)
        con = pb_m_thigh_parent_socket .constraints.new('COPY_ROTATION')
        con.name = "Copy Rotation"
        con.target = arma
        con.subtarget = self.o_thigh 

        pb_m_thigh_parent_socket = arma.pose.bones.get(self.m_thigh_parent_socket)
        con = pb_m_thigh_parent_socket .constraints.new('COPY_ROTATION')
        con.name = "Copy Rotation"
        con.target = arma
        con.subtarget = self.o_thigh 
        
        
        pb = arma.pose.bones.get(self.o_toe)
        pb.lock_location = [True,True,True]
        pb.lock_rotation = [True,True,True]
        pb.lock_scale = [True,True,True]  
        c = pb.constraints.new('COPY_ROTATION')
        c.name = "Copy Rotation"
        c.target = arma
        c.subtarget = self.c_toe 
        
        pb = arma.pose.bones.get(self.m_heel_roll1)
        pb.rotation_mode = 'ZXY'
        pb.lock_location = [True,True,True]
        pb.lock_rotation = [True,True,True]
        pb.lock_scale = [True,True,True]        
        c = pb.constraints.new('COPY_ROTATION')
        c.name = "Copy Rotation"
        c.target = arma
        c.subtarget = self.c_heel_ik 
        c.target_space = 'POSE'
        c.owner_space = 'POSE'
        
        #INCOMPLETE
        pb = arma.pose.bones.get(self.m_toe)
        pb.lock_location = [True,True,True]
        pb.lock_rotations_4d = True
        pb.lock_scale = [True,True,True]
        c = pb.constraints.new('COPY_TRANSFORMS')
        c.name = "Copy Transforms"
        #c.target = arma
        #c.subtarget = self.c_heel_ik 
        #DRIVER
        
        #INCOMPLETE
        pb = arma.pose.bones.get(self.c_foot_ik)
        pb.bone_group = self.bonegroup_control_basic_world1
        self.controlshape_foot_ik.apply_pb(pb)
        
        return