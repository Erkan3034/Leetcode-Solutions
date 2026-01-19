class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or ( x % 10 == 0 and x != 0 ): # negatif , ve sonu sıfır olan sayılar palindrom olamaz.
            return False
        
        reversed_half = 0  #sayıyı yarıya kadar bölüyoruz

        while x > reversed_half: 
            reversed_half = reversed_half * 10 + x % 10

            x //= 10

        return x == reversed_half or x == reversed_half // 10