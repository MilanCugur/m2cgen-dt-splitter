import os
import m2cgen as m2c
from sklearn.datasets import load_diabetes
from sklearn.tree import DecisionTreeRegressor

# Load data
X, y = load_diabetes(return_X_y=True)

# Create + Train ML model
tree = DecisionTreeRegressor()
tree.fit(X, y)

# Translate to .java code
code = m2c.export_to_java(tree, package_name=None, class_name="DecisionTreeModel", indent=4, function_name="score")

# Save .java code
out_path = os.path.join('test/model_small', 'DecisionTreeModel.java')
with open(out_path, 'w' ) as f:
    f.write(code)
