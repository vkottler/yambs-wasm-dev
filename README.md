<!--
    =====================================
    generator=datazen
    version=3.1.4
    hash=cdc6f30afd6b54d52bc4ad333f91ab6e
    =====================================
-->

# yambs-wasm-dev ([0.1.0](https://github.com/vkottler/yambs-wasm-dev/releases/tag/0.1.0))

[![codecov](https://codecov.io/gh/vkottler/yambs-wasm-dev/branch/master/graph/badge.svg)](https://codecov.io/gh/vkottler/yambs-wasm-dev)
![Build Status](https://github.com/vkottler/yambs-wasm-dev/actions/workflows/yambs-project.yml/badge.svg)

*Short project description.*

## Documentation

### Generated

* By [sphinx+breathe+exhale](https://vkottler.github.io/cpp/sphinx/yambs-wasm-dev/)
(What's [sphinx](https://www.sphinx-doc.org/en/master/) /
[breathe](https://breathe.readthedocs.io/en/latest/) /
[exhale](https://exhale.readthedocs.io/en/latest/)?)

## Workflow

Install [vmklib](https://github.com/vkottler/vmklib) such that you can
`mk --version` (a `pip install vmklib` to your desired Python environment is
all that's needed).

From a fresh checkout:

```
git submodule update --init
mk dz-sync
mk g
```

This should result in fully compiled code that you can now use or add to.


### Generating Interfaces

Structs and enumerations can be defined for
[ifgen](https://github.com/vkottler/ifgen) which can then generate C++ source
code into the project.

Generating configurations based on an
[SVD](https://github.com/vkottler/ifgen/tree/master/ifgen/data/svd) file:

```
mk ifgen-svd-XMC4700
```

Generating code from an `ifgen.yaml` in the root directory of the project:

```
mk ifgen
```
