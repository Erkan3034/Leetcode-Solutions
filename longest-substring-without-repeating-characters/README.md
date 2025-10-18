# Longest Substring Without Repeating Characters

Harika bir LeetCode problemi için profesyonel bir README.md dosyası oluşturalım.

---

# Longest Substring Without Repeating Characters

## 📝 Problem Açıklaması

Bu problemde, verilen bir `s` dizgesi (string) içinde, tekrar eden karakterler içermeyen en uzun alt dizgenin (substring) uzunluğunu bulmamız istenmektedir. Alt dizge, orijinal dizgenin ardışık bir bölümü olmalıdır.

**Örnekler:**

*   **Örnek 1:**
    *   **Girdi:** `s = "abcabcbb"`
    *   **Çıktı:** `3`
    *   **Açıklama:** "abc" alt dizgesi 3 uzunluğundadır ve tekrar eden karakter içermez. "bca" ve "cab" de geçerli yanıtlardır.
*   **Örnek 2:**
    *   **Girdi:** `s = "bbbbb"`
    *   **Çıktı:** `1`
    *   **Açıklama:** "b" alt dizgesi 1 uzunluğundadır.
*   **Örnek 3:**
    *   **Girdi:** `s = "pwwkew"`
    *   **Çıktı:** `3`
    *   **Açıklama:** "wke" alt dizgesi 3 uzunluğundadır. "pwke" bir alt dizi (subsequence) olmasına rağmen, ardışık olmadığı için bir alt dizge (substring) değildir.

**Kısıtlamalar:**

*   `0 <= s.length <= 5 * 10^4`
*   `s` İngilizce harfler, rakamlar, semboller ve boşluklardan oluşur.

## 💡 Çözüm Yaklaşımı

Bu problemi çözmek için **Kayar Pencere (Sliding Window)** algoritması yaklaşımını kullanıyoruz. Bu yöntem, dizge üzerinde iki işaretçi (`left` ve `right`) ile tanımlanan bir "pencere"yi hareket ettirerek, belirli bir koşulu (bu durumda, tekrar eden karakter olmaması) sağlayan en iyi alt dizgeyi bulmayı hedefler.

