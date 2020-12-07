#!/bin/bash
echo votre version python est :
pip --version
echo nous avons codé et testé notre programme avec python 3.8, nous vous conseillons donc d utiliser python 3.8.
echo installation des dependances 
pip install tkfilebrowser
pip install Pillow
pip install cx_Freeze
echo dependances OK
echo si vous avez un : TypeError: NoneType object is not subscriptable, modifiez /projet/lib/python3.8/site-packages/tkfilebrowser/constants.py et supprimer les lignes 82, 83, 84
