#!/bin/bash

read -p "What would you like to do?
	1 Exit,
	2 Deploy DORA-VIEW app,
	3 Deploy APP_20,
	4 Deploy app_minimal: " choice

echo $choice

# Activate virtual environment
if [ -f "./doraview/venv/bin/activate" ]; then
    cmd source ./doraview/venv/bin/activate .
    echo "Virtual environment activated"
else
    echo "Warning: Virtual environment not found at ./doraview/venv/bin/activate"
    echo "Continuing without activating venv..."
fi

# Check if Python is installed
if [ "$choice" == 1 ]; then
	echo "Exiting"
	exit 1

elif [ "$choice" == 2 ]; then
	echo "Deploying DORA-VIEW app"
	python3 ./doraview/app.py

elif [ "$choice" == 3 ]; then
	echo "Deploying APP_20"
	python3 ./dash_app/app_20.py

elif [ "$choice" == 4 ]; then
	echo "Deploying app_minimal"
	python3 ./venv/bin/python3 ./dash_app/app_minimal.py
else
	echo "Unknown choice: $choice Exiting..."
	exit 1
fi