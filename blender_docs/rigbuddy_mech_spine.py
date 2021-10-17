import bpy

RBS = bpy.data.texts["rigbuddy_statics.py"].as_module()

    
class instance:

    arma = None
    
    bonelayer_bone_basic = None
    bonelayer_control_basic = None

    bonegroup_control_basic_world1 = None
    bonegroup_control_basic_world2 = None
    bonegroup_control_basic_local1 = None
    bonegroup_control_basic_local2 = None
    
    rig_root = None
        
    ebd_hip = None
    ebd_pelvis = None
    ebd_spine1 = None
    ebd_spine2 = None
    ebd_spine3 = None
    ebd_spine4 = None
    
    controlshape_c_hip = None
    controlshape_c_pelvis = None
    controlshape_c_spine1 = None
    controlshape_c_spine2 = None
    controlshape_c_spine3 = None
    controlshape_c_spine4 = None
        
    controlshape_t_pelvis = None
    controlshape_t_spine1 = None
    controlshape_t_spine2 = None
    controlshape_t_spine3 = None
    controlshape_t_spine4 = None
        
    o_hip = None
    o_pelvis = None
    o_spine1 = None
    o_spine2 = None
    o_spine3 = None
    o_spine4 = None 
    t_pelvis = None
    t_spine1 = None
    t_spine2 = None
    t_spine3 = None
    t_spine4 = None
    c_hip = None
    c_pelvis = None
    c_spine1 = None
    c_spine2 = None
    c_spine3 = None
    c_spine4 = None 
        
                       
    def go(self):
        print("Creating Spine Mech")
        header = "Spine Mech > "
        
        bpy.ops.object.mode_set(mode='EDIT')
            
        arma = self.arma
        active_arma = RBS.activate_arma(arma)  
                    
        eb_root =  active_arma.edit_bones[self.rig_root]     

        eb_o_hip = RBS.new_eb(arma, self.o_hip)
        self.ebd_hip.apply(eb_o_hip)
        RBS.set_bonelayer(eb_o_hip, self.bonelayer_bone_basic)
        eb_o_hip.parent = eb_root
        
        eb_o_pelvis = RBS.new_eb(arma, self.o_pelvis)
        self.ebd_pelvis.apply(eb_o_pelvis)
        RBS.set_bonelayer(eb_o_pelvis, self.bonelayer_bone_basic)
        eb_o_pelvis.parent = eb_o_hip 
          
        eb_o_spine1 = RBS.new_eb(arma, self.o_spine1)
        self.ebd_spine1.apply(eb_o_spine1)
        RBS.set_bonelayer(eb_o_spine1, self.bonelayer_bone_basic)
        eb_o_spine1.parent = eb_o_pelvis
        
        eb_o_spine2 = RBS.new_eb(arma, self.o_spine2)
        self.ebd_spine2.apply(eb_o_spine2)
        RBS.set_bonelayer(eb_o_spine2, self.bonelayer_bone_basic)
        eb_o_spine2.parent = eb_o_spine1
        
        eb_o_spine3 = RBS.new_eb(arma, self.o_spine3)
        self.ebd_spine3.apply(eb_o_spine3)
        RBS.set_bonelayer(eb_o_spine3, self.bonelayer_bone_basic)
        eb_o_spine3.parent = eb_o_spine2
        
        eb_o_spine4 = RBS.new_eb(arma, self.o_spine4)
        self.ebd_spine4.apply(eb_o_spine4)
        RBS.set_bonelayer(eb_o_spine4, self.bonelayer_bone_basic)
        eb_o_spine4.parent = eb_o_spine3
        
        eb_c_hip = RBS.copy_eb(arma, eb_o_hip, self.c_hip)
        RBS.set_bonelayer(eb_c_hip, self.bonelayer_control_basic) 
        self.controlshape_c_hip.apply_eb(eb_c_hip)
        
        eb_c_pelvis = RBS.copy_eb(arma, eb_o_pelvis, self.c_pelvis)
        RBS.set_bonelayer(eb_c_pelvis, self.bonelayer_control_basic) 
        self.controlshape_c_pelvis.apply_eb(eb_c_pelvis)
        eb_c_pelvis.parent = eb_c_hip
        
        eb_c_spine1 = RBS.copy_eb(arma, eb_o_spine1, self.c_spine1)
        RBS.set_bonelayer(eb_c_spine1, self.bonelayer_control_basic) 
        self.controlshape_c_spine1.apply_eb(eb_c_spine1)
        eb_c_spine1.parent = eb_c_hip
        
        eb_t_spine1 = RBS.copy_eb(arma, eb_o_spine1, self.t_spine1)
        RBS.set_bonelayer(eb_t_spine1, self.bonelayer_control_basic) 
        eb_t_spine1.parent = eb_c_spine1
        
        eb_c_spine2 = RBS.copy_eb(arma, eb_o_spine2, self.c_spine2)
        RBS.set_bonelayer(eb_c_spine2, self.bonelayer_control_basic) 
        self.controlshape_c_spine2.apply_eb(eb_c_spine2)
        eb_c_spine2.parent = eb_t_spine1
              
        eb_t_spine2 = RBS.copy_eb(arma, eb_o_spine2, self.t_spine2)
        RBS.set_bonelayer(eb_t_spine2, self.bonelayer_control_basic) 
        eb_t_spine2.parent = eb_c_spine2
                
        eb_c_spine3 = RBS.copy_eb(arma, eb_o_spine3, self.c_spine3)
        RBS.set_bonelayer(eb_c_spine3, self.bonelayer_control_basic) 
        self.controlshape_c_spine3.apply_eb(eb_c_spine3)
        eb_c_spine3.parent = eb_t_spine2
        
        eb_c_spine4 = RBS.copy_eb(arma, eb_o_spine4, self.c_spine4)
        RBS.set_bonelayer(eb_c_spine4, self.bonelayer_control_basic) 
        self.controlshape_c_spine4.apply_eb(eb_c_spine4)
        
        eb_t_pelvis = RBS.copy_eb(arma, eb_o_pelvis, self.t_pelvis)
        RBS.set_bonelayer(eb_t_pelvis, self.bonelayer_control_basic) 
        

        
        eb_t_spine3 = RBS.copy_eb(arma, eb_o_spine3, self.t_spine3)
        RBS.set_bonelayer(eb_t_spine3, self.bonelayer_control_basic) 
        
        eb_t_spine4 = RBS.copy_eb(arma, eb_o_spine4, self.t_spine4)
        RBS.set_bonelayer(eb_t_spine4, self.bonelayer_control_basic)
        
        
        #POSE BONE PHASE
        
        bpy.ops.object.mode_set(mode='POSE')
        
        pb = arma.pose.bones.get(self.o_hip)
        pb.lock_location = [True,True,True]
        pb.lock_rotation = [True,True,True]
        pb.lock_scale = [True,True,True]  
        c = pb.constraints.new('COPY_TRANSFORMS')
        c.name = "Copy Transforms"
        c.target = arma
        c.subtarget = self.c_hip
        
        pb = arma.pose.bones.get(self.c_hip)
        self.controlshape_c_hip.apply_pb(pb)
        pb.bone_group = self.bonegroup_control_basic_world1
        
        pb = arma.pose.bones.get(self.c_pelvis)
        self.controlshape_c_pelvis.apply_pb(pb)
        pb.bone_group = self.bonegroup_control_basic_local2
        
        pb = arma.pose.bones.get(self.c_spine1)
        self.controlshape_c_spine1.apply_pb(pb)
        pb.bone_group = self.bonegroup_control_basic_local1
        
        pb = arma.pose.bones.get(self.c_spine2)
        self.controlshape_c_spine2.apply_pb(pb)
        pb.bone_group = self.bonegroup_control_basic_local1
        
        
        pb = arma.pose.bones.get(self.c_spine3)
        self.controlshape_c_spine3.apply_pb(pb)
        pb.bone_group = self.bonegroup_control_basic_local1
        
        pb = arma.pose.bones.get(self.c_spine4)
        self.controlshape_c_spine4.apply_pb(pb)
        pb.bone_group = self.bonegroup_control_basic_local1
        
            
        
        pb = arma.pose.bones.get(self.t_pelvis)
        self.controlshape_t_pelvis.apply_pb(pb)
        
        pb = arma.pose.bones.get(self.t_spine1)
        self.controlshape_t_spine1.apply_pb(pb)
        
        pb = arma.pose.bones.get(self.t_spine2)
        self.controlshape_t_spine2.apply_pb(pb)
        
        pb = arma.pose.bones.get(self.t_spine3)
        self.controlshape_t_spine3.apply_pb(pb)
        
        pb = arma.pose.bones.get(self.t_spine4)
        self.controlshape_t_spine4.apply_pb(pb)
        
        return