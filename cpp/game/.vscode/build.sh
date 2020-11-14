# /usr/bin/g++ -g src/*.cpp -I include -o main

#cleanup old file
rm main

echo compiling

#compiler options

CFLAGS="-g -Wall"
LSDL2FLAGS="-lSDL2"

INCDIR="include"
SRCDIR="src"

OUTPUT="main"

g++ -o $OUTPUT -I $INCDIR src/*.cpp $LSDL2FLAGS $CFLAGS