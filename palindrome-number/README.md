# Palindrome Number

Harika! Bir yazılım mühendisi ve algoritma uzmanı olarak, "Palindrome Number" problemi için profesyonel bir `README.md` dosyası hazırlayalım.

---

# Palindrome Number

## 📝 Problem Açıklaması

Bir `x` tam sayısı verildiğinde, bu sayının bir palindrom olup olmadığını kontrol eden bir fonksiyon yazmanız istenmektedir. Bir sayı, soldan sağa ve sağdan sola okunduğunda aynı ise palindromdur.

**Örnekler:**

*   **Örnek 1:**
    *   **Giriş:** `x = 121`
    *   **Çıkış:** `true`
    *   **Açıklama:** 121, soldan sağa ve sağdan sola okunduğunda 121'dir.
*   **Örnek 2:**
    *   **Giriş:** `x = -121`
    *   **Çıkış:** `false`
    *   **Açıklama:** Soldan sağa -121 okunur. Sağdan sola ise 121- olur. Bu nedenle bir palindrom değildir.
*   **Örnek 3:**
    *   **Giriş:** `x = 10`
    *   **Çıkış:** `false`
    *   **Açıklama:** Sağdan sola 01 olarak okunur. Bu nedenle bir palindrom değildir.

**Kısıtlamalar:**

*   `-2^31 <= x <= 2^31 - 1`

**Ek Soru:**
Tam sayıyı bir string'e dönüştürmeden çözebilir misiniz?

## 💡 Çözüm Yaklaşımı

Bu problem için en verimli ve ek soruyu karşılayan yaklaşım, sayıyı bir string'e dönüştürmeden, sayının yalnızca yarısını tersine çevirerek orijinal sayının diğer yarısı ile karşılaştırmaktır.

**Neden bu yaklaşım?**

1.  **String Dönüşümünden Kaçınma:** Problemdeki ek soruya uygun olarak, sayıyı string'e dönüştürmek yerine matematiksel işlemlerle çözüme ulaşılır. Bu, potansiyel olarak daha az bellek kullanımı ve daha hızlı işlem anlamına gelebilir (özellikle çok büyük sayılar için, string dönüşümünün kendi maliyetleri vardır).
2.  **Tam Ters Çevirmeden Kaçınma:** Sayının tamamını tersine çevirmek, özellikle çok büyük sayılar için taşma (overflow) sorunlarına yol açabilir. Sayının sadece yarısını tersine çevirerek bu risk azaltılır ve işlem sayısı yarıya indirilir.
3.  **Kenar Durumların Ele Alınması:** Negatif sayılar ve sonu sıfır ile biten pozitif sayılar (0 hariç) özel durumlar olarak ele alınır, çünkü bunlar asla palindrom olamazlar.

## ⚙️ Algoritma Adımları

1.  **Kenar Durum Kontrolü:**
    *   Eğer `x` negatif ise, `false` döndür. (Negatif sayılar palindrom değildir.)
    *   Eğer `x` sıfır değilken `x`'in son basamağı sıfır ise (yani `x % 10 == 0` ve `x != 0`), `false` döndür. (Örn: 10, 200 gibi sayılar palindrom değildir, çünkü tersleri 01, 002 gibi olur. Ancak 0 sayısı bir palindromdur ve bu kurala takılmamalıdır.)

2.  **Sayıyı Yarıya Kadar Ters Çevirme:**
    *   `reversed_half` adında bir değişkeni `0` olarak başlat. Bu değişken, `x`'in ters çevrilmiş yarısını tutacaktır.
    *   `x` değişkeni `reversed_half`'tan büyük olduğu sürece bir döngü çalıştır:
        *   `reversed_half`'ı güncelle: `reversed_half = reversed_half * 10 + x % 10`. Bu adım, `x`'in en sağdaki basamağını alır ve `reversed_half`'ın en sağına ekler.
        *   `x`'i güncelle: `x //= 10`. Bu adım, `x`'in en sağdaki basamağını kaldırır.
    *   Döngü, `x` orijinal sayının ilk yarısını temsil ederken, `reversed_half` ikinci yarısının tersini temsil edene kadar devam eder.

