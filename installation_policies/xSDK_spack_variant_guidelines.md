# xSDK Spack Variant Guidelines

Common Spack [variants](https://spack.readthedocs.io/en/latest/basic_usage.html#variants) help users to build a consistent and compatible software stack, and offers the potential to support global or xsdk-scoped variants and automation.

For example, if a user wished to build the software stack in "debug" mode, potentially a global Spack variant could be applied.

This document outlines a list of features that must be exposed as Spack variants, when alternative options  for these features are available. If the package does not have options for these features, then a Spack variant is not required.

The exact variants names and types (e.g. boolean or multi-value) used are currently given as recommendations. If the recommended variants are inadequate to express a packages options,  then this feedback should be provided to the xSDK team so that these guidelines can be improved.

This document may be updated over time, and so should be checked before each xSDK release.

The proposed recommendations for Spack variants given below are based on a review first carried out on August 18th 2020 The reviewing of Spack variants is open-ended. It is documented in the following location: https://github.com/xsdk-project/xsdk-community-policies/wiki/Spack-variant-review.

The following options MUST be exposed through Spack, where alternative options for the given feature are supported in the configuration stage.

---

**1. Index size**

This option concerns index sizes (or compile-time determined integer sizes).

We recommend using the boolean `int64` variant name to set index sizes to 64-bits. It is expected that `~int64` will result in 32-bit integer size.

`int64`: Index sizes (or compile-time determined integer sizes) are set to 64 bits.

When different options are required, an alternative variant (either boolean or multi-valued) may be used. Please refer to the [Spack variant review](https://github.com/xsdk-project/xsdk-community-policies/wiki/Spack-variant-review) for guidance.

---

**2. Precision**

This concerns the size of compile-time configured floating-point variables.

We recommend using multi-valued variant `precision`.

`precision`: The multi-valued variant `precision` can accept multiple precision descriptions. The names `single` and `double` are recommended for 32-bit/64-bit respectively. Other options may include `half` for 16-bit, `extended` for 80-bit or `quad` for 128-bit.

---

**3. Shared/Static libraries**

These options determine how libraries are built.

**_Note_**
There has been discussion about adopting a multi-value variant for this purpose, which may better cover the possible permutations. However, the following recommendations have been determined based on a review of current usage. It is possible this will change in the future.

We recommend using one or more of following boolean variants which have been adopted widely in Spack:

`shared`: A boolean variant. If True, then shared libraries will be built.
`static`: A boolean variant. If True, then static libraries will be built.
`pic`: A boolean variant. If True, then produce position independent code.

The meaning and combination of these values is expected to follow conventions given below (based on cmake):

If `shared` is the only option present, then enabling this option is expected to build shared libraries *instead* of static, and these will be built using _pic_ (position independent code). If False, then static libraries will be built without pic.

If the user wishes to build both static and shared libraries, then use both `static` and `shared` variants and set both to True.

If the user wishes to build shared libraries but without _pic_, then use `shared` and `pic`, and set `pic` to False.

Permutations of package variants that are unsupported or infeasible should be denoted in a `conflict` statement. E.g. `conflicts('~static~shared')`

---

**4. Debug/build_type**

These options specify flags to do with debugging symbols and optimization.

We recommend using the multi-valued variant `build_type`

`build_type`: A multi-value variant which must include at least `Debug` and `Release` options. Other options, mirroring their Cmake counterparts, may include `RelWithDebInfo` and and `MinSizeRel`. A brief description of these options is given below.

- `Release`: Fully optimized version for code release.
- `Debug`: Debugging symbols should be produced and optimization disabled. Further useful debugging information and additional error checking maybe included.
- `RelWithDebInfo` Contains debugging symbols without disabling optimization
- `MinSizeRel` Configures optimization for a smaller size release.

The `multi` argument to the `variant` function (used to declare variants) should be set to False. This means only one option can be enabled.

User's may add further options, if the above are inadequate.
