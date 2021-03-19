## Prepare .jar archive from '/test/model_large/'

# Print intro msg
echo 'Must run from the repo root folder!'
echo 'Current dir:'
pwd

# Generate DT
# ./test/model_large/dt-generator.sh
# unzip test/model_large/tree_mleaf10.zip
# file at test/model_large/tree_mleaf10/DecisionTreeModel.java

# Compile
python3 src/convert.py -model-path test/model_large/tree_mleaf10/DecisionTreeModel.java
cd test/model_large/tree_mleaf10/DecisionTreeModelSplitted
javac DecisionTreeModel0.java

# Archive
jar cf DecisionTree.jar *.class 

# Clear .class files
rm -rf *.class

# Print output .jar path
echo 'Output .jar archive contatining prepared model:'
realpath DecisionTree.jar




