# IfcOpenShell 101

### Computational Design Day 2024

Python notebooks for interaction with IFC data models

### Setup

- Install Miniconda (a Python distribution with optimized binary packages)

  https://docs.conda.io/projects/miniconda/en/latest/
  
- Activate the "anaconda command prompt" and run

  ```
  conda create -n ifopsh07 conda-forge::pythonocc-core==7.5.1 python<3.11 numpy scipy matplotlib
  conda activate ifopsh07
  python -m pip install networkx ifcopenshell jupyter lark pythreejs
  ```