Pencere içindeki karakterlerin benzersizliğini hızlı bir şekilde kontrol etmek için bir **hash seti (Python'da `set`)** kullanırız. Hash seti, eleman ekleme, silme ve kontrol etme işlemlerini ortalama O(1) zaman karmaşıklığında gerçekleştirdiği için bu problem için ideal bir veri yapısıdır.

Bu yaklaşım, her olası alt dizgeyi kontrol etmek yerine (ki bu O(N^2) veya O(N^3) olabilir), dizgeyi tek bir geçişte işleyerek zaman karmaşıklığını optimize eder.

## ⚙️ Algoritma Adımları

1.  **Başlangıç Değerleri:**
    *   `seen`: Pencere içindeki benzersiz karakterleri tutacak boş bir hash seti (`set`) oluştur.
    *   `left`: Pencerenin sol kenarını temsil eden işaretçiyi `0` olarak başlat.
    *   `max_len`: Bulunan en uzun tekrar etmeyen alt dizgenin uzunluğunu tutacak değişkeni `0` olarak başlat.

2.  **Pencereyi Genişletme:**
    *   `right` işaretçisini `0`'dan dizgenin sonuna kadar (`len(s) - 1`) ilerleten bir döngü başlat. Bu işaretçi, pencerenin sağ kenarını temsil eder.

3.  **Tekrar Eden Karakter Kontrolü ve Pencereyi Daraltma:**
    *   Her `right` iterasyonunda, `s[right]` karakterinin `seen` setinde olup olmadığını kontrol et.
    *   Eğer `s[right]` karakteri `seen` setinde zaten varsa (yani tekrar eden bir karakter bulunmuşsa):
        *   `s[left]` karakterini `seen` setinden çıkar.
        *   `left` işaretçisini bir birim sağa kaydır (`left += 1`).
        *   Bu işlemi, `s[right]` karakteri `seen` setinden tamamen çıkarılana kadar (veya `s[right]` karakteri `seen` setinde olmayana kadar) tekrarla. Bu, pencerenin sol tarafını daraltarak tekrar eden karakteri dışarı atmayı sağlar.

4.  **Yeni Karakteri Ekleme ve Uzunluğu Güncelleme:**
    *   `s[right]` karakterini `seen` setine ekle. (Bu noktada, pencere içindeki tüm karakterler benzersizdir.)
    *   Mevcut pencerenin uzunluğunu (`right - left + 1`) hesapla.
    *   `max_len` değişkenini, mevcut `max_len` ile yeni hesaplanan pencere uzunluğunun maksimumu ile güncelle (`max_len = max(max_len, right - left + 1)`).

5.  **Sonuç:**
    *   `right` döngüsü tamamlandığında, `max_len` değişkeni tekrar eden karakterler içermeyen en uzun alt dizgenin uzunluğunu tutacaktır. Bu değeri döndür.

## ⏱️ Karmaşıklık Analizi

*   **Zaman Karmaşıklığı: O(N)**
    *   `N`, giriş dizgesinin (`s`) uzunluğudur.
    *   `right` işaretçisi dizge üzerinde `N` kez ilerler.
    *   `left` işaretçisi de en fazla `N` kez ilerler (her karakter `seen` setine bir kez eklenir ve en fazla bir kez çıkarılır).
    *   `set` üzerindeki `add`, `remove` ve `in` işlemleri ortalama O(1) zaman karmaşıklığına sahiptir.
    *   Bu nedenle, algoritma dizgeyi etkin bir şekilde tek bir geçişte işler ve toplam zaman karmaşıklığı doğrusal, yani O(N) olur.

*   **Uzay Karmaşıklığı: O(min(N, A))**
    *   `A`, kullanılan karakter setinin (alfabe boyutu) boyutudur (örneğin, ASCII için 128 veya 256).
    *   `seen` seti, pencere içindeki benzersiz karakterleri saklar. En kötü durumda, tüm karakterler benzersizse, set `N` karakter içerebilir. Ancak, karakter seti boyutu (`A`) sınırlı olduğundan, setin içerebileceği maksimum karakter sayısı `A` ile sınırlıdır.
    *   Dolayısıyla, kullanılan ek alan `N` ve `A`'nın minimumu ile orantılıdır. Eğer `A` sabit ve küçükse (genellikle bu tür problemler için geçerlidir), uzay karmaşıklığı O(1) olarak da kabul edilebilir.

## 💻 Kod Açıklaması

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()      # 1. Pencere içindeki benzersiz karakterleri tutan hash seti.
                          #    Karakterlerin varlığını O(1) sürede kontrol etmek için kullanılır.
        left = 0          # 2. Kayar pencerenin sol kenarını işaret eden pointer.
        max_len = 0       # 3. Bulunan en uzun tekrar etmeyen alt dizgenin uzunluğu.

        # 4. right pointer'ı ile dizge üzerinde ilerle, pencereyi sağa doğru genişlet.
        for right in range(len(s)):
            # 5. Eğer mevcut karakter (s[right]) pencerede (seen setinde) zaten varsa,
            #    bu bir tekrar eden karakter olduğu anlamına gelir.
            while s[right] in seen:
                # 6. Pencerenin solundan karakterleri çıkararak pencereyi daralt.
                #    Bu, tekrar eden karakteri pencereden atana kadar devam eder.
                seen.remove(s[left])
                left += 1 # Sol pointer'ı bir sağa kaydır.

            # 7. Tekrar eden karakter kalmadığında veya yeni bir karakter geldiğinde,
            #    bu karakteri pencereye (seen setine) ekle.
            seen.add(s[right])

            # 8. Mevcut pencerenin uzunluğunu hesapla (right - left + 1) ve
            #    max_len ile karşılaştırarak en büyük olanı güncelle.
            max_len = max(max_len, right - left + 1)

        # 9. Tüm dizge işlendikten sonra, bulunan maksimum uzunluğu döndür.
        return max_len
```

## 🧪 Örnek Test Case

**Girdi:**
`s = "abcabcbb"`

**Çıktı:**
`3`

**Açıklama:**

1.  `seen = {}`, `left = 0`, `max_len = 0`
2.  `right = 0`, `s[0] = 'a'`:
    *   `'a'` `seen` içinde değil.
    *   `seen.add('a')` -> `seen = {'a'}`
    *   `max_len = max(0, 0 - 0 + 1) = 1`
3.  `right = 1`, `s[1] = 'b'`:
    *   `'b'` `seen` içinde değil.
    *   `seen.add('b')` -> `seen = {'a', 'b'}`
    *   `max_len = max(1, 1 - 0 + 1) = 2`
4.  `right = 2`, `s[2] = 'c'`:
    *   `'c'` `seen` içinde değil.
    *   `seen.add('c')` -> `seen = {'a', 'b', 'c'}`
    *   `max_len = max(2, 2 - 0 + 1) = 3`
5.  `right = 3`, `s[3] = 'a'`:
    *   `'a'` `seen` içinde **var**.
    *   `while 'a' in seen`:
        *   `seen.remove(s[left='a'])` -> `seen = {'b', 'c'}`
        *   `left = 1`
        *   `s[right='a']` hala `seen` içinde değil. Döngü biter.
    *   `seen.add('a')` -> `seen = {'b', 'c', 'a'}`
    *   `max_len = max(3, 3 - 1 + 1) = max(3, 3) = 3`
6.  `right = 4`, `s[4] = 'b'`:
    *   `'b'` `seen` içinde **var**.
    *   `while 'b' in seen`:
        *   `seen.remove(s[left='b'])` -> `seen = {'c', 'a'}`
        *   `left = 2`
        *   `s[right='b']` hala `seen` içinde değil. Döngü biter.
    *   `seen.add('b')` -> `seen = {'c', 'a', 'b'}`
    *   `max_len = max(3, 4 - 2 + 1) = max(3, 3) = 3`
7.  `right = 5`, `s[5] = 'c'`:
    *   `'c'` `seen` içinde **var**.
    *   `while 'c' in seen`:
        *   `seen.remove(s[left='c'])` -> `seen = {'a', 'b'}`
        *   `left = 3`
        *   `s[right='c']` hala `seen` içinde değil. Döngü biter.
    *   `seen.add('c')` -> `seen = {'a', 'b', 'c'}`
    *   `max_len = max(3, 5 - 3 + 1) = max(3, 3) = 3`
8.  `right = 6`, `s[6] = 'b'`:
    *   `'b'` `seen` içinde **var**.
    *   `while 'b' in seen`:
        *   `seen.remove(s[left='a'])` -> `seen = {'b', 'c'}`
        *   `left = 4`
        *   `s[right='b']` hala `seen` içinde var.
        *   `seen.remove(s[left='b'])` -> `seen = {'c'}`
        *   `left = 5`
        *   `s[right='b']` `seen` içinde değil. Döngü biter.
    *   `seen.add('b')` -> `seen = {'c', 'b'}`
    *   `max_len = max(3, 6 - 5 + 1) = max(3, 2) = 3`
9.  `right = 7`, `s[7] = 'b'`: (Dizge sonu, döngü biter.)

Döngü bittikten sonra `max_len` değeri `3` olarak döndürülür.

## 🔗 LeetCode Linki

Bu problemin orijinal LeetCode sayfasına aşağıdaki bağlantıdan ulaşabilirsiniz:

[Longest Substring Without Repeating Characters - LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## 💻 Programlama Dili

python

---

*Bu README dosyası Universal LeetCode GitHub Sync Tool tarafından otomatik olarak oluşturulmuştur.*