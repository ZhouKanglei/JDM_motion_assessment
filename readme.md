# Motion quality assessment for JDM


## Skeleton topolopy

![](data/topology/pose_tracking_full_body_landmarks.png)


## `fbx` to `npz` converter

The original topology is as follows:

<center>
    <img src="./data/topology/skeleton_body.jpg" width="48%" align=left>
    <img src="./data/topology/skeleton_hand.jpg" width="48%" align=right>
</center>

![](data/topology/skeleton_body.jpg)![](data/topology/skeleton_hand.jpg)

By the following script, the original data format can be converted from `fbx` to `npz`.

```shell script
cd ./utils
blender --background -P fbx2npz.py
```

The original data is located in `./data/fbx`, while the obtained data is located in `./data/npz`.

The obtained topology is as follows:

![](data/topology/topology.jpg)
