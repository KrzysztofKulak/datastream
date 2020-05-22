#!/usr/bin/env sh
cd dataqueue
python -m unittest
cd ../datamanager
python -m unittest
cd ../dataproducer
python -m unittest