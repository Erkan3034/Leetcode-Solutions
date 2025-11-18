# Median of Two Sorted Arrays

Harika bir LeetCode problemi! Verilen kodun karmaşıklık gereksinimini karşılamadığını belirterek, profesyonel bir README.md dosyası oluşturalım.

---

# Median of Two Sorted Arrays

## Problem Açıklaması

İki sıralı dizi `nums1` ve `nums2` veriliyor. Bu dizilerin boyutları sırasıyla `m` ve `n`'dir. Görevimiz, bu iki dizinin birleşiminden oluşan dizinin medyanını bulmaktır. Çözümün genel zaman karmaşıklığı `O(log (m+n))` olmalıdır.

**Örnek 1:**
*   **Giriş:** `nums1 = [1,3]`, `nums2 = [2]`
*   **Çıkış:** `2.00000`
*   **Açıklama:** Birleştirilmiş dizi `[1,2,3]` ve medyan `2`'dir.

**Örnek 2:**
*   **Giriş:** `nums1 = [1,2]`, `nums2 = [3,4]`
*   **Çıkış:** `2.50000`
*   **Açıklama:** Birleştirilmiş dizi `[1,2,3,4]` ve medyan `(2 + 3) / 2 = 2.5`'tir.

**Kısıtlar:**
*   `nums1.length == m`
*   `nums2.length == n`
*   `0 <= m <= 1000`
*   `0 <= n <= 1000`
*   `1 <= m + n <= 2000`
*   `-10^6 <= nums1[i], nums2[i] <= 10^6`

## Çözüm Yaklaşımı

Bu problem için optimal çözüm, iki sıralı dizi üzerinde ikili arama (binary search) yaparak `O(log (m+n))` zaman karmaşıklığına ulaşmayı gerektirir. Bu yaklaşım, dizileri fiziksel olarak birleştirmeden, medyanın konumunu bulmak için bölme ve yönetme (divide and conquer) stratejisini kullanır.

**Ancak, sağlanan Python kodu, problemde belirtilen `O(log (m+n))` karmaşıklık hedefini karşılamayan daha basit bir yaklaşım benimsemektedir.** Sağlanan çözüm, iki diziyi birleştirip ardından sıralayarak medyanı bulur. Bu yaklaşım, anlaşılması ve uygulanması kolay olmakla birlikte, zaman karmaşıklığı açısından daha az verimlidir. Bu README, sağlanan kodun mantığını ve karmaşıklığını analiz edecektir.

## Algoritma Adımları

Sağlanan çözümün algoritma adımları aşağıdaki gibidir:

1.  **Dizileri Birleştirme:** `nums1` ve `nums2` dizileri tek bir `merged_array` içinde birleştirilir. Bu, Python'da `+` operatörü ile kolayca yapılabilir.
2.  **Birleştirilmiş Diziyi Sıralama:** `merged_array` dizisi, Python'ın yerleşik `sorted()` fonksiyonu kullanılarak küçükten büyüğe doğru sıralanır. Bu adım, dizinin medyanını doğru bir şekilde bulabilmek için kritik öneme sahiptir.
3.  **Dizi Uzunluğunu Belirleme:** Sıralanmış dizinin toplam eleman sayısı (`n`) bulunur.
4.  **Boş Dizi Kontrolü:** Eğer `n` sıfır ise (dizi boşsa), medyan `0.0` olarak döndürülür. (Kısıtlar gereği `m+n >= 1` olduğundan bu durum pratikte oluşmayacaktır, ancak genel bir güvenlik kontrolüdür.)
5.  **Medyanı Hesaplama:**
    *   **Tek Uzunluk:** Eğer `n` tek sayı ise, medyan `sorted_array[n // 2]` konumundaki elemandır. `//` operatörü tam sayı bölme yaptığı için, bu bize tam orta indeksi verir. Bu değer `float` tipine dönüştürülür.
    *   

## 🔗 LeetCode Linki

[Problem Linki](https://leetcode.com/problems/median-of-two-sorted-arrays/)

## 💻 Programlama Dili

python

---

*Bu README dosyası Universal LeetCode GitHub Sync Tool tarafından otomatik olarak oluşturulmuştur.*