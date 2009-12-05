#!/bin/bash

mkdir ~/.wine/drive_c/steam
cd ~/.wine/drive_c/steam
cabextract SteamInstall.msi
wine SteamService.exe
