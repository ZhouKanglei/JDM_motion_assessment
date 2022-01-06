import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation
# plt.style.use('science')

plt.rcParams['font.family'] = 'serif'
plt.rcParams['savefig.dpi'] = 300
plt.rcParams["savefig.format"] = 'pdf'
plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['text.usetex'] = True

BONES = [[0, 1], [1, 2], [1, 3], [2, 4], [2, 14],
         [4, 6], [6, 12], [6, 10], [6, 8], [3, 5],
         [3, 15], [5, 7], [7, 13], [7, 11], [7, 9],
         [14, 15], [14, 16], [16, 18], [18, 20], [15, 17],
         [17, 19], [19, 21]]

PARTS = [[2, 4, 6],  # left arm
         [3, 5, 7],  # right arm
         [14, 16, 18, 20],  # left leg
         [15, 17, 19, 21],  # right leg
         [0, 1]]  # trunk

part_color = ['magenta', 'magenta', 'green', 'green', 'blue']

def vis_skeleton(data, fig_name='ani', output_dir='outputs/ani', bones=BONES, parts=PARTS):

    data = data.transpose(0, 2, 1)

    def plot_joint_bone(skeleton):
        for i, j in bones:
            joint_locs = skeleton[:, [i, j]]
            part_idx_i, part_idx_j = search_part_idx(i), search_part_idx(j)
            if part_idx_i != part_idx_j:
                part_idx = -1
            else:
                part_idx = part_idx_i

            # plot them
            ax.plot(joint_locs[0], joint_locs[1], joint_locs[2], color=part_color[part_idx], linewidth=1)

        for jnt_idx in range(len(skeleton.transpose(1, 0))):
            jnt = skeleton.transpose(1, 0)[jnt_idx]
            part_idx = search_part_idx(jnt_idx)
            ax.plot(jnt[0], jnt[1], jnt[2], color=part_color[part_idx], marker='o', markersize=1, alpha=1)

    # get the idx of parts for the joint
    def search_part_idx(idx):
        for i in range(len(parts)):
            if idx in parts[i]:
                return i
        return -1

    fig = plt.figure()
    for i_num in range(5):
        index = i_num * 5 + 2
        ax = fig.add_subplot(1, 5, i_num + 1, projection='3d')
        skeleton = data[index]
        # ax.view_init(elev=45, azim=-15)

        plot_joint_bone(skeleton)

        ax.set_title(f'{index}-th', fontsize=6)
        plt.axis('off')

    os.makedirs(output_dir, exist_ok=True)
    file_name = os.path.join(output_dir, f'{fig_name}.pdf')
    plt.savefig(file_name)
    print('Save fig to {}'.format(file_name))

    file_name = os.path.join(output_dir, f'{fig_name}.jpg')
    plt.savefig(file_name)
    print('Save fig to {}'.format(file_name))

    # animation
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    global skeleton_index
    skeleton_index = [0]

    def animate(skeleton):
        ax.clear()
        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])
        ax.set_zlim([-1, 1])

        plot_joint_bone(skeleton)

        ax.set_xlabel('$x$')
        ax.set_ylabel('$y$')
        ax.set_zlabel('$z$')

        skeleton_index[0] += 1
        plt.title(f'Frame \#{skeleton_index[0]}')

        print('-', end='')
        return ax

    ani = FuncAnimation(fig, animate, data, repeat=False, interval=5)
    os.makedirs(output_dir, exist_ok=True)
    file_name = os.path.join(output_dir, f'{fig_name}.gif')
    ani.save(file_name, writer='pillow', fps=10)
    print('\nSave animation to {}'.format(file_name))



if __name__ == '__main__':
    vis_skeleton()
