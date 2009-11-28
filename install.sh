#!/bin/bash

mkdir steam
cd steam
wget http://storefront.steampowered.com/download/SteamInstall.msi
cabextract SteamInstall.msi
wine SteamService.exe
