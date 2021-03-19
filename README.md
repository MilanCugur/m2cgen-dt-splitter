# Project Description

Split large [m2cgen](https://github.com/BayesWitnesses/m2cgen) `java trees` into subroutines  and: 

 * avoid Java's 64KB function size memory error 

 * avoid Java's class too many constants error

Can be used (with small modifications) to fix al of the [m2cgen issues](https://github.com/BayesWitnesses/m2cgen/issues):

 * [#298](https://github.com/BayesWitnesses/m2cgen/issues/298)

 * [#306](https://github.com/BayesWitnesses/m2cgen/pull/306)

 * [#297](https://github.com/BayesWitnesses/m2cgen/issues/297)

 * [#103](https://github.com/BayesWitnesses/m2cgen/issues/103)

ATTENTION: provide `m2cgen` (rigid structure!) java tree code as input.

# Project Structure

* `src`: source code of the project

* `prove`: code to shows that currently, `m2cgen` param tuning heuristics don't work - all of the generated files have the same number of the subroutines (it isn't affected by the param fine-tuning)

* `test`: 
    
    * `model_small`: small model to test the coded approach

    * `model_large`: PRIVATE

* `integr-rflction`: PRIVATE

* `integr-pipeline`: PRIVATE