## Prepare .jar archive from '/test/model_small/'

# Print intro msg
echo 'Must run from the repo root folder!'
echo 'Current dir:'
pwd

# Generate DT
python3 test/model_small/dt-generator.py
ls -lt test/model_small/

# Compile
python3 src/convert.py -model-path test/model_small/DecisionTreeModel.java
cd test/model_small/DecisionTreeModelSplitted
javac DecisionTreeModel0.java
ls -lt 

# Archive
jar cf DecisionTree.jar *.class 

# Clear .class files
rm -rf *.class

# Print output .jar path
echo 'Output .jar archive contatining prepared model:'
realpath DecisionTree.jar




