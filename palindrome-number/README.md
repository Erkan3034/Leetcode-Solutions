# Palindrome Number

## 📝 Problem Açıklaması

Bir `x` tam sayısı verildiğinde, bu sayının bir palindrom olup olmadığını belirleyin. Bir tam sayı, soldan sağa ve sağdan sola okunduğunda aynı ise palindromdur.

**Örnekler:**

*   **Örnek 1:**
    *   **Giriş:** `x = 121`
    *   **Çıkış:** `true`
    *   **Açıklama:** 121, soldan sağa ve sağdan sola okunduğunda 121'dir.

*   **Örnek 2:**
    *   **Giriş:** `x = -121`
    *   **Çıkış:** `false`
    *   **Açıklama:** Soldan sağa -121 okunur. Sağdan sola okunduğunda 121- olur. Bu nedenle bir palindrom değildir.

*   **Örnek 3:**
    *   **Giriş:** `x = 10`
    *   **Çıkış:** `false`
    *   **Açıklama:** Sağdan sola 01 okunur. Bu nedenle bir palindrom değildir.

**Kısıtlamalar:**

*   `-2^31 <= x <= 2^31 - 1`

**Ek Soru:**

*   Tam sayıyı bir string'e dönüştürmeden çözebilir misiniz?

---

## 💡 Çözüm Yaklaşımı

Bu problem için temel yaklaşım, sayıyı bir string'e dönüştürmeden, sayının tersini oluşturarak veya sayının yarısını tersine çevirerek orijinal sayıyla karşılaştırmaktır. "Ek Soru" kısıtlaması göz önüne alındığında, string dönüşümünden kaçınmak gerekmektedir.

Seçilen yaklaşım, sayının yalnızca ikinci yarısını tersine çevirmek ve bu ters çevrilmiş yarıyı orijinal sayının kalan yarısı ile karşılaştırmaktır. Bu yöntem, tam sayının tamamını tersine çevirme riskini (taşma potansiyeli) ortadan kaldırır ve daha verimlidir.

**Temel Fikirler:**

1.  **Özel Durumların Ele Alınması:**
    *   Negatif sayılar hiçbir zaman palindrom olamaz. (Örn: -121)
    *   Sonu sıfır ile biten pozitif sayılar (0 hariç) hiçbir zaman palindrom olamaz. Çünkü ters çevrildiğinde başı sıfır ile başlayacaktır. (Örn: 10, tersi 01)
2.  **Sayıyı Ters Çevirme:** Sayının basamaklarını tek tek alıp yeni bir sayı oluşturarak tersini elde edebiliriz. Ancak, sayının tamamını ters çevirmek yerine, sadece yarısını ters çevirmek yeterlidir.
3.  **Karşılaştırma:** Sayının yarısı ters çevrildikten sonra, orijinal sayının kalan yarısı ile ters çevrilmiş yarı karşılaştırılır. Eğer sayının basamak sayısı tek ise, ters çevrilmiş yarının ortadaki basamağı atılarak karşılaştırma yapılır.

---

## ⚙️ Algoritma Adımları

1.  **Başlangıç Kontrolleri:**
    *   Eğer `x` negatifse (`x < 0`), `false` döndür. Negatif sayılar palindrom değildir.
    *   Eğer `x` sıfır değilse (`x != 0`) ve `x`'in son basamağı sıfır ise (`x % 10 == 0`), `false` döndür. Sonu sıfır ile biten sayılar (0 hariç) palindrom değildir. (Örn: 10, 120)
    *   Eğer `x` sıfır ise, `true` döndür. (0 bir palindromdur.)

2.  **Yarıyı Ters Çevirme:**
    *   `reversed_half` adında bir değişkeni `0` olarak başlat. Bu değişken, sayının ters çevrilmiş yarısını tutacaktır.
    *   Bir `while` döngüsü başlat: `x` değeri `reversed_half` değerinden büyük olduğu sürece döngü devam etsin. Bu koşul, sayının yarısını ters çevirdiğimizde döngüyü durdurmamızı sağlar.
        *   `reversed_half` değerini güncelle: `reversed_half = reversed_half * 10 + x % 10`. Bu adım, `x`'in son basamağını alır ve `reversed_half`'in sonuna ekler.
        *   `x` değerini güncelle: `x //= 10`. Bu adım, `x`'in son basamağını siler.

3.  **Son Karşılaştırma:**
    *   Döngü sona erdiğinde, `x` ya orijinal sayının ilk yarısı (veya ortadaki basamağı içeren ilk yarısı) ya da `reversed_half` ile aynı olacaktır.
    *   Eğer `x`'in basamak sayısı çift ise, `x` ve `reversed_half` tam olarak eşit olmalıdır (`x == reversed_half`).
    *   Eğer `x`'in basamak sayısı tek ise, `x`'in ortadaki basamağı `reversed_half`'in son basamağına denk gelir. Bu durumda, `reversed_half`'in son basamağını atarak (`reversed_half // 10`) `x` ile karşılaştırmalıyız (`x == reversed_half // 10`).
    *   Bu iki koşuldan herhangi biri doğruysa, `true` döndür; aksi takdirde `false` döndür.

