# Project Description

Split large [m2cgen](https://github.com/BayesWitnesses/m2cgen) java trees into subroutines  and: 
    * avoid Java's 64KB function size mempty error 
    * avoid Java's class too many constants error.

ATTENTION: provide m2cgen (rigid structure!) java code as input.

# Project Structure

* `src`: source code of the project

* `prove`: code to shows that currently, `m2cgen` param tuning heuristics don't work - all of the generated files have the same number of the subroutines (it isn't affected by the param fine-tuning)

* `test`: 
    
    * `model_small`: small model to test the coded approach

    * `model_large`: PRIVATE

* `integr-rflction`: PRIVATE

* `integr-pipeline`: PRIVATE