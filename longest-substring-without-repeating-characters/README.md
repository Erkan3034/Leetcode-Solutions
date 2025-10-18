# Longest Substring Without Repeating Characters

Harika, LeetCode problemi için profesyonel bir README.md dosyası oluşturalım.

---

# Longest Substring Without Repeating Characters

## 📝 Problem Açıklaması

Bu problemde, verilen bir `s` dizisi (string) içinde, tekrar eden karakterler içermeyen en uzun alt dizinin (substring) uzunluğunu bulmamız istenmektedir.

**Örnekler:**

*   **Örnek 1:**
    *   **Girdi:** `s = "abcabcbb"`
    *   **Çıktı:** `3`
    *   **Açıklama:** Cevap "abc" olup, uzunluğu 3'tür. "bca" ve "cab" de geçerli cevaplardır.
*   **Örnek 2:**
    *   **Girdi:** `s = "bbbbb"`
    *   **Çıktı:** `1`
    *   **Açıklama:** Cevap "b" olup, uzunluğu 1'dir.
*   **Örnek 3:**
    *   **Girdi:** `s = "pwwkew"`
    *   **Çıktı:** `3`
    *   **Açıklama:** Cevap "wke" olup, uzunluğu 3'tür. "pwke" bir alt dizi (substring) değil, bir alt sıra (subsequence) olduğu için geçerli değildir. Cevabın bir alt dizi olması gerektiğine dikkat ediniz.

**Kısıtlamalar:**

*   `0 <= s.length <= 5 * 10^4`
*   `s` dizisi İngilizce harfler, rakamlar, semboller ve boşluklardan oluşur.

## 💡 Çözüm Yaklaşımı

Bu problemi çözmek için **Kayar Pencere (Sliding Window)** algoritma deseni kullanılmıştır. Bu desen, diziler veya listeler üzerinde belirli bir koşulu sağlayan alt dizileri/alt listeleri verimli bir şekilde bulmak için idealdir.

