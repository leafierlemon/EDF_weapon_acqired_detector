@echo off
cd /d %~dp0
python ./scanWeapon_GCV.py %1 -t ./data/EDF5_WEAPON_LIST_JA.txt -c ./.account/test-ocr-353804-96ef00b6a9b5.json
pause