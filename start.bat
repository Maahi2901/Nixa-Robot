@echo off
TITLE Nixa Robot 
:: Enables virtual env mode and then starts asuna
env\scripts\activate.bat && py -m NixaRobot
