# Motion quality assessment for JDM


## `fbx` to `npz` converter

By the following script, the original data format can be converted from `fbx` to `npz`.

```shell script
cd ./utils
blender --background -P fbx2npz.py
```

The original data is located in `./data/fbx`, while the obtained data is located in `./data/npz`. 

The original topology (a-b) and the converted topology (c) are as follows:

| ![](data/topology/skeleton_body.jpg) | ![](data/topology/skeleton_hand.jpg) | ![](data/topology/topology.jpg) |
| :----------------------------------: | :----------------------------------: | :-----------------------------: |
|               (a) Body               |               (b) Hand               |            (c) Ours             |


Compared with [MediaPipe Pose landmarks](https://google.github.io/mediapipe/solutions/pose.html#pose-landmark-model-blazepose-ghum-3d), ours (c) has less joints in the face, hand and foot.

The generated motion is as follows:

![](outputs/ani/ani.gif)