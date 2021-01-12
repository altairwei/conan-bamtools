## How to use conan-bamtools

Currently `conan-bamtools` is only uploaded to my personal conan repository, so you will first need to add my conan repository:

```shell
conan remote add altairwei https://api.bintray.com/conan/altairwei/conan 
```

After you add `conan-bamtools` as your project dependency using conan-related techniques, you can find the header files under paths like `BamTools/api/BamWriter.h`:

```C++
#include "api/BamMultiReader.h"
#include "api/BamWriter.h"
using namespace BamTools;
```

If you are using conan-bamtools in CMake, then the relevant variables are named `jjj` and `sss`