import bpy
RBS = bpy.data.texts["rigbuddy_statics.py"].as_module()
Rigbuddy_Arma = bpy.data.texts["rigbuddy_arma.py"].as_module()
RB_Bone = bpy.data.texts["rigbuddy_bone.py"].as_module()
Rigbuddy_Mech_Leg = bpy.data.texts["rigbuddy_mech_leg.py"].as_module()
Rigbuddy_Mech_Spine = bpy.data.texts["rigbuddy_mech_spine.py"].as_module()
Rigbuddy_Mech_Arm = bpy.data.texts["rigbuddy_mech_arm.py"].as_module()
Rigbuddy_Mech_Palm = bpy.data.texts["rigbuddy_mech_palm.py"].as_module()
Rigbuddy_Mech_Hand = bpy.data.texts["rigbuddy_mech_hand.py"].as_module()
Rigbuddy_Controlshape = bpy.data.texts["rigbuddy_controlshape.py"].as_module()

class rig_biped_full:
                 
    def __init__(self):
        self.source_rba = None
        self.axis_x_suffix = ["_l","_r"]
        self.deform_prefix = "d_"    
        self.control_prefix = "c_"
        self.mech_prefix = "m_"
        return
        
    def go(self):
        
        print("Starting Operation: Rig Biped Full")
        
        #col = bpy.data.collections.new("rigbuddy_biped_full")        
        #bpy.context.scene.collection.children.link(col)
        
        #col_shapes = bpy.data.collections.new("rig_control_shapes") 
        #col.children.link(col_shapes)
        #controlshape_foot = Rigbuddy_Controlshape.foot().init().collection(col_shapes)
        #controlshape_circle_solid_z = Rigbuddy_Controlshape.circle_solid_z().init().collection(col_shapes)
        #controlshape_circle_solid_y = Rigbuddy_Controlshape.circle_solid_y().init().collection(col_shapes)
        
        controlshape_foot_ik = bpy.data.objects['controlshape_foot_ik']
        controlshape_circle_solid_z = bpy.data.objects['controlshape_circle_solid_z']
        controlshape_circle_solid_y = bpy.data.objects['controlshape_circle_solid_y']
        
        s_arma = self.source_rba.arma
        bpy.data.objects[s_arma.name].select_set(True)
        

        original = "o_"
        deform = "d_"
        control = "c_"
        mechanism = "m_"
        tweak = "t_"
        
        srba = self.source_rba        
        arma_new = bpy.data.armatures.new("Armature")
        arma = bpy.data.objects.new("Armature", arma_new)
        #col.objects.link(arma)        
        bpy.context.scene.collection.objects.link(arma)
        bpy.context.view_layer.objects.active = arma
        bpy.ops.object.editmode_toggle()
        arma.show_in_front = True

        
        bonelayer_control_basic = 1
        bonelayer_tweak = 7
        bonelayer_control_legik_left = 2
        bonelayer_control_legik_right = 18
        bonelayer_control_legfk_left = 3
        bonelayer_control_legfk_right = 19
        
        bonelayer_bone_basic = 8
        bonelayer_mech = 25
        
        layer_bone_basic = 8
        layer_bone_mech = 25
        layer_control_basic = 1
        layer_control_armik_left = 4
        layer_control_armik_right =20
        layer_control_armfk_left = 5
        layer_control_armfk_right = 21
        
        #update this
        
        arma = arma
        active_arma = RBS.activate_arma(arma) 
        
        bpy.ops.object.mode_set(mode='POSE')
        bpy.ops.pose.group_add()
        bpy.ops.pose.group_add()
        bpy.ops.pose.group_add()
        
        obj = bpy.data.objects[arma.name]
        bone_groups = obj.pose.bone_groups
        bone_groups.new(name="general_control_basic_world1")
        bga = bone_groups.active
        bonegroup_control_basic_world1 = bga        
        bga.color_set = 'CUSTOM'
        bga.colors.active = (1,.38,.42)
        bga.colors.select = (1,.38,.42)
        bga.colors.normal = (1,.38,.42)
        
        obj = bpy.data.objects[arma.name]
        bone_groups = obj.pose.bone_groups
        bone_groups.new(name="general_control_basic_world2")
        bga = bone_groups.active
        bonegroup_control_basic_world2 = bga        
        bga.color_set = 'CUSTOM'
        bga.colors.active = (1,.38,.42)
        bga.colors.select = (1,.38,.42)
        bga.colors.normal = (1,.38,.42)
        
        bga.colors.show_colored_constraints = True        
        bone_groups.new(name="general_control_basic_local1")
        bga = bone_groups.active
        bonegroup_control_basic_local1 = bga 
        bga.color_set = 'CUSTOM'
        bga.colors.active = (1,1,1)
        bga.colors.select = (1,1,1)
        bga.colors.normal = (1,1,1)
        bga.colors.show_colored_constraints = True   
         
        bga.colors.show_colored_constraints = True        
        bone_groups.new(name="general_control_basic_local2")
        bga = bone_groups.active
        bonegroup_control_basic_local2 = bga 
        bga.color_set = 'CUSTOM'
        bga.colors.active = (1,1,1)
        bga.colors.select = (1,1,1)
        bga.colors.normal = (1,1,1)
        bga.colors.show_colored_constraints = True   
        
        bpy.ops.object.mode_set(mode='EDIT')
           
        o_root = original+"root"
        eb_root = RBS.copy_bone_from_arma(s_arma,"root",arma,o_root)
        
        
        m = Rigbuddy_Mech_Spine.instance() 
        m.arma = arma
        m.bonelayer_bone_basic = bonelayer_bone_basic
        m.bonelayer_control_basic = bonelayer_control_basic
        
        m.bonegroup_control_basic_world1 = bonegroup_control_basic_world1
        m.bonegroup_control_basic_world2 = bonegroup_control_basic_world2
        m.bonegroup_control_basic_local1 = bonegroup_control_basic_local1
        m.bonegroup_control_basic_local2 = bonegroup_control_basic_local2
            
        m.rig_root = o_root
        
        active_arma = RBS.activate_arma(s_arma) 
        m.ebd_hip = RBS.editbone_data(active_arma.edit_bones["hip"])
        m.ebd_pelvis = RBS.editbone_data(active_arma.edit_bones["pelvis"])
        m.ebd_spine1 = RBS.editbone_data(active_arma.edit_bones["spine1"])
        m.ebd_spine2 = RBS.editbone_data(active_arma.edit_bones["spine2"])
        m.ebd_spine3 = RBS.editbone_data(active_arma.edit_bones["spine3"])
        m.ebd_spine4 = RBS.editbone_data(active_arma.edit_bones["spine4"])
        

        m.controlshape_c_hip = Rigbuddy_Controlshape.data(controlshape_circle_solid_y,100.0,True,True)
        m.controlshape_c_pelvis = Rigbuddy_Controlshape.data(controlshape_circle_solid_y,40.0,True,True)
        m.controlshape_c_spine1 = Rigbuddy_Controlshape.data(controlshape_circle_solid_y,18.0,True,True)
        m.controlshape_c_spine2 = Rigbuddy_Controlshape.data(controlshape_circle_solid_y,15.0,True,True)
        m.controlshape_c_spine3 = Rigbuddy_Controlshape.data(controlshape_circle_solid_y,12.0,True,True)
        m.controlshape_c_spine4 = Rigbuddy_Controlshape.data(controlshape_circle_solid_y,8,True,True)
        
        m.controlshape_t_pelvis = Rigbuddy_Controlshape.data(controlshape_circle_solid_y,3.0,True,True)
        m.controlshape_t_spine1 = Rigbuddy_Controlshape.data(controlshape_circle_solid_y,3.0,True,True)
        m.controlshape_t_spine2 = Rigbuddy_Controlshape.data(controlshape_circle_solid_y,3.0,True,True)
        m.controlshape_t_spine3 = Rigbuddy_Controlshape.data(controlshape_circle_solid_y,3.0,True,True)
        m.controlshape_t_spine4 = Rigbuddy_Controlshape.data(controlshape_circle_solid_y,3.0,True,True)
        
        o_hip = original+"hip"
        o_pelvis = original+"pelvis"
        o_spine1 = original+"spine1"
        o_spine2 = original+"spine2"
        o_spine3 = original+"spine3"
        o_spine4 = original+"spine4"   
         
        m.o_hip = o_hip
        m.o_pelvis = o_pelvis
        m.o_spine1 = o_spine1
        m.o_spine2 = o_spine2
        m.o_spine3 = o_spine3
        m.o_spine4 = o_spine4
        m.t_pelvis = tweak+"pelvis"
        m.t_spine1 = tweak+"spine1"
        m.t_spine2 = tweak+"spine2"
        m.t_spine3 = tweak+"spine3"
        m.t_spine4 = tweak+"spine4"
        
        m.t_m_pelvis = tweak+mechanism+"pelvis"
        m.t_m_spine1 = tweak+mechanism+"spine1"
        m.t_m_spine2 = tweak+mechanism+"spine2"
        m.t_m_spine3 = tweak+mechanism+"spine3"
        m.t_m_spine4 = tweak+mechanism+"spine4"
        
        m.c_hip = control+"hip"
        m.c_pelvis = control+"pelvis"
        m.c_spine1 = control+"spine1"
        m.c_spine2 = control+"spine2"
        m.c_spine3 = control+"spine3"
        m.c_spine4 = control+"spine4"        
        m.go()

         
                
        for i, axis in enumerate(self.axis_x_suffix):
                
            m = Rigbuddy_Mech_Arm.rigbuddy_mech_arm(arma,i,axis)
            m.init() 
            m.set_source(s_arma)
            m.set_layers(layer_bone_basic,layer_bone_mech,layer_control_basic,layer_control_armik_left,layer_control_armfk_left)
            m.set_arm_parent_id("o_spine4")        
            m.set_bonegroups(bonegroup_control_basic_local2,bonegroup_control_basic_local1,bonegroup_control_basic_world1)
            m.set_control_scale(10.0,10.0,10.0,10.0,10.0,10.0)
            m.go()
            
            m = Rigbuddy_Mech_Palm.rigbuddy_mech_palm(arma,i,axis)
            m.init() 
            m.set_source(s_arma)
            m.set_layers(layer_bone_basic,layer_control_basic)
            m.set_palm_parent_id("hand"+axis)        
            m.set_bonegroups(bonegroup_control_basic_world1)
            m.set_control_scale(10.0)
            m.go()
            
            m = Rigbuddy_Mech_Hand.rigbuddy_mech_hand(arma,i,axis)
            m.init() 
            m.set_source(s_arma)
            m.set_layers(layer_bone_basic,layer_control_basic)
            m.set_finger_parent_ids(["hand"+axis,"palm1"+axis,"palm2"+axis,"palm3"+axis,"palm4"+axis])        
            m.set_bonegroups(bonegroup_control_basic_local1)
            m.set_control_scale(10.0)
            m.go()
 
            m = Rigbuddy_Mech_Leg.rigbuddy_mech_leg(arma,i,axis)
            m.init() 
            #m.set_source(s_arma)
            #m.set_layers(layer_bone_basic,layer_control_basic)
            #m.set_finger_parent_ids(["hand"+axis,"palm1"+axis,"palm2"+axis,"palm3"+axis,"palm4"+axis])        
            #m.set_bonegroups(bonegroup_control_basic_local1)
            #m.set_control_scale(10.0)
            #m.go()

        body = bpy.data.objects["female_phat.001"]
        arma_modifier = body.modifiers[1]
        arma_modifier.target = arma
        
        bpy.data.objects[s_arma.name]
        
        RBS.activate_arma(arma) 
        bpy.data.objects[s_arma.name].select_set(False)  
        bpy.data.objects[arma.name].select_set(True)    