class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()      # karakterleri tutar
        left = 0          # pencerenin başlangıcı
        max_len = 0

        for right in range(len(s)):
            # eğer tekrar eden karakter varsa, soldan çıkar
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # yeni karakteri ekle
            seen.add(s[right])

            # maksimum uzunluğu güncelle
            max_len = max(max_len, right - left + 1)

        return max_len
 