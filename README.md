# LRNN: Lipschitz-Regularization-of-Neural-Networks

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

The Table below highlightes how the measured lipschitz bound slowly approaches the true (empirical) lipschitz bound.

SL No. | Set Size (n) | Avg. Emp Value | Max. of Max Emp value
:---: | :---: | :---: | :---:
1 | 10 | 10.279830587380388 | 21.996063734099092
2 | 30 | 10.279830587380388 | 21.996063734099092
3 | 50 | 10.279830587380388 | 21.996063734099092
4 | 100 | 10.279830587380388 | 21.996063734099092
5 | 250 | 10.279830587380388 | 21.996063734099092
6 | 500 | 10.279830587380388 | 21.996063734099092
7 | 1000 | 10.279830587380388 | 21.996063734099092
8 | 2000 | 10.279830587380388 | 21.996063734099092
9 | 5000 | 10.279830587380388 | 21.996063734099092

## Acknowledgements

Parts of the codebase has been borrowed from the [LipSDP](https://github.com/arobey1/LipSDP) repository. We are grateful to the authors for making their work publicly available. 
