class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ""
        list1 = []
        for i in digits:
            s += str(i)
        s = int(s)
        s = s+1
        s = str(s)
        for z in s:
            list1.append(int(z))
        return(list1)
