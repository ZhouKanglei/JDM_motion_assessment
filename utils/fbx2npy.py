import bpy
import os
import json
from mathutils import Vector
import numpy as np 

HOME_FILE_PATH = os.path.abspath('homefile.blend')
MIN_NR_FRAMES = 64
RESOLUTION = (512, 512)

# Crucial joints sufficient for visualisation # FIX ME - Add more joints if desirable for MixamRig
BASE_JOINT_NAMES = [
    'Head', 'Neck',
    'left_Shoulder', 'right_Shoulder', 'left_elbow', 'right_elbow', 'left_wrist', 'right_wrist',
    'left_little_distal', 'right_little_distal', 'left_index_distal', 'right_index_distal',
    'right_thumb_distal', 'left_thumb_distal',
    'left_hip', 'right_hip', 'left_knee', 'right_knee', 'left_ankle', 'right_ankle',
    'left_foot_index', 'right_foot_index'
]

# Source directory where .fbx exist
SRC_DATA_DIR = '../data/raw'

# Ouput directory where .fbx to JSON dict will be stored
OUT_DATA_DIR ='../data/tmp/fbx2json'

# Final directory where NPY files will ve stored
FINAL_DIR_PATH ='../data/tmp/json2npy'

# Number of joints to be used from MixamoRig
joint_names = [x for x in BASE_JOINT_NAMES]

def fbx2jointDict():
    
    # Remove 'Cube' object if exists in the scene
    if bpy.data.objects.get('Cube') is not None:
        cube = bpy.data.objects['Cube']
        bpy.data.objects.remove(cube)
    
    # Intensify Light Point in the scene
    if bpy.data.objects.get('Light') is not None:
        bpy.data.objects['Light'].data.energy = 2
        bpy.data.objects['Light'].data.type = 'POINT'
    
    # Set resolution and it's rendering percentage
    bpy.data.scenes['Scene'].render.resolution_x = RESOLUTION[0]
    bpy.data.scenes['Scene'].render.resolution_y = RESOLUTION[1]
    bpy.data.scenes['Scene'].render.resolution_percentage = 100
    
    # Base file for blender
    bpy.ops.wm.save_as_mainfile(filepath=HOME_FILE_PATH)
    
    # Get animation(.fbx) file paths
    anims_path = os.listdir(SRC_DATA_DIR)
    
    # Make OUT_DATA_DIR
    os.makedirs(OUT_DATA_DIR, exist_ok=True)

    for anim_name in anims_path:
        
        anim_file_path = os.path.join(SRC_DATA_DIR,anim_name)
        save_dir = os.path.join(OUT_DATA_DIR,anim_name.split('.')[0], 'JointDict')
        
        # Make save_dir
        os.makedirs(save_dir, exist_ok=True)
        
        # Load HOME_FILE and .fbx file
        bpy.ops.wm.read_homefile(filepath=HOME_FILE_PATH)
        bpy.ops.import_scene.fbx(filepath=anim_file_path)
        
        # End Frame Index for .fbx file
        frame_end = bpy.data.actions[0].frame_range[1]

        # print all objects
        for obj in bpy.data.objects:
            print('---- ', obj.name)
        
        for i in range(int(frame_end) + 1):
            
            bpy.context.scene.frame_set(i)

            bone_struct = bpy.data.objects['Bip001'].pose.bones
            # print(bone_struct.keys())

            armature = bpy.data.objects['Bip001']

            out_dict = {'pose_keypoints_3d': []}
        
            for name in joint_names:
                global_location = armature.matrix_world @ bone_struct[name].matrix @ Vector((0, 0, 0))
                l = [global_location[0], global_location[1], global_location[2]]
                out_dict['pose_keypoints_3d'].extend(l)
            
            save_path = os.path.join(save_dir,'%04d_keypoints.json'%i)
            with open(save_path,'w') as f:
                json.dump(out_dict, f)

def jointDict2npy():
    
    json_dir = OUT_DATA_DIR
    npy_dir = FINAL_DIR_PATH
    if not os.path.exists(npy_dir):
        os.makedirs(npy_dir)
        
    anim_names = os.listdir(json_dir)
    print('======', anim_names)
    
    for anim_name in anim_names:
        files_path = os.path.join(json_dir, anim_name, 'JointDict')
        frame_files = os.listdir(files_path)

        motion = []
        for frame_file in frame_files:
            file_path = os.path.join(files_path, frame_file)
            
            with open(file_path) as f:
                info = json.load(f)
                joint = np.array(info['pose_keypoints_3d']).reshape((-1, 3))
            motion.append(joint)
            
        motion = np.stack(motion, axis=2)
        save_path = os.path.join(npy_dir,anim_name)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
            
        print(save_path)
        
        np.save(save_path + '/' + '{i}.npy'.format(i=anim_name), motion)
        
if __name__ == '__main__':
    
    # Convert .fbx files to JSON dict
    fbx2jointDict()
    
    # Convert JSON dict to NPY 
    jointDict2npy()           


