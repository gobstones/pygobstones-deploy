#!/bin/bash
# Author: Ary Pablo Batista <arypbatista@gmail.com>

PYGOBSTONES_VERSION=1.5.4
UI_URL="https://github.com/gobstones/pygobstones/archive/v$PYGOBSTONES_VERSION.tar.gz"
LANG_URL="https://github.com/gobstones/pygobstones-lang/archive/v$PYGOBSTONES_VERSION.tar.gz"

TEMP_DIR=`mktemp -d`

echo "[PyGobstones] PyGobstones $PYGOBSTONES_VERSION installation started."
echo "[PyGobstones] Installing dependencies"
apt-get install -y python2.7 python-qt4

echo "[PyGobstones] Downloading PyGobstones files"
wget -O $TEMP_DIR/pygobstones.tar.gz $UI_URL
wget -O $TEMP_DIR/pygobstones-lang.tar.gz $LANG_URL

echo "[PyGobstones] Unpacking PyGobstones files"
tar -zxf $TEMP_DIR/pygobstones-lang.tar.gz -C $TEMP_DIR
rm $TEMP_DIR/pygobstones-lang.tar.gz
cp -R $TEMP_DIR/pygobstones-lang-*/* $TEMP_DIR/
rm -R $TEMP_DIR/pygobstones-lang-*/

tar -zxf $TEMP_DIR/pygobstones.tar.gz -C $TEMP_DIR
rm $TEMP_DIR/pygobstones.tar.gz
cp -R $TEMP_DIR/pygobstones-*/* $TEMP_DIR/
rm -R $TEMP_DIR/pygobstones-*/

echo "[PyGobstones] Storing PyGobstones in /opt/pygobstones folder."
rm -rf /opt/pygobstones
mkdir -p /opt/pygobstones
cp -r $TEMP_DIR/* /opt/pygobstones

echo "[PyGobstones] Creating symbolic link to pygobstones."
rm -rf /usr/bin/pygobstones
ln -s /opt/pygobstones/pygobstones.py /usr/bin/pygobstones
rm -rf /usr/bin/pygobstones-lang
ln -s /opt/pygobstones/pygobstones-lang.py /usr/bin/pygobstones-lang

echo "[PyGobstones] Success."
echo ""
echo "[PyGobstones] Commands:"
echo "[PyGobstones]   - pygobstones : launch PyGobstones v$PYGOBSTONES_VERSION GUI."
echo "[PyGobstones]   - pygobstones-lang : use PyGobstones v$PYGOBSTONES_VERSION Language from command line."
echo ""
echo "Script created by Ary Pablo Batista <arypbatista@gmail.com>."
