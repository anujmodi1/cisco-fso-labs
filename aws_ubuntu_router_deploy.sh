#!/bin/sh
export AWS_PAGER=""
cp config ~/.aws
rm -rf __pycache__
export AWS_PAGER=""
python3 aws_ubuntu_router_deploy.py

