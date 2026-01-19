# Palindrome Number

## 📝 Problem Açıklaması

Verilen bir `x` tam sayısının bir palindrom olup olmadığını belirleyin. Bir tam sayı, soldan sağa ve sağdan sola okunduğunda aynı ise palindromdur.

**Örnekler:**

*   **Örnek 1:**
    *   **Giriş:** `x = 121`
    *   **Çıkış:** `true`
    *   **Açıklama:** `121` soldan sağa ve sağdan sola okunduğunda `121`'dir.
*   **Örnek 2:**
    *   **Giriş:** `x = -121`
    *   **Çıkış:** `false`
    *   **Açıklama:** Soldan sağa `-121` okunur. Sağdan sola `121-` olur. Bu nedenle bir palindrom değildir.
*   **Örnek 3:**
    *   **Giriş:** `x = 10`
    *   **Çıkış:** `false`
    *   **Açıklama:** Sağdan sola `01` okunur. Bu nedenle bir palindrom değildir.

**Kısıtlamalar:**

*   `-2^31 <= x <= 2^31 - 1`

**Ek Soru:**

*   Tam sayıyı bir string'e dönüştürmeden çözebilir misiniz?

## 💡 Çözüm Yaklaşımı

Bu problem için temel yaklaşım, sayıyı bir string'e dönüştürmeden, yalnızca matematiksel işlemler kullanarak sayının yarısını tersine çevirmektir. Bu yöntem, hem zaman hem de uzay karmaşıklığı açısından oldukça verimlidir.

**Neden bu yaklaşım seçildi?**

1.  **String Dönüşümünden Kaçınma:** Problemdeki "Follow up" sorusuna doğrudan yanıt verir. String dönüşümü, özellikle çok büyük sayılar için ek bellek ve işlem maliyeti getirebilir.
2.  **Verimlilik:** Sayının sadece yarısını tersine çevirmek, tüm sayıyı tersine çevirmekten daha az işlem gerektirir ve sayının basamak sayısı kadar iterasyon yapar.
3.  **Kenar Durumların Ele Alınması:** Negatif sayılar ve sonu sıfır ile biten sayılar (sıfır hariç) gibi palindrom olamayacak özel durumlar başlangıçta hızlıca elenir.

## ⚙️ Algoritma Adımları

1.  **Kenar Durum Kontrolü:**
    *   Eğer `x` negatifse, `false` döndür. Negatif sayılar, öndeki eksi işareti nedeniyle asla palindrom olamaz.
    *   Eğer `x` sıfır değilse ve `x`'in son basamağı sıfır ise (`x % 10 == 0`), `false` döndür. Örneğin, `10`, `100` gibi sayılar tersine çevrildiğinde `01`, `001` olur ve orijinal sayıya eşit olmaz. Tek istisna `0` sayısıdır, o bir palindromdur.

2.  **Sayıyı Tersine Çevirme (Yarıya Kadar):**
    *   `reversed_half` adında bir değişkeni `0` olarak başlat. Bu değişken, `x`'in tersine çevrilmiş yarısını tutacaktır.
    *   `x`, `reversed_half`'ten büyük olduğu sürece bir döngü başlat. Bu koşul, sayının yaklaşık yarısını tersine çevirdiğimizde döngüyü durdurmamızı sağlar.
        *   `reversed_half`'i güncelle: `reversed_half = reversed_half * 10 + x % 10`. Bu adım, `x`'in son basamağını alır ve `reversed_half`'in sağına ekler.
        *   `x`'i güncelle: `x //= 10`. Bu adım, `x`'in son basamağını kaldırır.

3.  **Sonuç Kontrolü:**
    *   Döngü bittiğinde, `x` orijinal sayının ilk yarısını (veya tek basamaklı bir sayı ise ortadaki basamağı) temsil ederken, `reversed_half` sayının ikinci yarısının tersini temsil eder.
    *   İki olası durum vardır:
        *   **Çift sayıda basamak:** `x` ve `reversed_half` tam olarak eşit olmalıdır (örneğin, `x = 12`, `reversed_half = 12`).
        *   **Tek sayıda basamak:** `x`, `reversed_half`'in son basamağı atıldığında eşit olmalıdır (örneğin, `x = 1`, `reversed_half = 12` için `reversed_half // 10 = 1`). Bu durumda, ortadaki basamak her iki tarafta da aynı olduğu için önemsizdir ve `reversed_half`'ten çıkarılabilir.
    *   Bu nedenle, `x == reversed_half` veya `x == reversed_half // 10` koşullarından biri doğruysa `true` döndür, aksi takdirde `false` döndür.

