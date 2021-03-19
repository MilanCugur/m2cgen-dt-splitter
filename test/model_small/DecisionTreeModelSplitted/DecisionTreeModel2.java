
public class DecisionTreeModel2 {
    public static double score(double[] input) {
        if ((input[6]) <= (0.021027816)) {
            return DecisionTreeModel3.score(input);
        } else {
            return DecisionTreeModel4.score(input);
        }
    }
}
