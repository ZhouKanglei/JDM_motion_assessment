# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 2022/fbx/4 21:13

import bpy
import os
from mathutils import Vector
import numpy as np

HOME_FILE_PATH = os.path.abspath('homefile.blend')
MIN_NR_FRAMES = 64
RESOLUTION = (512, 512)

# Crucial joints sufficient for visualisation # FIX ME - Add more joints if desirable for MixamRig
BASE_JOINT_NAMES = [
    'head', 'neck',
    'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow', 'left_wrist', 'right_wrist',
    'left_little_distal', 'right_little_distal', 'left_index_distal', 'right_index_distal',
    'right_thumb_distal', 'left_thumb_distal',
    'left_hip', 'right_hip', 'left_knee', 'right_knee', 'left_ankle', 'right_ankle',
    'left_foot_index', 'right_foot_index'
]

# Source directory where .fbx exist
SRC_DATA_DIR = '../data/fbx'

# Final directory where NPY files will ve stored
FINAL_DIR_PATH = '../data/npz'

# Number of joints to be used from MixamoRig
joint_names = [x for x in BASE_JOINT_NAMES]


def fbx2npz():
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

    data, label = [], []
    for anim_name in anims_path:

        anim_file_path = os.path.join(SRC_DATA_DIR, anim_name)

        # Load HOME_FILE and .fbx file
        bpy.ops.wm.read_homefile(filepath=HOME_FILE_PATH)
        bpy.ops.import_scene.fbx(filepath=anim_file_path)

        # End Frame Index for .fbx file
        frame_end = bpy.data.actions[0].frame_range[1]

        motion = []
        for i in range(int(frame_end) + 1):

            bpy.context.scene.frame_set(i)

            bone_struct = bpy.data.objects['bip001'].pose.bones

            armature = bpy.data.objects['bip001']

            frame = []
            for name in joint_names:
                global_location = armature.matrix_world @ bone_struct[name].matrix @ Vector((0, 0, 0))
                l = [global_location[0], global_location[1], global_location[2]]
                frame.append(np.array(l))
            motion.append(np.array(frame))

        data.append(np.array(motion))
        label.append(anim_name)

    data = np.array(data)

    filename = os.path.join(FINAL_DIR_PATH, 'JDM_motion.npz')
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    np.savez(filename, data=data, label=label)
    print(f'Save [{filename}]')

if __name__ == '__main__':
    # Convert .fbx files to .npz file
    fbx2npz()



