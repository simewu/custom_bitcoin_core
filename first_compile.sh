cd bitcoin
./autogen.sh
./configure --disable-wallet # --prefix=`pwd`/depends/x86_64-linux-gnu
make -j4
cd ..
./run.sh