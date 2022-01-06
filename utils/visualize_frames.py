import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def visualise_frames(pathtonpy='data/npz/JDM_motion.npz',up_view=0,side_view=90,x_lim=[-2,2],y_lim=[-2,2],z_lim=[-2,2]):
    #MIXAMO DATASET
    """
    Each POSE follow the given index joints below:
    
        0 - Head
        fbx - Neck
        2 - Lshoulder
        3 - Lelbow
        4 - Lwrist
        5 - Rshoulder
        6 - Relbow
        7 - Rwrist
        8 - Pelvis
        9 - Lhip
        10 - Lknee
        11 - Lankle
        12 - Rhip
        13 - Rknee
        14 - Rankle
    """
    #Load .npy file
    motion3d = np.load(pathtonpy)['data']
    motion3d = motion3d.reshape(1,77,22,3)
    motion3d = motion3d[0]
    motion3d = motion3d.transpose(1,2,0)

    #Index for bone links
    bones = [[0,1],[1,2],[1,3],[2,4],[2,14],[4,6],[6,12],[6,10],[6,8],[3,5],[3,15],[5,7],[7,13],[7,11],[7,9],[14,15],[14,16],[16,18],[18,20],[15,17],[17,19],[19,21]]

    #Set offset for few frame visualisation
    offset = int(motion3d.shape[2]/5)
    offset_sum = 0
    fig = plt.figure()
    plt.ion()
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(elev=140,azim=-90)

    #Output frames
    for i in range(motion3d.shape[2]):
        ax.lines.clear()
        # ax.scatter(motion3d[:,0,i],motion3d[:,1,i],motion3d[:,2,i])
        ax.set_xlim(x_lim)
        ax.set_ylim(y_lim)
        ax.set_zlim(z_lim)
        for i in range(len(bones)):
            ax.plot3D([motion3d[bones[i][0],0,offset_sum],motion3d[bones[i][1],0,offset_sum]],[motion3d[bones[i][0],1,offset_sum],motion3d[bones[i][1],1,offset_sum]],[motion3d[bones[i][0],2,offset_sum],motion3d[bones[i][1],2,offset_sum]], c="#3498db")

        RADIUS = 0.5  # space around the subject
        xroot, yroot, zroot = motion3d[1, 0, i], motion3d[1, 1, i], motion3d[1, 2, i]
        ax.set_xlim3d([-RADIUS + xroot, RADIUS + xroot])
        ax.set_zlim3d([-RADIUS, 2 * RADIUS + zroot])
        ax.set_ylim3d([-RADIUS + yroot, RADIUS + yroot])

        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")

        plt.pause(0.001)
        # ax.set_title('Frame: %d'%(offset_sum))

    plt.ioff()
    plt.show()

if __name__ == '__main__':
    visualise_frames()
