/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/**
 * @param {TreeNode} root
 * @return {number}
 */
 var maxDepth = function(root) {
    const queue = [root];
    let depth = 0;
    
    if (root === null) {
        return 0;
    }
    
    while (queue.length) {
        depth++;
        const nodeCount = queue.length;
        
        for (i = 0; i < nodeCount; i++) {
            currNode = queue[0];
            
            if (currNode?.left) {
                queue.push(currNode.left);
            }
            if (currNode?.right) {
                queue.push(currNode.right);
            }

            queue.shift();
        }
    }
    
    return depth;
};