## ⏱️ Karmaşıklık Analizi

*   **Zaman Karmaşıklığı: O(log N)**
    *   `N` giriş sayısının değerini temsil eder.
    *   Algoritma, `x`'in basamak sayısı kadar döngü yapar. Bir sayının basamak sayısı `log10(N)` ile orantılıdır. Bu nedenle, zaman karmaşıklığı logaritmiktir.

*   **Uzay Karmaşıklığı: O(1)**
    *   Algoritma, giriş boyutundan bağımsız olarak yalnızca sabit miktarda ek bellek (birkaç değişken) kullanır. Bu nedenle, uzay karmaşıklığı sabittir.

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
        # Sonu sıfır ile biten sayılar (0 hariç) palindrom olamaz.
        # Örneğin, 10 tersine çevrildiğinde 01 olur, 100 tersine çevrildiğinde 001 olur.
        if x < 0 or ( x % 10 == 0 and x != 0 ):
            return False
        
        # 2. Sayının yarısını tersine çevirmek için değişken başlatma
        reversed_half = 0  
        
        # 3. Sayının yarısını tersine çevirme döngüsü
        # x, reversed_half'ten büyük olduğu sürece döngü devam eder.
        # Bu, sayının yaklaşık yarısını tersine çevirdiğimizde döngünün durmasını sağlar.
        while x > reversed_half: 
            # reversed_half'e x'in son basamağını ekle
            reversed_half = reversed_half * 10 + x % 10
            # x'in son basamağını kaldır
            x //= 10

        # 4. Sonuç Kontrolü:
        # Döngü bittiğinde, iki durum olabilir:
        # a) Sayının basamak sayısı çift ise: x ve reversed_half tam olarak eşit olmalıdır. (örn: 1221 -> x=12, reversed_half=12)
        # b) Sayının basamak sayısı tek ise: x, reversed_half'in son basamağı atıldığında eşit olmalıdır.
        #    (örn: 121 -> x=1, reversed_half=12. reversed_half // 10 = 1. Ortadaki basamak atılır.)
        return x == reversed_half or x == reversed_half // 10

```

## 🧪 Örnek Test Case

**Giriş:** `x = 121`

**Beklenen Çıkış:** `true`

**Algoritma İzlemesi:**

1.  `x = 121`.
2.  **Kenar Durum Kontrolü:** `x` negatif değil ve sonu sıfır ile bitmiyor. Devam et.
3.  `reversed_half = 0`.
4.  **Döngü Başlangıcı:**
    *   **İterasyon 1:**
        *   `x (121) > reversed_half (0)` koşulu doğru.
        *   `reversed_half = 0 * 10 + 121 % 10 = 1`.
        *   `x = 121 // 10 = 12`.
    *   **İterasyon 2:**
        *   `x (12) > reversed_half (1)` koşulu doğru.
        *   `reversed_half = 1 * 10 + 12 % 10 = 10 + 2 = 12`.
        *   `x = 12 // 10 = 1`.
    *   **İterasyon 3:**
        *   `x (1) > reversed_half (12)` koşulu yanlış. Döngü sonlanır.
5.  **Sonuç Kontrolü:**
    *   `x = 1`, `reversed_half = 12`.
    *   `x == reversed_half` (`1 == 12`) -> `False`.
    *   `x == reversed_half // 10` (`1 == 12 // 10` yani `1 == 1`) -> `True`.
    *   Koşullardan biri doğru olduğu için `true` döndürülür.

## 🔗 LeetCode Linki

[Palindrome Number - LeetCode](https://leetcode.com/problems/palindrome-number/)

## 💻 Programlama Dili

python

---

*Bu README dosyası Universal LeetCode GitHub Sync Tool tarafından otomatik olarak oluşturulmuştur.*
