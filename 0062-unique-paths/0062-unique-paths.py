class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
    Computes the number of unique paths in an m x n grid using combinatorics.

    The robot moves exactly (m-1) steps down and (n-1) steps right.
    The total number of moves required is (m-1) + (n-1) = (m + n - 2).
    Out of these (m + n - 2) moves, we must choose (m-1) moves to be downward.
    
    The number of ways to choose (m-1) downward moves from (m + n - 2) total moves 
    is given by the combination formula:
    
        C(total_moves, down_moves) = (total_moves)! / (down_moves)! (right_moves)!
                                   = (m + n - 2)! / ((m-1)! * (n-1)!)

    This formula calculates the number of ways to arrange (m-1) downs and (n-1) rights
    in a sequence of (m+n-2) moves.
    """
        return math.comb(m + n - 2, m - 1)
        