# /usr/bin/g++ -g src/*.cpp -I include -o main

#cleanup old file
rm main
rm main.o
rm cppGood_d.pyd

echo compiling

#compiler options

INCDIR="include"
SRCDIR="src"

OUTPUT="main"


# g++ -o $OUTPUT -I $INCDIR src/*.cpp $CFLAGS
python3 setup.py build
sudo python3 setup.py install

echo "\n\nPROGRAM\n"

python3 python/main.py