## How to use conan-bamtools

Currently `conan-bamtools` is only uploaded to my personal conan repository, so you will first need to add my conan repository:

```shell
conan remote add altairwei https://api.bintray.com/conan/altairwei/conan 
```

Then add `bamtools/2.5.1@altairwei/testing` to your dependencies.

After you add `conan-bamtools` as your project dependency using conan-related techniques, you can find the header files under paths like `BamTools/api/BamWriter.h`:

```C++
#include "BamTools/api/BamMultiReader.h"
#include "BamTools/api/BamWriter.h"
using namespace BamTools;
```

If you are using `conan-bamtools` with `cmake_find_package` generator, then the relevant variables are named `bamtools_INCLUDES` and `bamtools_LIBRARIES`:

```cmake
cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

find_package(bamtools REQUIRED)

add_executable(example example.cpp)
target_include_directories(example PRIVATE ${bamtools_INCLUDES})
target_link_libraries(example ${bamtools_LIBRARIES})
```