# Motion quality assessment for JDM


## Directory structure

```shell script
©À©¤©¤ data
©¦?? ©À©¤©¤ 1
©¦?? ©¦?? ©¸©¤©¤ AA.FBX
©¦?? ©À©¤©¤ 2
©¦?? ©¦?? ©¸©¤©¤ 1_00.FBX
©¦?? ©¸©¤©¤ 3
©¦??     ©¸©¤©¤ Aim.fbx
©À©¤©¤ test.py
©¸©¤©¤ utils
    ©À©¤©¤ fbx2json
    ©¦?? ©À©¤©¤ 1_00
    ©¦?? ©¦?? ©¸©¤©¤ JointDict
    ©¦?? ©¸©¤©¤ AA
    ©¦??     ©¸©¤©¤ JointDict
    ©À©¤©¤ fbx2npy.py
    ©À©¤©¤ homefile.blend
    ©À©¤©¤ homefile.blend1
    ©À©¤©¤ json2npy
    ©¸©¤©¤ visualize_frames.py
```

## `FBX` to `NPY` converter

```shell script
cd ./utils
blender --background -P fbx2npy.py
```
