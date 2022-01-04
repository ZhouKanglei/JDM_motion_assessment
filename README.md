# Motion quality assessment for JDM


## Directory structure

```shell script
.
├── data
│   ├── raw
│   │   ├── AA.FBX
│   │   └── BB.FBX
│   └── tmp
│       └── JDM_motion.npz
├── README.md
├── test.py
└── utils
    ├── fbx2npy.py
    ├── fbx2npz.py
    └── visualize_frames.py
```

## `FBX` to `NPY` converter

```shell script
cd ./utils
blender --background -P fbx2npz.py
```
