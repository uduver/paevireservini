#!/bin/bash
python3 -m http.server -d /usr/src/app/output 8080 &
python3 ./main.py