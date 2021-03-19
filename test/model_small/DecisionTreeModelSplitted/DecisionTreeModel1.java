
public class DecisionTreeModel1 {
    public static double score(double[] input) {
        if ((input[2]) <= (0.006188885)) {
            return DecisionTreeModel2.score(input);
        } else {
            return DecisionTreeModel5.score(input);
        }
    }
}
