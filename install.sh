#!/bin/bash

mkdir ~/.wine/drive_c/steam
cd ~/.wine/drive_c/steam
wget http://storefront.steampowered.com/download/SteamInstall.msi
cabextract SteamInstall.msi
wine SteamService.exe