Yaklaşım, iki işaretçi (`left` ve `right`) kullanarak bir "pencere" tanımlar. `right` işaretçisi pencereyi sağa doğru genişletirken, `left` işaretçisi pencereyi soldan daraltır. Pencere içindeki karakterlerin benzersizliğini takip etmek için bir `hash set` (Python'da `set`) kullanılır. `set` veri yapısı, eleman ekleme, silme ve varlığını kontrol etme işlemlerini ortalama O(1) zaman karmaşıklığında gerçekleştirdiği için bu problem için oldukça uygundur.

## ⚙️ Algoritma Adımları

1.  **Başlangıç Değerleri:**
    *   `seen` adında boş bir `set` oluşturulur. Bu set, mevcut kayar pencere içindeki benzersiz karakterleri tutacaktır.
    *   `left` işaretçisi `0` olarak başlatılır. Bu, pencerenin sol sınırını temsil eder.
    *   `max_len` değişkeni `0` olarak başlatılır. Bu, bulunan en uzun benzersiz alt dizinin uzunluğunu saklayacaktır.

2.  **Pencereyi Genişletme:**
    *   `right` işaretçisi, `s` dizisi üzerinde `0`'dan `len(s) - 1`'e kadar ilerler. Her adımda `s[right]` karakteri mevcut pencereye dahil edilmeye çalışılır.

3.  **Benzersizlik Kontrolü ve Pencereyi Daraltma:**
    *   `s[right]` karakteri `seen` setinde zaten varsa, bu, pencere içinde tekrar eden bir karakter olduğu anlamına gelir.
    *   Bu durumu düzeltmek için, `s[left]` karakteri `seen` setinden çıkarılır ve `left` işaretçisi bir artırılır. Bu işlem, `s[right]` karakteri `seen` setinde bulunmayana kadar tekrarlanır. Bu, pencereyi soldan daraltarak tekrar eden karakteri dışarı atmayı sağlar.

4.  **Karakteri Ekleme ve Uzunluğu Güncelleme:**
    *   `s[right]` karakteri artık `seen` setinde olmadığına göre (ya hiç yoktu ya da tekrar eden karakterler pencereden çıkarıldı), `s[right]` karakteri `seen` setine eklenir.
    *   Mevcut pencerenin uzunluğu (`right - left + 1`) hesaplanır ve `max_len` ile karşılaştırılarak maksimum değer `max_len`'e atanır.

5.  **Sonuç:**
    *   `right` işaretçisi dizinin sonuna ulaştığında, `max_len` değişkeni, tekrar eden karakterler içermeyen en uzun alt dizinin uzunluğunu tutacaktır. Bu değer döndürülür.

## ⏱️ Karmaşıklık Analizi

*   **Zaman Karmaşıklığı: O(N)**
    *   `right` işaretçisi dizinin her karakterini bir kez ziyaret eder (N adım).
    *   `left` işaretçisi de dizinin her karakterini en fazla bir kez ziyaret eder (ve `seen` setinden çıkarır).
    *   `set` veri yapısının `add()`, `remove()`, ve `in` (varlık kontrolü) işlemleri ortalama O(1) zaman karmaşıklığına sahiptir.
    *   Bu nedenle, toplam zaman karmaşıklığı dizinin uzunluğu `N` ile doğru orantılıdır.

*   **Uzay Karmaşıklığı: O(min(N, K))**
    *   `seen` seti, pencere içindeki benzersiz karakterleri saklar.
    *   En kötü durumda, tüm karakterler benzersizse, set `N` karakter saklayabilir.
    *   Ancak, karakter kümesinin boyutu `K` ile sınırlıdır (örneğin, ASCII karakterler için `K=128` veya `K=256`).
    *   Bu nedenle, setin saklayabileceği maksimum karakter sayısı `N` veya `K`'den küçük olanıdır.
    *   Pratikte, `K` genellikle `N`'den çok daha küçük ve sabit bir değer olarak kabul edildiğinde, uzay karmaşıklığı O(1) olarak da ifade edilebilir.

## 💻 Kod Açıklaması

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()      # 1. Pencere içindeki benzersiz karakterleri tutan hash set.
                          #    Karakterlerin varlığını O(1) ortalama sürede kontrol etmemizi sağlar.
        left = 0          # 2. Kayar pencerenin sol sınırını (başlangıç indeksini) temsil eden işaretçi.
        max_len = 0       # 3. Bulunan en uzun benzersiz alt dizinin uzunluğunu saklar.

        # 4. right işaretçisi ile diziyi baştan sona tararız. Bu, pencereyi sağa doğru genişletir.
        for right in range(len(s)):
            # 5. Eğer mevcut karakter (s[right]) zaten pencere içindeki karakterler arasında (seen setinde) ise,
            #    bu, bir tekrar eden karakter bulduğumuz anlamına gelir.
            while s[right] in seen:
                # 6. Tekrar eden karakteri ortadan kaldırmak için pencereyi soldan daraltırız.
                #    s[left] karakterini setten çıkarırız.
                seen.remove(s[left])
                # 7. Sol işaretçiyi bir adım sağa kaydırırız.
                left += 1

            # 8. s[right] karakteri artık pencere içinde benzersizdir (ya hiç yoktu ya da tekrar edenler çıkarıldı).
            #    Bu karakteri seen setine ekleriz.
            seen.add(s[right])

            # 9. Mevcut pencerenin uzunluğunu (right - left + 1) hesaplarız.
            #    Bu uzunluk ile şimdiye kadar bulunan maksimum uzunluğu karşılaştırırız ve büyük olanı max_len'e atarız.
            max_len = max(max_len, right - left + 1)

        # 10. Tüm dizi tarandıktan sonra, en uzun benzersiz alt dizinin uzunluğunu döndürürüz.
        return max_len
```

## 🧪 Örnek Test Case

**Girdi:**
```
s = "abcabcbb"
```

**Çıktı:**
```
3
```

**Açıklama:**

| `right` | `s[right]` | `seen` (önce) | `s[right] in seen` | `while` döngüsü (işlemler) | `seen` (sonra) | `left` | `right - left + 1` | `max_len` |
| :------ | :--------- | :------------ | :----------------- | :------------------------- | :------------- | :----- | :----------------- | :-------- |
| 0       | 'a'        | `{}`          | `False`            | -                          | `{'a'}`        | 0      | 1                  | 1         |
| 1       | 'b'        | `{'a'}`       | `False`            | -                          | `{'a', 'b'}`   | 0      | 2                  | 2         |
| 2       | 'c'        | `{'a', 'b'}`  | `False`            | -                          | `{'a', 'b', 'c'}` | 0      | 3                  | 3         |
| 3       | 'a'        | `{'a', 'b', 'c'}` | `True`             | `seen.remove('a')`, `left=1` | `{'b', 'c'}`   | 1      | 3                  | 3         |
|         |            |               | `s[3] ('a') in seen` | `False`                    | `{'b', 'c', 'a'}` | 1      | 3                  | 3         |
| 4       | 'b'        | `{'b', 'c', 'a'}` | `True`             | `seen.remove('b')`, `left=2` | `{'c', 'a'}`   | 2      | 3                  | 3         |
|         |            |               | `s[4] ('b') in seen` | `False`                    | `{'c', 'a', 'b'}` | 2      | 3                  | 3         |
| 5       | 'c'        | `{'c', 'a', 'b'}` | `True`             | `seen.remove('c')`, `left=3` | `{'a', 'b'}`   | 3      | 3                  | 3         |
|         |            |               | `s[5] ('c') in seen` | `False`                    | `{'a', 'b', 'c'}` | 3      | 3                  | 3         |
| 6       | 'b'        | `{'a', 'b', 'c'}` | `True`             | `seen.remove('a')`, `left=4` | `{'b', 'c'}`   | 4      | 3                  | 3         |
|         |            |               | `s[6] ('b') in seen` | `True`                     | `seen.remove('b')`, `left=5` | `{'c'}`        | 3                  | 3         |
|         |            |               | `s[6] ('b') in seen` | `False`                    | `{'c', 'b'}`   | 5      | 2                  | 3         |
| 7       | 'b'        | `{'c', 'b'}`  | `True`             | `seen.remove('c')`, `left=6` | `{'b'}`        | 6      | 2                  | 3         |
|         |            |               | `s[7] ('b') in seen` | `True`                     | `seen.remove('b')`, `left=7` | `{}`           | 2                  | 3         |
|         |            |               | `s[7] ('b') in seen` | `False`                    | `{'b'}`        | 7      | 1                  | 3         |

Döngü tamamlandığında `max_len` değeri `3` olarak kalır ve bu değer döndürülür.

## 🔗 LeetCode Linki

Bu problemin orijinal LeetCode sayfasına aşağıdaki bağlantıdan ulaşabilirsiniz:

[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## 💻 Programlama Dili

python

---

*Bu README dosyası Universal LeetCode GitHub Sync Tool tarafından otomatik olarak oluşturulmuştur.*