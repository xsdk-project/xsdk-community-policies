In the future this will be where the xSDK policies are kept.

# xSDK Community Package Policies

The IDEAS Project xSDK Team

Version 0.4.0, July 27, 2018

[https://xsdk.info/policies](https://xsdk.info/policies)

## Background

A key aspect of work in the [IDEAS Scientific Software Productivity Project][1] is developing an Extreme-scale
Scientific Software Development Kit ([xSDK][2]) — a collection of related and complementary software elements
that provide the building blocks, tools, models, processes, and related artifacts for rapid and efficient
development of high-quality applications. As an initial step in creating the xSDK, we have written the
following draft xSDK package community policies to help address challenges in interoperability and
sustainability of software developed by diverse groups at different institutions.

## Goal

Develop a set of **xSDK community policies** that a software library/framework (henceforth
referred to as package)<sup>1</sup> must satisfy in order to to be **xSDK compatible** . The designation of a
package being xSDK compatible informs potential users that the package can be easily used with
other xSDK libraries and components and thus helps to address issues in long-term sustainability<sup>2</sup>
and interoperability among packages.

We consider two categories of xSDK packages: **xSDK compatible** packages and **xSDK member**
packages. We also consider two levels of xSDK compatibility: **mandatory policies** and
**recommended policies**.

+ A package will be declared **xSDK compatible** once the xSDK team has determined that the
**package satisfies the mandatory xSDK policies** listed below. In addition to the required
policies, we specify **recommended xSDK policies** that further help to address issues in
software interoperability.

+ Similarly, a package can become an **xSDK member package** if (1) it is an xSDK-compatible
package, *and* (2) it uses or can be used by another package in the xSDK, and the connecting
interface is regularly tested for regressions.

Initially the requirements and process are informally presented; over time, if needed, we can begin to
formalize them. Currently the xSDK includes seven popular numerical libraries ([hypre][3] , [MAGMA][4] ,
[MFEM][5] , [PETSc/TAO][6] , [SUNDIALS][7] , [SuperLU][8] , and [Trilinos][9]) and two application
packages ([Alquimia][10] and [PFLOTRAN][11]), which satisfy the required policies. Over the longer term,
the xSDK may expand to incorporate additional packages, depending on community needs and contributions.

## xSDK Mandatory Policies

**M1.** [Support xSDK community GNU Autoconf or CMake options.](./M1.md)

**M2.** Provide a comprehensive test suite for correctness of installation verification.

**M3.** Employ user-provided MPI communicator (no MPI_COMM_WORLD). Don't assume a full MPI 2 or MPI 3
implementation without checking. Provide an option to prevent any changes to MPI error-handling if it is
changed by default.

**M4.** Give best effort at portability to key architectures (standard Linux distributions, GNU, Clang,
vendor compilers, and target machines at ALCF, NERSC, OLCF).

**M5.** Provide a documented, reliable way to contact the development team.

**M6.** Respect system resources and settings made by other previously called packages (e.g. signal handling).

**M7.** Come with an open source (BSD style) license.

**M8.** Provide a runtime API to return the current version number of the software.

**M9.** Use a limited and well-defined symbol, macro, library, and include file name space.

**M10.** Provide an xSDK team accessible repository (not necessarily publicly available).

**M11.** Have no hardwired print or IO statements that cannot be turned off.

**M12.** For external dependencies, allow installing, building, and linking against an outside copy of external software.

**M13.** Install headers and libraries under <prefix>/include and <prefix>/lib.
  
**M14.** Be buildable using 64 bit pointers. 32 bit is optional.

**M15.** All xSDK compatibility changes should be sustainable.

**M16.** The package must support production-quality installation compatible with the xSDK install tool
and xSDK metapackage.

## xSDK Recommended Policies

In addition to the required xSDK policies listed above, the following capabilities are also recommended.

**R1.** [Have a public repository](./R1.md).

**R2.** Possible to run test suite under valgrind in order to test for memory corruption issues.

**R3.** Adopt and document consistent system for error conditions/exceptions.

**R4.** Free all system resources acquired as soon as they are no longer needed.

**R5.** Provide a mechanism to export ordered list of library dependencies.

**R6.** Document versions of packages that it works with or depends upon, preferably in machine-readable form.

-----

<sup>1</sup> For the purpose of this document, the term *package* refers to a collection of source code
(possibly containing C, Fortran, or C++) that can generate zero or more shared or static libraries, zero
or more include files, zero or more Fortran modules, and possibly other auxiliary artifacts, including
executables, and whose functionality can be used by other packages and by application codes. A software
artifact that generates only an executable is, by this definition, not an xSDK package; that is, xSDK 
packages are libraries, frameworks, and domain components.

<sup>2</sup> See, for example, "Self-Sustaining Software" as outlined in
http://trac.trilinos.org/wiki/TribitsLifecycleModelOverview#self_sustaining_software.




[//]: # "Links go here"

[1]: http://www.ideas-productivity.org/
[2]: http://xsdk.info/
[3]: https://computation.llnl.gov/project/linear_solvers/
[4]: http://icl.utk.edu/magma
[5]: http://mfem.org/
[6]: http://www.mcs.anl.gov/petsc/
[7]: https://computation.llnl.gov/projects/sundials
[8]: http://crd-legacy.lbl.gov/~xiaoye/SuperLU/
[9]: https://trilinos.org/
[10]: https://bitbucket.org/berkeleylab/alquimia
[11]: http://www.pflotran.org/
