#!/bin/bash
yes | conda create --name py2 python=2.7
source /opt/conda/etc/profile.d/conda.sh
conda activate py2
pip install pycuda
