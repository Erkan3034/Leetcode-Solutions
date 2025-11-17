# Median of Two Sorted Arrays

Harika! LeetCode'daki "Median of Two Sorted Arrays" problemi için profesyonel bir `README.md` dosyası oluşturalım. Verilen çözümün karmaşıklık gereksinimini karşılamadığını belirterek, mevcut kodu detaylı bir şekilde açıklayacağım.

---

# Median of Two Sorted Arrays

## Problem Açıklaması

Bu problemde, `nums1` ve `nums2` adında, sırasıyla `m` ve `n` boyutlarında iki adet sıralı tam sayı dizisi verilmektedir. Görevimiz, bu iki dizinin birleşimiyle oluşacak dizinin medyanını bulmaktır. Problemin önemli bir kısıtı, çözümün zaman karmaşıklığının `O(log (m+n))` olması gerektiğidir.

**Örnek 1:**
*   **Giriş:** `nums1 = [1,3]`, `nums2 = [2]`
*   **Çıkış:** `2.00000`
*   **Açıklama:** Birleştirilmiş dizi `[1,2,3]`'tür ve medyan 2'dir.

**Örnek 2:**
*   **Giriş:** `nums1 = [1,2]`, `nums2 = [3,4]`
*   **Çıkış:** `2.50000`
*   **Açıklama:** Birleştirilmiş dizi `[1,2,3,4]`'tür ve medyan `(2 + 3) / 2 = 2.5`'tir.

**Kısıtlar:**
*   `nums1.length == m`
*   `nums2.length == n`
*   `0 <= m <= 1000`
*   `0 <= n <= 1000`
*   `1 <= m + n <= 2000`
*   `-10^6 <= nums1[i], nums2[i] <= 10^6`

## Çözüm Yaklaşımı

Verilen çözüm, iki sıralı diziyi birleştirip ardından bu birleşik diziyi tekrar sıralama ve medyanı hesaplama stratejisini izlemektedir. Bu yaklaşım, problemin temel mantığını anlamak ve medyan hesaplamasını gerçekleştirmek için basit ve anlaşılır bir yol sunar.

Ancak, problem tanımında belirtilen `O(log (m+n))` zaman karmaşıklığı gereksinimini karşılamamaktadır. Optimal çözüm genellikle iki dizideki bölümleri (partitions) ikili arama (binary search) kullanarak arayarak, medyanı `O(log(min(m,n)))` veya `O(log(m+n))` zamanında bulmayı hedefler. Verilen çözüm ise, birleştirme ve sıralama işlemleri nedeniyle daha yüksek bir zaman karmaşıklığına sahiptir.

Bu `README.md` dosyasında, sağlanan kodun çalışma prensibi ve karmaşıklık analizi detaylandırılacaktır.

## Algoritma Adımları

Verilen çözüm aşağıdaki adımları takip eder:

1.  **Dizileri Birleştirme:** `nums1` ve `nums2` dizileri tek bir `merged_array` içinde birleştirilir.
2.  **Birleşik Diziyi Sıralama:** `merged_array` Python'ın yerleşik `sorted()` fonksiyonu kullanılarak küçükten büyüğe doğru sıralanır ve `sorted_array` adında yeni bir dizi oluşturulur.
3.  **Dizinin Boyutunu Belirleme:** Sıralanmış dizinin toplam eleman sayısı (`n`) bulunur.
4.  **Medyanı Hesaplama:**
    *   Eğer `n` (dizinin boyutu) tek sayı ise, medyan `sorted_array[n // 2]` konumundaki elemandır.
    *   Eğer `n` çift sayı ise, medyan `sorted_array[(n // 2) - 1]` ve `sorted_array[n // 2]` konumundaki iki orta elemanın ortalamasıdır.
5.  **Sonucu Döndürme:** Hesaplanan medyan değeri `float` olarak döndürülür.

## Karmaşıklık Analizi

Verilen çözümün karmaşıklık analizi aşağıdaki gibidir:

*   **Zaman Karmaşıklığı:** `O((m+n) log (m+n))`
    *   `merged_array = nums1 + nums2`: İki diziyi birleştirmek `O(m+n)` zaman alır.
    *   `sorted_array = sorted(merged_array)`: Birleştirilmiş `m+n` boyutundaki diziyi sıralamak, genel amaçlı bir sıralama algoritması (örneğin Timsort) kullanıldığında `O((m+n) log (m+n))` zaman alır.
    *   Medyanı hesaplamak (dizinin ortasındaki elemanlara erişim): `O(1)` zaman alır.
    *   Bu nedenle, toplam zaman karmaşıklığı `O((m+n) log (m+n))`'dir.
    *   **Not:** Bu karmaşıklık, problem tanımında istenen `O(log (m+n))` optimal zaman karmaşıklığı gereksinimini karşılamamaktadır. Optimal çözüm için ikili arama tabanlı daha karmaşık bir algoritma gereklidir.

