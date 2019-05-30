## Discussion and Examples

For configure we are trying to match as closely as possible the GNU autoconf and CMake standards and conventions. 

1. `--prefix=/usr/local/; cmake -DCMAKE_INSTALL_PREFIX=/usr/local`

2. `CC=/usr/local/bin/mpicc ./configure`

    * The reason to support environmental variables is that Linux package managers use environmental variables to set the compiler options, not command line arguments. 

    * When reading environmental variables, the configure output should clearly show which variables are being used.

3. `./configure CC=/usr/bin/mpicc; cmake -DCMAKE_C_COMPILER=/usr/bin/mpicc -DCMAKE_CXX_FLAGS="-O3 -Wall”`

    * With CMake projects, compiler flags are passed to the compiler as follows:
    `${CMAKE_<LANG>_COMPILER>  ${CMAKE_<LANG>_FLAGS} ${CMAKE_<LANG>_FLAGS_<CMAKE_BUILD_TYPE>}`
     Therefore, `CMAKE_<LANG>_FLAGS` never overrides the build type (e.g., `DEBUG`, `RELEASE`) specific compiler flags.  

4. `./configure --disable-debug; cmake -DCMAKE_BUILD_TYPE=RELEASE `

    * `Debug` is the default because it helps users while developing (writing) their code, which is most of the time.

    * The optimized/release version may or may not contain debug symbols. Although the consensus is that including debug 
    symbols is a good idea for deeply templated C++ libraries, the object size can become very large. Therefore, we do not 
    require such symbols.

5. `./configure --disable-shared; cmake -DBUILD_SHARED_LIBS=FALSE `

    * Shared is the default because linking against the libraries is dramatically faster.

6. `./configure --disable-cxx --enable-fc ; cmake -DXSDK_ENABLE_CXX=FALSE `

    * The default is to have C and C++ enabled and Fortran disabled. Packages that do not use Fortran (or C++) are free to 
    ignore that flag.

7. `./configure --with-precision=single`

    * If a package automatically supports multiple versions, it can ignore this option.

8. `./configure --with-index-size=64`

    * If a package automatically supports multiple versions, it can ignore this option.

9. `./configure --with-lapack-lib="-llapack -lblas”`

    * Packages are free to locate a BLAS/LAPACK installation on the file system if none is specifically provided by the user. 
    If the user does provide one, however, it **must** be used; if it is not able to be used, then an error must be 
    generated. A package cannot silently substitute a different installation.

10.  `./configure --with-x --with-metis-lib=/usr/local/lib/libmetis.a --with-metis-include=/usr/local/include`

     * In CMake, the analogous approach would be `cmake -DTPL_ENABLE_METIS=ON -DTPL_METIS_INCLUDE_DIRS=/usr/local/include -DTPL_METIS_LIBRARIES=/usr/local/lib/libmetis.a`. However, a package may use CMake's `find_package()` command to load a dependent library as long as the package provides a way for a user to specify an installation of the dependent library to use, *and* the package guarantees that the specified installation is not substituted.
    
     * Packages are free to locate a package on the file system if none is specifically provided by the user. If the user does provide one, however, it **must** be used; if it is not able to be used, then an error must be generated. A package 
cannot silently substitute a different installation.
    
     * There does not exist any CMake standard allowing an external user to set what external package dependencies should be enabled or disabled when configuring. Therefore, this is a TriBITS/Trilinos standard is which calls external packages "TPL"s and therefore the name `TPL_ENABLE_<package>`.

     * MPI is never considered a `<package>`, and xSDK packages do not need to support `--with-mpi-lib` and `--with-mpi-include`. In fact, we recommend against it. 
    
11. In order for linking of applications with a multitude of libraries without users needing to set LD_LIBRARY_PATH, 
each package likely needs to manage how it handles the rpath linker options when building its libraries.

    * Packages are also free to have configure modes that require setting LD_LIBRARY_PATH.

12. Note that the `make test_install` is run **after** the `make install` and utilizes the **installed** versions of of the 
library.  This type of test is often called a *smoke test*, as it verifies that at least something can be built and run using
the installed library. It can consist of one or several distinct tests but should not require parallelism nor take more than 
a couple of minutes.

13. This information is useful for debugging; it can, for example, be emailed to the package developer when problems arise.

    * The "pkgconfig" format and the “module” are two examples of such representations. Both are unfortunately neither 
    complete nor fully standard.  

    * We may want to develop an extension of the pkgconfig standard
