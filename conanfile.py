import os
import shutil
from conans import ConanFile, CMake, tools


class BamtoolsConan(ConanFile):
    name = "bamtools"
    version = "2.5.1"
    license = "MIT"
    url = "https://github.com/altairwei/conan-bamtools.git"
    description = "C++ API & command-line toolkit for working with BAM data"
    topics = ("conan", "Bioinformatics", "BAM format", "samtools")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    _source_subfolder = "source_subfolder"

    def source(self):
        url = 'https://github.com/pezmaster31/bamtools/archive/v%s.tar.gz' % self.version
        tools.get(url)

        if os.path.exists(self._source_subfolder) and os.path.isdir(self._source_subfolder):
            shutil.rmtree(self._source_subfolder)
        os.rename("bamtools-" + self.version, self._source_subfolder)
        tools.replace_in_file(
            self._source_subfolder + "/CMakeLists.txt",
            "project( BamTools LANGUAGES CXX VERSION %s )" % self.version,
            ("project( BamTools LANGUAGES CXX VERSION %s )\n" % self.version) +
            "include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)\n" +
            "conan_basic_setup()"
        )


    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self._source_subfolder)
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="hello")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]

