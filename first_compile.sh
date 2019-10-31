cd bitcoin
./autogen.sh
./configure #--disable-wallet # --prefix=`pwd`/depends/x86_64-linux-gnu
make -j8
cd ..
./run.sh