3.  **Karşılaştırma ve Sonuç:**
    *   Döngü bittiğinde, iki durum oluşabilir:
        *   **Çift basamaklı sayılar:** `x` ve `reversed_half` birbirine eşit olmalıdır (örn: `1221` -> `x=12`, `reversed_half=12`).
        *   **Tek basamaklı sayılar:** `x`, `reversed_half`'ın son basamağı atıldığında (yani `reversed_half // 10`) eşit olmalıdır (örn: `121` -> `x=1`, `reversed_half=12` döngü bittiğinde. `x`'in `reversed_half // 10`'a eşit olup olmadığını kontrol ederiz: `1 == 12 // 10` -> `1 == 1`).
    *   Bu iki durumu kapsayan bir kontrol ile `x == reversed_half` veya `x == reversed_half // 10` ifadesinin sonucunu döndür.

## ⏱️ Karmaşıklık Analizi

*   **Zaman Karmaşıklığı: O(log₁₀ N)**
    *   Algoritma, `x` sayısını her adımda 10'a bölerek basamak sayısını azaltır. Bu nedenle, döngü `x`'in basamak sayısı kadar çalışır. Bir sayının basamak sayısı logaritmik olarak artar (log₁₀ N). Dolayısıyla, zaman karmaşıklığı O(log₁₀ N)'dir.
*   **Uzay Karmaşıklığı: O(1)**
    *   Algoritma, `x` ve `reversed_half` gibi sabit sayıda değişken kullanır. Kullanılan ek bellek miktarı, giriş `x`'in boyutundan bağımsızdır. Bu nedenle, uzay karmaşıklığı O(1)'dir.

## 💻 Kod Açıklaması

```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 1. Kenar Durum Kontrolü:
        # Negatif sayılar palindrom olamaz.
        # Sonu sıfır ile biten pozitif sayılar (örn: 10, 200) palindrom olamaz,
        # çünkü tersleri 01, 002 gibi olur. Ancak 0 sayısı bir palindromdur,
        # bu yüzden 'x != 0' kontrolü eklenmiştir.
        if x < 0 or ( x % 10 == 0 and x != 0 ):
            return False
        
        reversed_half = 0  # Sayının ters çevrilmiş yarısını tutacak değişken

        # 2. Sayıyı Yarıya Kadar Ters Çevirme Döngüsü:
        # x, reversed_half'tan büyük olduğu sürece döngü devam eder.
        # Bu, x'in basamak sayısı tek ise x'in ortadaki basamağına ulaşana kadar,
        # çift ise x'in ilk yarısı reversed_half'ın tersine eşit olana kadar sürer.
        while x > reversed_half: 
            # x'in en sağdaki basamağını alıp reversed_half'ın sonuna ekle
            reversed_half = reversed_half * 10 + x % 10
            # x'in en sağdaki basamağını kaldır
            x //= 10

        # 3. Karşılaştırma ve Sonuç:
        # Döngü bittiğinde, x ya reversed_half'a eşit olmalı (çift basamaklı sayılar için)
        # ya da reversed_half'ın son basamağı atıldığında x'e eşit olmalı (tek basamaklı sayılar için).
        # Örn: 121 -> x=1, reversed_half=12. Burada x == reversed_half // 10 (1 == 12 // 10 -> 1 == 1)
        # Örn: 1221 -> x=12, reversed_half=12. Burada x == reversed_half (12 == 12)
        return x == reversed_half or x == reversed_half // 10

```

## 🧪 Örnek Test Case

**Giriş:**
`x = 121`

**Çalışma Adımları:**

1.  `x = 121`. `x < 0` değil. `x % 10 == 0` değil. Kenar durum kontrolünden geçer.
2.  `reversed_half = 0`.
3.  **Döngü 1:**
    *   `x (121) > reversed_half (0)` doğru.
    *   `reversed_half = 0 * 10 + 121 % 10 = 1`.
    *   `x = 121 // 10 = 12`.
4.  **Döngü 2:**
    *   `x (12) > reversed_half (1)` doğru.
    *   `reversed_half = 1 * 10 + 12 % 10 = 10 + 2 = 12`.
    *   `x = 12 // 10 = 1`.
5.  **Döngü 3:**
    *   `x (1) > reversed_half (12)` yanlış. Döngü sonlanır.
6.  **Sonuç:**
    *   `x (1) == reversed_half (12)` yanlış.
    *   `x (1) == reversed_half // 10 (12 // 10 = 1)` doğru.
    *   `true` döndürülür.

**Çıkış:**
`true`

## 🔗 LeetCode Linki

Bu problemin orijinaline aşağıdaki bağlantıdan ulaşabilirsiniz:
[https://leetcode.com/problems/palindrome-number/](https://leetcode.com/problems/palindrome-number/)

## 💻 Programlama Dili

python

---

*Bu README dosyası Universal LeetCode GitHub Sync Tool tarafından otomatik olarak oluşturulmuştur.*