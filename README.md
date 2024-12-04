# Phenotyping

To run the phenotyping playground demo, position yourself in the project root and execute the following

```
python demo.py
```

## Segmentation

### Grounding DINO Setup

1. Change the current directory to the GroundingDINO folder.

```
cd modules/segmentation/GroundingDINO/
```

2. Install the required dependencies in the current directory.

```
pip install -e .
```

3. Download pre-trained model weights

```
mkdir weights
cd weights
wget -q https://github.com/IDEA-Research/GroundingDINO/releases/download/v0.1.0-alpha/groundingdino_swint_ogc.pth
```