*   **Uzay Karmaşıklığı:** `O(m+n)`
    *   `merged_array`: `nums1` ve `nums2`'nin birleştirilmesiyle `O(m+n)` boyutunda yeni bir dizi oluşturulur.
    *   `sorted_array`: `sorted()` fonksiyonu genellikle orijinal diziyi değiştirmek yerine yeni bir sıralı dizi döndürdüğü için, `O(m+n)` boyutunda ek bellek alanı gerektirir.
    *   Bu nedenle, toplam uzay karmaşıklığı `O(m+n)`'dir.

## Kod Açıklaması

```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        # Adım 1: İki diziyi birleştirme
        # nums1 ve nums2 dizilerini '+' operatörü ile birleştirerek yeni bir dizi oluşturur.
        # Bu işlem O(m+n) zaman ve O(m+n) uzay karmaşıklığına sahiptir.
        merged_array = nums1 + nums2
        
        # Adım 2: Birleşik diziyi sıralama
        # Python'ın yerleşik sorted() fonksiyonunu kullanarak birleşik diziyi sıralar.
        # Bu fonksiyon, Timsort algoritmasını kullanır ve O((m+n) log (m+n)) zaman
        # ve O(m+n) uzay karmaşıklığına sahiptir.
        sorted_array = sorted(merged_array)

        # Adım 3: Sıralanmış dizinin boyutunu belirleme
        # Medyanı hesaplamak için dizinin uzunluğu gereklidir.
        n = len(sorted_array)
        
        # Kenar Durum Kontrolü: Dizi boşsa 0.0 döndürür.
        # Problem kısıtlarına göre (1 <= m + n <= 2000) bu durum oluşmayacaktır,
        # ancak genel bir sağlamlık kontrolüdür.
        if n == 0:
            return 0.0

        # Adım 4: Medyanı hesaplama
        # Dizinin uzunluğu tek mi çift mi kontrol edilir.
        if n % 2 == 1:
            # Dizi uzunluğu tek ise, medyan tam ortadaki elemandır.
            # Örneğin, [1,2,3] için n=3, n//2=1, sorted_array[1] = 2.
            median = float(sorted_array[n // 2])
        else:
            # Dizi uzunluğu çift ise, medyan ortadaki iki elemanın ortalamasıdır.
            # Örneğin, [1,2,3,4] için n=4, (n//2)-1=1, n//2=2.
            # sorted_array[1]=2, sorted_array[2]=3. Medyan (2+3)/2 = 2.5.
            mid1 = sorted_array[(n // 2) - 1]
            mid2 = sorted_array[n // 2]
            median = (mid1 + mid2) / 2.0

        # Adım 5: Hesaplanan medyanı döndürme
        return median

```

## Örnek Test Case

**Örnek 1:**

*   **Giriş:**
    ```python
    nums1 = [1,3]
    nums2 = [2]
    ```
*   **Çalışma Adımları:**
    1.  `merged_array = [1,3,2]`
    2.  `sorted_array = [1,2,3]`
    3.  `n = 3`
    4.  `n` tek sayı olduğu için `median = float(sorted_array[3 // 2]) = float(sorted_array[1]) = 2.0`
*   **Çıkış:**
    ```
    2.00000
    ```

**Örnek 2:**

*   **Giriş:**
    ```python
    nums1 = [1,2]
    nums2 = [3,4]
    ```
*   **Çalışma Adımları:**
    1.  `merged_array = [1,2,3,4]`
    2.  `sorted_array = [1,2,3,4]`
    3.  `n = 4`
    4.  `n` çift sayı olduğu için `mid1 = sorted_array[(4 // 2) - 1] = sorted_array[1] = 2` ve `mid2 = sorted_array[4 // 2] = sorted_array[2] = 3`.
        `median = (2 + 3) / 2.0 = 2.5`
*   **Çıkış:**
    ```
    2.50000
    ```

## LeetCode Linki

Bu problem ve diğer çözümler için LeetCode sayfasını ziyaret edebilirsiniz:
[https://leetcode.com/problems/median-of-two-sorted-arrays/](https://leetcode.com/problems/median-of-two-sorted-arrays/)

## 💻 Programlama Dili

python

---

*Bu README dosyası Universal LeetCode GitHub Sync Tool tarafından otomatik olarak oluşturulmuştur.*