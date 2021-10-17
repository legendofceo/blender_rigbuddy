import bpy
from mathutils import Vector, Quaternion
context = bpy.context

Rigbuddy_Arma = bpy.data.texts["rigbuddy_arma.py"].as_module()
Rigbuddy_Ops = bpy.data.texts["rigbuddy_op.py"].as_module()

axis_x_suffix = ["_l","_r"]               

#source_rig = op_rig_biped_source()
#source_rig.go()

selected_object = bpy.context.view_layer.objects.active
arma = selected_object.data 
source_rba = Rigbuddy_Arma.armature().set_armature(arma)
        
op = Rigbuddy_Ops.rig_biped_full()
op.source_rba = source_rba
op.axis_x_suffix = axis_x_suffix
op.dfm_prefix = "d_"
op.go()