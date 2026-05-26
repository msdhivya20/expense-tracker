#!/usr/bin/env bash

set -o errexit

pip install --upgrade pip

# install numpy/scipy first (prevents build chaos)
pip install numpy==1.26.4
pip install scipy==1.11.4
pip install scikit-learn==1.4.2

# install rest
pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate