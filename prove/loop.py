from sklearn.datasets import load_boston
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.tree import DecisionTreeRegressor
import m2cgen as m2c

X, y = load_boston(return_X_y=True)
est = DecisionTreeRegressor().fit(X, y)

assemble = m2c.assemblers.TreeModelAssembler(est).assemble()

class CustomJavaInterpreter(m2c.interpreters.JavaInterpreter):
    pass

interpreter = CustomJavaInterpreter()
for ast_size_threshold in range(4600, 3000, -500):
    interpreter.ast_size_per_subroutine_threshold = ast_size_threshold
    code = interpreter.interpret(assemble)
    with open('test1_{}.java'.format(ast_size_threshold), 'w') as f:
        f.write(code)
