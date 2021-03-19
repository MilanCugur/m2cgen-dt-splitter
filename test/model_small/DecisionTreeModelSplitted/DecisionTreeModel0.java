
public class DecisionTreeModel0 {
    public static double score(double[] input) {
        if ((input[8]) <= (-0.003761786)) {
            return DecisionTreeModel1.score(input);
        } else {
            return DecisionTreeModel6.score(input);
        }
    }
}
