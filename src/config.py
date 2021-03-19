LEAF_TEMPLATE = \
"""
public class DecisionTreeModel{} {{
    public static double score(double[] input) {{
        double var0;
        {}
        return var0;
    }}
}}
"""

INNER_TEMPLATE = \
"""
public class DecisionTreeModel{} {{
    public static double score(double[] input) {{
        {}
            return DecisionTreeModel{}.score(input);
        {}
            return DecisionTreeModel{}.score(input);
        {}
    }}
}}
"""

LEAF_BORDER = 500

VERBOSE = 1