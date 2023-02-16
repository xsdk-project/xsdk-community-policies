# <img src="/res/xsdk-logo.png" width="128">

We are actively soliciting suggestions from the community at https://xsdk.info/policies.

# xSDK Community Package Policies

The IDEAS Project xSDK Team

Version 0.6.0, October 12, 2020

[https://xsdk.info/policies](https://xsdk.info/policies)

## Background

A key aspect of work started in the [IDEAS Scientific Software Productivity Project][1] and continued in the [xSDK4ECP Project][2] is developing an Extreme-scale
Scientific Software Development Kit ([xSDK][3]) — a collection of related and complementary software elements
that provide the building blocks, tools, models, processes, and related artifacts for rapid and efficient
development of high-quality applications. As an initial step in creating xSDK, we have written the
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
package, *and* (2) it uses or can be used by another package in xSDK, and the connecting
interface is regularly tested for regressions.

Initially the requirements and process are informally presented; over time, if needed, we can begin to
formalize them. Currently, xSDK includes twenty-three popular numerical libraries:

1. [AMReX][14]
2. [ButterflyPACK][24]
3. [DTK][15]
4. [deal.II][16]
5. [Ginkgo][25]
6. [heFFTe][28]
7. [hypre][4]
8. [libEnsemble][26]
9. [MAGMA][5]
10. [MFEM][6]
11. [Omega_h][17]
12. [PETSc/TAO][7]
13. [PHIST][18]
14. [preCICE][27]
15. [PLASMA][19]
16. [PUMI][20]
17. [SLATE][29]
18. [SLEPc][21]
19. [STRUMPACK][22]
20. [SUNDIALS][8]
21. [SuperLU][9]
22. [Tasmanian][23]
23. [Trilinos][10]

and two applications packages:

1. [Alquimia][10]
2. [PFLOTRAN][12],

which satisfy the required policies. Over the longer term,
xSDK may expand to incorporate additional packages, depending on community needs and contributions.

## xSDK Mandatory Policies

**M1.** [Support portable installation through Spack.](/package_policies/M1.md)

**M2.** [Provide a comprehensive test suite for correctness of installation verification.](/package_policies/M2.md)

**M3.** [Employ user-provided MPI communicator (no MPI_COMM_WORLD). Don't assume a full MPI 3
implementation without checking. Provide an option to prevent any changes to MPI error-handling if it is
changed by default.](/package_policies/M3.md)

**M4.** [Give best effort at portability to key architectures (standard Linux distributions, GNU, Clang,
vendor compilers, and target machines at ALCF, NERSC, OLCF).](/package_policies/M4.md)

**M5.** [Provide a documented, reliable way to contact the development team.](/package_policies/M5.md)

**M6.** [Respect system resources and settings made by other previously called packages (e.g. signal handling).](/package_policies/M6.md)

**M7.** [Come with an open source (BSD style) license.](/package_policies/M7.md)

**M8.** [Provide a runtime API to return the current version number of the software.](/package_policies/M8.md)

**M9.** [Use a limited and well-defined symbol, macro, library, and include file name space.](/package_policies/M9.md)

**M10.** [Provide a publicly available repository.](/package_policies/M10.md)

**M11.** [Have no hardwired print or IO statements that cannot be turned off.](/package_policies/M11.md)

**M12.** [For external dependencies, allow installing, building, and linking with an outside copy of external software.](/package_policies/M12.md)

**M13.** [Install headers and libraries under `<prefix>/include` and `<prefix>/lib`.](/package_policies/M13.md)
  
**M14.** [Be buildable using 64 bit pointers. 32 bit is optional.](/package_policies/M14.md)

**M15.** [All xSDK compatibility changes should be sustainable.](/package_policies/M15.md)

**M16.** [Have a debug build option.](/package_policies/M16.md)

**M17.** [Provide sufficient documentation to support use and further development.](/package_policies/M17.md)

## xSDK Recommended Policies

In addition to the required xSDK policies listed above, the following capabilities are also recommended.

**R2.** [Possible to run test suite under Valgrind in order to test for memory corruption issues.](/package_policies/R2.md)

**R3.** [Adopt and document consistent system for error conditions/exceptions.](/package_policies/R3.md)

**R4.** [Free all system resources acquired as soon as they are no longer needed.](/package_policies/R4.md)

**R5.** [Provide a mechanism to export ordered list of library dependencies.](/package_policies/R5.md)

**R6.** [Document versions of packages that it works with or depends upon, preferably in machine-readable form.](/package_policies/R6.md)

**R7.** [Have README, SUPPORT, LICENSE, and CHANGELOG files in top directory.](/package_policies/R7.md)

**R8.** [Provide version comparision preprocessor macros.](/package_policies/R8.md)

**R1.** [At least one validation (smoke) test that can be invoked through the Spack package.](/package_policies/R1.md)

## History of the xSDK Community Policies

The original version of this document was prepared in 2015 by Barry Smith with key input from Roscoe Bartlett
and feedback from members of the IDEAS project. Over time, revisions have been introduced based on discussions
with the broader computational science community and developers of an expanding collection of xSDK member
packages. We thank all xSDK package developers, the IDEAS team, and the scientific computing community for
insightful discussion about issues and approaches.

+ Changes in version 0.6.0, October 12, 2020:
  + Added new policy R8 on documentation quality
  + Merged policies M1 and M16 with emphasis on use of Spack as xSDK installer 
  + Eliminated installation policies which were included in previous M1
  + Provided a document with xSDK Spack variant guidelines
  + Added new policy M16, which requires an xSDK package to have a configuration option that allows building in debug mode, 
a requirement previously included in the eliminated installation policies
+ Changes in version 0.5.0, June 27, 2019:
  + Added new policy R7, which recommends the inclusion of various information files in the top directory
  + Dropped the requirement to detect MPI 2 features in M3
  + Made various editorial changes in M5, M13, M15, and R2 for clarification or to fix typos. 
+ Changes in version 0.4.0, July 27, 2018:
  + Split policy M4 into 2 parts: M4 (portability to common platforms) and new policy R6
(package should document the versions of packages with which it can work on on which it depends). See
https://github.com/xsdk-project/xsdk-issues/issues/55
  + Revision to M7: language about open source licensing requirements. See
https://github.com/xsdk-project/xsdk-issues/issues/56
  + New section on history of policies and summary of changes, misc minor edits
+ Changes in version 0.3.0, November 6, 2017: added 2 new policies (M15 and M16), changed
naming convention to follow xSDK release number, minor typo edits
+ Changes in version 0.3, December 2, 2016: clear definition of xSDK member packages, misc
minor edits
+ Changes in version 0.2, January 28, 2016: minor edit
+ Version 0.1, November 10, 2015: original version

## Frequently Asked Questions about xSDK

See the [xSDK FAQ list][13].

## Acknowledgment

This material is based upon work supported by the U.S. Department of Energy, Office of Science, Advanced Scientific
Computing Research and Biological and Environmental Research programs.

-----

[//]: # "Main body footnotes"

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
[2]: http://xsdk.info/ecp/
[3]: http://xsdk.info/
[4]: https://computing.llnl.gov/projects/hypre-scalable-linear-solvers-multigrid-methods
[5]: http://icl.utk.edu/magma
[6]: http://mfem.org/
[7]: http://www.mcs.anl.gov/petsc/
[8]: https://computing.llnl.gov/projects/sundials
[9]: http://crd-legacy.lbl.gov/~xiaoye/SuperLU/
[10]: https://trilinos.org/
[11]: https://bitbucket.org/berkeleylab/alquimia
[12]: http://www.pflotran.org/
[13]: http://xsdk.info/faq/
[14]: https://amrex-codes.github.io/amrex/
[15]: https://github.com/ORNL-CEES/DataTransferKit
[16]: http://www.dealii.org/
[17]: https://github.com/ibaned/omega_h
[18]: https://bitbucket.org/essex/phist
[19]: http://icl.utk.edu/plasma/
[20]: https://github.com/SCOREC/core
[21]: http://slepc.upv.es/
[22]: https://portal.nersc.gov/project/sparse/strumpack/
[23]: https://tasmanian.ornl.gov/
[24]: https://github.com/liuyangzhuan/ButterflyPACK
[25]: https://github.com/ginkgo-project/ginkgo
[26]: https://github.com/Libensemble/libensemble
[27]: https://www.precice.org/
[28]: https://bitbucket.org/icl/heffte/src/master/
[29]: https://bitbucket.org/icl/slate/src/master/
