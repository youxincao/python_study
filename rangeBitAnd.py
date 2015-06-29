class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        ans = 0xFFFFFFFF
        while m <= n:
            ans &= m
            if ans == 0 :
                break
            m += 1
        return ans