---

## ⏱️ Karmaşıklık Analizi

*   **Zaman Karmaşıklığı: `O(log₁₀(x))`**
    *   Algoritma, `x` sayısının basamak sayısı kadar iterasyon yapar. Bir sayının basamak sayısı, o sayının 10 tabanına göre logaritmasıyla orantılıdır (`log₁₀(x)`). Her iterasyonda sabit zamanlı matematiksel işlemler yapılır. Dolayısıyla, zaman karmaşıklığı `O(log₁₀(x))`'tir.

*   **Uzay Karmaşıklığı: `O(1)`**
    *   Algoritma, `x` ve `reversed_half` gibi yalnızca birkaç sabit sayıda değişken kullanır. Bu değişkenlerin kapladığı alan, giriş `x`'in büyüklüğünden bağımsızdır. Bu nedenle, uzay karmaşıklığı sabittir, yani `O(1)`'dir.

---

## 💻 Kod Açıklaması

```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 1. Başlangıç Kontrolleri:
        # Negatif sayılar palindrom olamaz.
        # Sonu sıfır ile biten sayılar (0 hariç) palindrom olamaz. (Örn: 10 -> 01)
        if x < 0 or ( x % 10 == 0 and x != 0 ):
            return False
        
        reversed_half = 0  # Sayının ters çevrilmiş yarısını tutacak değişken

        # 2. Yarıyı Ters Çevirme Döngüsü:
        # x, reversed_half'ten büyük olduğu sürece döngü devam eder.
        # Bu, sayının yaklaşık yarısını ters çevirdiğimizde duracağımız anlamına gelir.
        while x > reversed_half: 
            # x'in son basamağını alıp reversed_half'in sonuna ekle.
            # Örn: x=121, reversed_half=0 -> reversed_half = 0*10 + 1 = 1
            # Örn: x=12, reversed_half=1 -> reversed_half = 1*10 + 2 = 12
            reversed_half = reversed_half * 10 + x % 10

            # x'in son basamağını sil.
            # Örn: x=121 -> x = 12
            # Örn: x=12 -> x = 1
            x //= 10

        # 3. Son Karşılaştırma:
        # Döngü bittiğinde iki durum olabilir:
        # a) x'in basamak sayısı çift ise (örn: 1221):
        #    x = 12, reversed_half = 12. Bu durumda x == reversed_half olmalı.
        # b) x'in basamak sayısı tek ise (örn: 121):
        #    x = 1, reversed_half = 12. Ortadaki basamak (1) x'te kalır,
        #    reversed_half'te ise ters çevrilmiş ilk yarı (2) ve ortadaki basamak (1) bulunur.
        #    Bu durumda reversed_half'in son basamağını (ortadaki basamağı) atarak karşılaştırma yapılır.
        #    x == reversed_half // 10 (1 == 12 // 10 -> 1 == 1)
        return x == reversed_half or x == reversed_half // 10

```

---

## 🧪 Örnek Test Case

**Giriş:** `x = 121`

**Beklenen Çıkış:** `true`

**Algoritma İzlemesi:**

1.  **Başlangıç Kontrolleri:**
    *   `x = 121`. `x < 0` yanlış.
    *   `x % 10 == 0` (121 % 10 = 1) yanlış.
    *   Kontrollerden geçer.

2.  **Yarıyı Ters Çevirme Döngüsü:**
    *   `reversed_half = 0`
    *   **İterasyon 1:**
        *   `x = 121`, `reversed_half = 0`. `x > reversed_half` (121 > 0) doğru.
        *   `reversed_half = 0 * 10 + 121 % 10 = 0 + 1 = 1`
        *   `x = 121 // 10 = 12`
    *   **İterasyon 2:**
        *   `x = 12`, `reversed_half = 1`. `x > reversed_half` (12 > 1) doğru.
        *   `reversed_half = 1 * 10 + 12 % 10 = 10 + 2 = 12`
        *   `x = 12 // 10 = 1`
    *   **İterasyon 3:**
        *   `x = 1`, `reversed_half = 12`. `x > reversed_half` (1 > 12) yanlış.
        *   Döngü sona erer.

3.  **Son Karşılaştırma:**
    *   `x = 1`, `reversed_half = 12`
    *   `x == reversed_half` (1 == 12) yanlış.
    *   `x == reversed_half // 10` (1 == 12 // 10) -> (1 == 1) doğru.
    *   Fonksiyon `true` döndürür.

---

## 🔗 LeetCode Linki

[Palindrome Number - LeetCode](https://leetcode.com/problems/palindrome-number/)

## 💻 Programlama Dili

python

---

*Bu README dosyası Universal LeetCode GitHub Sync Tool tarafından otomatik olarak oluşturulmuştur.*