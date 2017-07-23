class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        mysqrt = x**(1/2.0)
        mysqrt = float(mysqrt)
        mysqrt = str(mysqrt)
        mysqrt = mysqrt.rstrip('0').rstrip('.')
        if float(mysqrt) % 1 == 0:
            return(int(mysqrt))
        else:
            return(int(math.floor(float(mysqrt))))
