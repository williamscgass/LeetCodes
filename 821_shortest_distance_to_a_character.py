class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # keep left and right pointer of where the character is
        # initially, left and right are both -1.
        
        # we search for the next instance of the char, then we fill the values in.
        
        # so... adjust r till we find c, then in spaces between l and c, fill, then move l to r
        sol = [0] * len(s)
        
        l = float("-inf")
        mid = -1
        r = 0
        
        while r < len(s):
            if (s[r] == c):
                # move l up and fill
                while (mid < r):
                    mid += 1
                    sol[mid] = min(abs(mid - l), abs(mid-r))
                    
                l = r
                mid = r
                    
            r += 1
            
        # fill end
        while (mid < r - 1):
            mid += 1
            sol[mid] = abs(mid - l)
            
        return sol