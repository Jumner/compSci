# /usr/bin/g++ -g src/*.cpp -I include -o main

#cleanup old file
rm main

echo compiling

#compiler options

CFLAGS="-g -Wall"
LSDL2FLAGS="-lSDL2 -lGL -lGLEW"

INCDIR="include"
SRCDIR="src"

OUTPUT="main"

g++ $CFLAGS $LSDL2FLAGS $SRCDIR/*.cpp -I $INCDIR -o $OUTPUT