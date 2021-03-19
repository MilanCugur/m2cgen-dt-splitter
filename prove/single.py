from sklearn.datasets import load_boston
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.tree import DecisionTreeRegressor
import m2cgen as m2c

X, y = load_boston(return_X_y=True)
est = DecisionTreeRegressor().fit(X, y)

# Not worling at all for single regressors!
interpreter = m2c.interpreters.JavaInterpreter()
interpreter.ast_size_check_frequency = 100
interpreter.ast_size_per_subroutine_threshold = 460
interpreter.subroutine_per_group_threshold = 10

print(interpreter.ast_size_per_subroutine_threshold, interpreter.ast_size_check_frequency, interpreter.subroutine_per_group_threshold, interpreter)

code = m2c.exporters._export(est, interpreter)
with open('code_{}_{}_{}.java'.format(interpreter.ast_size_per_subroutine_threshold, interpreter.ast_size_check_frequency, interpreter.subroutine_per_group_threshold), 'w') as f:
    f.write(code)
