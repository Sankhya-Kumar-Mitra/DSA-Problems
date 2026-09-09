/*
Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        Map<Node,Node> visited = new HashMap<Node,Node>();
        
        return dfs(node,visited);
    }

    public Node dfs(Node node, Map<Node,Node> visited){

        if (node == null){
            return null;
        }

        if (visited.containsKey(node)){
            return visited.get(node);
        }

        Node copy = new Node(node.val);
        visited.put(node,copy);

        for (Node nei : node.neighbors){
            copy.neighbors.add(dfs(nei,visited));
        }

        return copy;

    }
}