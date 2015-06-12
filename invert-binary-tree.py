# -*- coding: utf-8 -*-

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root is not None:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        q = [root]
        while q:
            node = q.pop()
            if node:
                node.left, node.right = node.right, node.left
                q.extend([node.left, node.right])
        return root
