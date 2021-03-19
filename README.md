# Project Description

Split large [m2cgen](https://github.com/BayesWitnesses/m2cgen) java trees into subfunctions and avoid Java's 64KB function size limit error and too many constants error.

ATTENTION: provide m2cgen (rigid structure!) java code as input.

# Project Structure

* `src`: source code of the project

* `prove`: code to shows that m2cgen param tuning not working right now - all of the generated files have the same number of the subroutines (it isn't affeceted by the param tuning)

* `test`: 
    
    * `model_small`: small model to test the coded approach

    * `model_large`: PRIVATE

* `reflection`: PRIVATE