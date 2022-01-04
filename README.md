# Motion quality assessment for JDM


## Directory structure

```shell script
├── data
│   ├── 1
│   │   └── AA.FBX
│   ├── 2
│   │   └── 1_00.FBX
│   └── 3
│       └── Aim.fbx
├── test.py
└── utils
    ├── fbx2json
    │   ├── 1_00
    │   │   └── JointDict
    │   └── AA
    │       └── JointDict
    ├── fbx2npy.py
    ├── homefile.blend
    ├── homefile.blend1
    ├── json2npy
    └── visualize_frames.py
```

## `FBX` to `NPY` converter

```shell script
cd ./utils
blender --background -P fbx2npy.py
```
