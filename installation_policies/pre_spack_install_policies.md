This document lists the installation policies prior to [PR20](https://github.com/xsdk-project/xsdk-community-policies/pull/20), which changed policy M1 from requiring CMake/Autoconf installation to Spack based installation.

----

1. Implement the default behavior described below. Each package can decide whether XSDK mode is the default mode.<sup>4</sup>

    1. `--dis/enable-xsdk-defaults`
    2. `USE_XSDK_DEFAULTS=[YES,NO]`
  
<sup>4</sup> For packages like Trilinos that need to maintain backward compatibility over consecutive releases, 
`USE_XSDK_DEFAULTS` may be `FALSE` by default.

----

2. Identify location to install package. Multiple "versions" of packages, such as debug and release, can be installed by 
using different prefix directories.

    1. `--prefix=directory`
    2. `CMAKE_INSTALL_PREFIX=directory`

----

3. Select compilers<sup>5</sup> and compiler flags.

    1. If the compilers (and or flags) are explicitly set on input, use those:

        1. `CC=<cc>`,  `CXX=<cxx>`,  `FC=<fc>`,  `CPP`, `FFLAGS`, `FCFLAGS`, `CFLAGS`, `CXXFLAGS`, `CPPFLAGS`, `LDFLAGS`

        2. `CMAKE_C_COMPILER=<cc>`, `CMAKE_CXX_COMPILER=<cxx>`, `CMAKE_Fortran_COMPILER=<fc>`, `CMAKE_C_FLAGS="<flag1> <flag2> ...”`, `CMAKE_CXX_FLAGS=”...”`, `CMAKE_Fortran_FLAGS=”...”`

    2. If the compilers and/or flags are not explicitly set on input but are set in the environment variables
    `FC`, `CC`, `CXX`, `CPP`<sup>6</sup>, `FFLAGS`, `FCFLAGS`, `CFLAGS`, `CXXFLAGS`, `CPPFLAGS`,<sup>7</sup>
    `LDFLAGS`, then the compilers and flags must be set to these.  If both `FFLAGS` and `FCFLAGS` are set, then they
    need to be the same or it is an error.

    3. If the compilers and/or compiler flags are not explicitly passed in or defined in the environment variables listed 
    above, then the package is free to try to find compilers on the system and set the compiler flags consistent with the 
    other settings defined below (e.g., shared libraries vs. static libraries, debug vs. non-debug).<sup>8</sup>

<sup>5</sup> Packages must support using the MPI compiler wrappers for these arguments.

<sup>6</sup> The environment variable CPP is not supported by raw CMake.

<sup>7</sup> The environment variable CPPFLAGS is not supported by raw CMake.

<sup>8</sup> All CMake projects should use the same built-in CMake algorithm to find the default compilers, so even when no 
explicit compilers or flags are set they should use the same compilers and flags.  Also, raw CMake projects will append 
compiler flags based on the build type.  See "Selecting compiler and linker options".

----

4. Create libraries with debugging information and possible additional error checking (default is debug in XSDK mode).

    1. `--dis/enable-debug` 

    2. `CMAKE_BUILD_TYPE=[Debug,Release]`

----

5. Select option used for indicating whether to build shared libraries (default is shared in XSDK mode).

    1. `--dis/enable-shared (configure)` 

    2. `BUILD_SHARED_LIBS=[YES,NO]` 

----

6. Build interface for a particular additional language.

    1.  `--dis/enable-<language>` 

    2. `XSDK_ENABLE_<language>=[YES,NO]` 


7. Determine precision for packages that build only for one precision (default is double). Packages that handle all 
precisions automatically are free to ignore this option.

    1. `--with-precision=[single,double,quad]`

    2. `XSDK_PRECISION=[SINGLE,DOUBLE,QUAD]` 

----

8. Determine index size for packages that build only for one index size (default is 32). Packages that handle all index sizes
automatically are free to ignore this option.

    1. `--with-index-size=[32,64]`

    2. `XSDK_INDEX_SIZE=[32,64]`

----

9. Set location of BLAS and LAPACK libraries (default is to locate one on the system automatically). 

    1. `--with-blas-lib="linkable list of libraries” --with-lapack-lib=”linkable list of libraries”` -- it is fine to use
    -L and -l flags in the lists

    2. `TPL_BLAS_LIBRARIES="linkable list of libraries”`, `TPL_LAPACK_LIBRARIES=”linkable list of libraries”` -- should not use
    -L or -l flags in the lists

----

10. Determine other package libraries and include directories.

    1. `--with-<package> --with-<package>-lib="linkable list of libraries” --with-<package>-include=”list of include directories”`
    2. `TPL_ENABLE_<package>=[YES,NO]`

Packages must provide a way for a user to specify a dependent package to use. Packages are free to locate a package on the file system if none is specifically provided by the user. If the user does provide one, however, it must be used; if it is not able to be used, then an error must be generated. A package cannot silently substitute a different installation.

----


11. In the XSDK mode, XSDK projects should not rely on users providing any library path information in environmental 
variables such as `LD_LIBRARY_PATH`.  

----

12. After packages are configured, they can be compiled, installed and "smoke" tested with the following commands: `make ; 
[sudo] make install ; make test_install`. 

----

13. After an install the package should provide a machine-readable output to show provenance, that is, what compilers were 
used and what libraries were linked with, as well as other build configuration information, so that users with problems can send the information directly to developers.
