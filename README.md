# LRNN: Lipschitz-Analysis-of-Neural-Networks

## About

This repository contains the implementation of this [technical report](https://sarosijbose.github.io/files/Report_IISc_internship.pdf). This work was carried out under the supervision of [Prof. Kunal Chaudhury](https://sites.google.com/site/kunalnchaudhury/home?authuser=0) at Indian Institute of Science, Bangalore. 

A mini implementation of this project can be found in this [repo](https://github.com/sarosijbose/Trivial-Lipschitz-Bound-Estimation).

## Setup

1. It is recommended to setup a fresh virtual environment first
```bash
python -m venv lrnn
source activate env/bin/activate
```
2. Install the required packages.

```bash
pip install -r requirements.txt
```
3. Run the ```main.py``` file in the ```code``` folder. Set the checkpoint paths accordingly.

4. All the checkpoints and other dependencies are present in the ```data``` folder.

## Results

## Acknowledgements

Parts of the codebase has been borrowed from the [LIPSDP](https://github.com/arobey1/LipSDP) repository. We are grateful to the authors for making their work publicly available. 
