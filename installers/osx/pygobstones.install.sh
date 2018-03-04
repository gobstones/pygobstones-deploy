#!/bin/bash
# Author: Ary Pablo Batista <arypbatista@gmail.com>

PYGOBSTONES_VERSION=1.5.4
UI_URL="https://github.com/gobstones/pygobstones/archive/v$PYGOBSTONES_VERSION.tar.gz"
LANG_URL="https://github.com/gobstones/pygobstones-lang/archive/v$PYGOBSTONES_VERSION.tar.gz"

TEMP_DIR=`mktemp -d`
DEST_DIR=~/pygobstones

echo "[PyGobstones] PyGobstones $PYGOBSTONES_VERSION installation started."
echo "[PyGobstones] Installing dependencies"
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install cartr/qt4/pyqt
brew install wget

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

echo "[PyGobstones] Storing PyGobstones in $DEST_DIR folder."
rm -rf $DEST_DIR
mkdir -p $DEST_DIR
cp -r $TEMP_DIR/* $DEST_DIR

echo "[PyGobstones] Creating symbolic link to pygobstones."
mkdir $DEST_DIR/path
ln -s $DEST_DIR/pygobstones-lang.py $DEST_DIR/path/pygobstones-lang
ln -s $DEST_DIR/pygobstones.py $DEST_DIR/path/pygobstones
echo "PATH=\$PATH:$DEST_DIR/path" >> ~/.bash_profile
echo "PYTHONPATH=\$PYTHONPATH:\`brew --prefix\`/lib/python2.7/site-packages" >> ~/.bash_profile
echo "export PYTHONPATH" >> ~/.bash_profile

echo "[PyGobstones] Success."
echo ""
echo "[PyGobstones] Commands:"
echo "[PyGobstones]   - pygobstones : launch PyGobstones v$PYGOBSTONES_VERSION GUI."
echo "[PyGobstones]   - pygobstones-lang : use PyGobstones v$PYGOBSTONES_VERSION Language from command line."
echo ""
echo "Script created by Ary Pablo Batista <arypbatista@gmail.com>."
