/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    int maxDepth = 0;
    public int maxDepth(TreeNode root) {
        
        if (root == null){
            return 0;
        }
        return dfs(root,1);
    }

    public int dfs(TreeNode node, int length){
        if (node == null){
            return length-1;
        }

        return  Math.max(dfs(node.left,length+1),dfs(node.right,length+1));

    }
}
