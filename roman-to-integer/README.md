# Roman to Integer

Harika! LeetCode'daki "Roman to Integer" problemi için profesyonel bir `README.md` dosyası oluşturalım.

---

# Roman to Integer

## Problem Açıklaması

Bu problemde, yedi farklı sembolle temsil edilen bir Roma rakamının karşılık gelen tam sayı değerine dönüştürülmesi istenmektedir. Roma rakamları ve değerleri aşağıdaki gibidir:

| Sembol | Değer |
| :----: | :---: |
|   I    |   1   |
|   V    |   5   |
|   X    |  10   |
|   L    |  50   |
|   C    |  100  |
|   D    |  500  |
|   M    | 1000  |

Roma rakamları genellikle en büyükten en küçüğe doğru soldan sağa yazılır ve değerleri toplanır (örn. `II = 2`, `XII = 12`, `XXVII = 27`). Ancak, altı özel durumda çıkarma kuralı uygulanır:

*   `I`, `V` (5) ve `X` (10) önüne gelerek 4 ve 9 yapar. (örn. `IV = 4`, `IX = 9`)
*   `X`, `L` (50) ve `C` (100) önüne gelerek 40 ve 90 yapar. (örn. `XL = 40`, `XC = 90`)
*   `C`, `D` (500) ve `M` (1000) önüne gelerek 400 ve 900 yapar. (örn. `CD = 400`, `CM = 900`)

Verilen bir Roma rakamı dizgesini (string) tam sayıya çevirmemiz gerekmektedir.

**Kısıtlamalar:**
*   `1 <= s.length <= 15`
*   `s` sadece `('I', 'V', 'X', 'L', 'C', 'D', 'M')` karakterlerini içerir.
*   `s`'in `[1, 3999]` aralığında geçerli bir Roma rakamı olduğu garanti edilmektedir.

## Çözüm Yaklaşımı

Bu problemi çözmek için, Roma rakamlarının değerlerini bir anahtar-değer çifti (dictionary/hash map) kullanarak saklayacağız. Temel yaklaşım, verilen Roma rakamı dizgesini soldan sağa doğru taramak ve her sembolün değerini toplamaya eklemektir. Ancak, çıkarma kuralının uygulandığı özel durumları ele almak için, mevcut sembolün değerini bir sonraki sembolün değeriyle karşılaştırmamız gerekmektedir.

Eğer mevcut sembolün değeri bir sonraki sembolün değerinden küçükse (örn. `IV`'deki `I` veya `CM`'deki `C`), bu bir çıkarma durumudur. Bu durumda, mevcut sembolün değeri toplamdan çıkarılır. Aksi takdirde (yani mevcut sembolün değeri bir sonraki sembolün değerinden büyük veya eşitse ya da dizgenin son sembolüyse), mevcut sembolün değeri toplama eklenir. Bu yöntem, hem standart toplama durumlarını hem de özel çıkarma durumlarını tek bir döngüde verimli bir şekilde ele almamızı sağlar.

## Algoritma Adımları

1.  Roma rakamı sembollerini ve karşılık gelen tam sayı değerlerini içeren bir sözlük (dictionary) oluşturulur.
    *   `'I': 1`, `'V': 5`, `'X': 10`, `'L': 50`, `'C': 100`, `'D': 500`, `'M': 1000`
2.  Dönüştürülen tam sayıyı tutacak `total` adında bir değişken `0` olarak başlatılır.
3.  Verilen Roma rakamı dizgesi `s` üzerinde `0`'dan başlayarak son karaktere kadar (dahil) bir döngü başlatılır.
4.  Her `i` indeksi için:
    a.  `i+1` indeksinin dizge sınırları içinde olup olmadığı ve mevcut sembol `s[i]`'nin değerinin bir sonraki sembol `s[i+1]`'in değerinden küçük olup olmadığı kontrol edilir.
    b.  Eğer bu koşul doğruysa (yani bir çıkarma durumu söz konusuysa, örn. `IV`, `IX`, `XL` vb.), `s[i]`'nin değeri `total`'dan çıkarılır.
    c.  Aksi takdirde (yani standart bir toplama durumu veya dizgenin son karakteriyse), `s[i]`'nin değeri `total`'a eklenir.
5.  Döngü tamamlandıktan sonra, `total` değişkeni Roma rakamının tam sayı karşılığını içerecektir. Bu değer döndürülür.

## Karmaşıklık Analizi

*   **Zaman Karmaşıklığı: `O(N)`**
    *   `N`, giriş dizgesi `s`'nin uzunluğudur.
    *   Algoritma, dizge üzerinde tek bir geçiş (iterasyon) yapar. Her adımda sözlük aramaları `O(1)` zaman alır.
    *   Bu nedenle, toplam zaman karmaşıklığı dizge uzunluğuyla doğru orantılıdır.
*   **Uzay Karmaşıklığı: `O(1)`**
    *   Kullanılan sözlük (dictionary) sabit sayıda (7 adet) Roma rakamı sembolü ve değerini saklar. Bu, giriş boyutundan bağımsız sabit bir bellek kullanımıdır.
    *   `total` değişkeni de sabit bellek kullanır.
    *   Bu nedenle, ek uzay karmaşıklığı sabittir.

## Kod Açıklaması

```python
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Roma rakamı sembollerini ve karşılık gelen tam sayı değerlerini içeren bir sözlük.
        # Bu sözlük, sembollerin değerlerine hızlı erişim sağlar.
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Dönüştürülen tam sayıyı tutacak toplam değişkeni.
        total = 0

        # Giriş dizgesi üzerinde soldan sağa doğru döngü.
        for i in range(len(s)):
             # Mevcut sembolün bir sonraki sembolle karşılaştırılması.
             # 1. `(i+1) < len(s)`: Bir sonraki sembolün var olup olmadığını kontrol eder.
             # 2. `roman[s[i]] < roman[s[i+1]]`: Mevcut sembolün değerinin bir sonraki sembolün değerinden küçük olup olmadığını kontrol eder.
             #    Bu koşul, IV, IX, XL, XC, CD, CM gibi çıkarma durumlarını tespit eder.
             if (i+1) < len(s) and roman[s[i]] < roman[s[i+1]]:
                # Eğer bir çıkarma durumuysa, mevcut sembolün değeri toplamdan çıkarılır.
                total -= roman[s[i]]
             else:
                # Aksi takdirde (toplama durumu veya dizgenin son sembolü),
                # mevcut sembolün değeri toplama eklenir.
                total += roman[s[i]]
        
        # Nihai toplam değeri döndürülür.
        return total
```

## Örnek Test Case

**Giriş:**
```
s = "MCMXCIV"
```

**Çıkış:**
```
1994
```

**Açıklama:**
1.  `M` (1000): `total = 1000`
2.  `C` (100) ve `M` (1000): `C < M` olduğu için `total -= 100` (`total = 900`)
3.  `X` (10) ve `C` (100): `X < C` olduğu için `total -= 10` (`total = 890`)
4.  `C` (100): `total += 100` (`total = 990`)
5.  `I` (1) ve `V` (5): `I < V` olduğu için `total -= 1` (`total = 989`)
6.  `V` (5): `total += 5` (`total = 994`)
7.  Döngü biter. `total` değeri `1994` olarak döndürülür.

## LeetCode Linki

[Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

---

## 💻 Programlama Dili

python

---

*Bu README dosyası Universal LeetCode GitHub Sync Tool tarafından otomatik olarak oluşturulmuştur.*