class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = "-"
        x = str(x)
        if x == "0":
            return(int(x))
        if x[0] == "-":
            x = x[1:]
            
            x = x[::-1]
            
            
            x = x.strip("0")
            
            if int(x) < 2147483647:
                x = negative + x
                return int(x)
            else:
                return 0
        else:
            x = x[::-1]
            x = x.strip("0")
            if int(x) < 2147483647:
                return int(x)
            else:
                return 0
        
