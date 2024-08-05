
class Solution:
    def bottomView(self, root):
        # code here
        m = {}
        def walk(n, level=0, pos=0):
            if not n:
                return
            walk(n.left, level+1, pos-1)
            if pos not in m or m[pos][1] <= level:
                m[pos] = (n.data, level)
            walk(n.right, level+1, pos+1)

        walk(root)
        return [m[k][0] for k in sorted(m)]