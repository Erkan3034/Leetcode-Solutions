# Add Two Numbers

Harika bir LeetCode problemi için profesyonel bir README.md dosyası hazırlayalım.

---

# Add Two Numbers

## 📝 Problem Açıklaması

Bu problemde, her biri boş olmayan iki adet tek yönlü bağlı liste (singly-linked list) verilmektedir. Bu bağlı listeler, negatif olmayan iki tam sayıyı temsil etmektedir. Sayıların basamakları ters sırada depolanmıştır ve her bir düğüm (node) tek bir basamak içermektedir. Görevimiz, bu iki sayıyı toplamak ve toplamı yine bir bağlı liste olarak döndürmektir.

Problem, verilen iki sayının, 0 sayısının kendisi hariç, önde sıfır içermediğini varsaymaktadır.

**Örnek 1:**
*   **Giriş:** `l1 = [2,4,3]`, `l2 = [5,6,4]`
*   **Çıkış:** `[7,0,8]`
*   **Açıklama:** `342 + 465 = 807`. (Bağlı listelerdeki basamaklar ters sırada olduğu için, `[2,4,3]` aslında 342'yi, `[5,6,4]` ise 465'i temsil eder.)

**Kısıtlamalar:**
*   Her bağlı listedeki düğüm sayısı `[1, 100]` aralığındadır.
*   `0 <= Node.val <= 9`
*   Listenin önde sıfır içermeyen bir sayıyı temsil ettiği garanti edilmektedir.

## 💡 Çözüm Yaklaşımı

Bu problem, ilkokulda öğrendiğimiz basamak basamak toplama işlemini simüle ederek çözülebilir. İki sayıyı toplarken sağdan sola doğru basamakları toplarız ve bir "elde" (carry) değeri oluşursa, bunu bir sonraki basamak toplamına ekleriz. Bağlı listelerdeki basamakların ters sırada olması, bu işlemi doğrudan soldan sağa (yani liste başından sonuna) yapmamıza olanak tanır.

Kullanılan temel veri yapısı bağlı listelerdir. Algoritma, her iki listede de düğümler olduğu sürece veya bir elde değeri mevcut olduğu sürece devam eden bir döngü etrafında döner. Her adımda, ilgili basamakları ve elde değerini toplayarak yeni bir basamak ve yeni bir elde değeri hesaplarız.

Bu yaklaşım, bağlı listelerin doğasına uygun olup, listelerin farklı uzunluklarda olması durumunu ve toplama sonucunda fazladan bir basamak oluşması (örneğin 99 + 1 = 100) durumunu zarifçe ele alır.

## ⚙️ Algoritma Adımları

1.  **Sahte Başlangıç Düğümü (Dummy Head) Oluşturma:** Sonuç bağlı listemizin başına `dummy = ListNode(0)` adında bir sahte düğüm oluşturulur. Bu düğüm, sonuç listesinin başına kolayca düğüm eklememizi sağlar ve boş liste gibi kenar durumlarını yönetmeyi basitleştirir.
2.  **Gezici İşaretçi (Current Pointer):** `current = dummy` ile sonuç listesinde ilerleyecek bir işaretçi tanımlanır. Yeni düğümler `current.next` olarak eklenecektir.
3.  **Elde Değeri (Carry):** `carry = 0` olarak başlatılır. Bu değişken, bir önceki basamak toplamından gelen elde değerini tutar.
4.  **Döngü Başlatma:** `l1` veya `l2` listelerinden herhangi birinde düğüm olduğu sürece VEYA `carry` değeri 0'dan büyük olduğu sürece bir `while` döngüsü başlatılır. Bu koşul, her iki liste bittikten sonra bile son bir elde değeri kalmış olabileceği durumunu ele alır.
5.  **Basamak Değerlerini Alma:**
    *   `val1`: Eğer `l1` mevcutsa `l1.val` değerini alır, aksi takdirde 0 olarak kabul edilir.
    *   `val2`: Eğer `l2` mevcutsa `l2.val` değerini alır, aksi takdirde 0 olarak kabul edilir.
6.  **Toplamı Hesaplama:** `total = val1 + val2 + carry` formülüyle mevcut basamakların ve elde değerinin toplamı bulunur.
7.  **Yeni Elde Değeri:** `carry = total // 10` ile yeni elde değeri hesaplanır (örneğin, 17 ise carry 1 olur).
8.  **Yeni Düğüm Oluşturma:** `current.next = ListNode(total % 10)` ile toplamın birler basamağı (`total % 10`) kullanılarak yeni bir düğüm oluşturulur ve sonuç listesine eklenir.
9.  **Gezici İşaretçiyi İlerletme:** `current = current.next` ile `current` işaretçisi yeni eklenen düğüme taşınır.
10. **Liste İşaretçilerini İlerletme:**
    *   Eğer `l1` mevcutsa, `l1 = l1.next` ile bir sonraki düğüme geçilir.
    *   Eğer `l2` mevcutsa, `l2 = l2.next` ile bir sonraki düğüme geçilir.
11. **Sonuç Döndürme:** Döngü tamamlandığında, `dummy.next` döndürülür. `dummy` düğümü sadece bir başlangıç noktası olduğu için, gerçek sonuç listesi `dummy`'nin bir sonraki düğümünden başlar.

## ⏱️ Karmaşıklık Analizi

*   **Zaman Karmaşıklığı: O(max(N, M))**
    *   Burada `N`, `l1` bağlı listesinin uzunluğunu ve `M`, `l2` bağlı listesinin uzunluğunu temsil eder.
    *   Algoritma, her iki listeyi de en fazla bir kez baştan sona dolaşır. Döngü, `l1` veya `l2` bitene kadar veya son bir elde değeri işlenene kadar devam eder. Bu nedenle, işlem süresi, iki listenin uzunluğunun maksimumu ile doğru orantılıdır.
*   **Uzay Karmaşıklığı: O(max(N, M))**
    *   Yeni bir bağlı liste oluşturulur. Bu yeni listenin uzunluğu, `max(N, M)` veya `max(N, M) + 1` olabilir (eğer son bir elde değeri ekstra bir basamak oluşturursa).
    *   Dolayısıyla, kullanılan ek alan, sonuç listesinin uzunluğu ile doğru orantılıdır.

## 💻 Kod Açıklaması

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Sonuç listesi için sahte bir başlangıç düğümü oluşturulur.
        # Bu, özellikle sonuç listesinin başına düğüm eklemeyi ve
        # boş liste gibi kenar durumlarını yönetmeyi kolaylaştırır.
        dummy = ListNode(0)
        
        # Sonuç listesinde ilerleyecek olan gezici işaretçi.
        # Başlangıçta sahte düğümü gösterir.
        current = dummy
        
        # Elde (carry) değerini tutar. Başlangıçta 0'dır.
        carry = 0

        # Döngü, her iki liste de bitene kadar VEYA bir elde değeri kalana kadar devam eder.
        # 'carry' kontrolü, örneğin 9+1=10 gibi durumlarda fazladan bir basamak eklenmesini sağlar.
        while l1 or l2 or carry:
            # l1'den basamak değerini al, eğer l1 bitmişse 0 kullan.
            val1 = l1.val if l1 else 0
            # l2'den basamak değerini al, eğer l2 bitmişse 0 kullan.
            val2 = l2.val if l2 else 0

            # Mevcut basamakları ve elde değerini topla.
            total = val1 + val2 + carry
            
            # Yeni elde değerini hesapla (örneğin, 17 ise carry 1 olur).
            carry = total // 10
            
            # Toplamın birler basamağını kullanarak yeni bir düğüm oluştur
            # ve bunu sonuç listesine ekle.
            current.next = ListNode(total % 10)
            
            # Gezici işaretçiyi yeni eklenen düğüme taşı.
            current = current.next

            # l1 listesini bir sonraki düğüme ilerlet (eğer mevcutsa).
            if l1:
                l1 = l1.next
            # l2 listesini bir sonraki düğüme ilerlet (eğer mevcutsa).
            if l2:
                l2 = l2.next
        
        # Sahte düğümün bir sonraki düğümünü döndür. Bu, gerçek sonuç listesinin başıdır.
        return dummy.next

```

## 🧪 Örnek Test Case

**Giriş:**
*   `l1 = [2,4,3]` (Temsil ettiği sayı: 342)
*   `l2 = [5,6,4]` (Temsil ettiği sayı: 465)

**Çalışma Adımları:**

1.  `dummy = ListNode(0)`, `current = dummy`, `carry = 0`
2.  **1. İterasyon:**
    *   `l1.val = 2`, `l2.val = 5`
    *   `total = 2 + 5 + 0 = 7`
    *   `carry = 7 // 10 = 0`
    *   `current.next = ListNode(7 % 10) = ListNode(7)`
    *   `current` yeni `ListNode(7)`'ye geçer.
    *   `l1 = [4,3]`, `l2 = [6,4]`
3.  **2. İterasyon:**
    *   `l1.val = 4`, `l2.val = 6`
    *   `total = 4 + 6 + 0 = 10`
    *   `carry = 10 // 10 = 1`
    *   `current.next = ListNode(10 % 10) = ListNode(0)`
    *   `current` yeni `ListNode(0)`'a geçer.
    *   `l1 = [3]`, `l2 = [4]`
4.  **3. İterasyon:**
    *   `l1.val = 3`, `l2.val = 4`
    *   `total = 3 + 4 + 1 = 8` (önceki iterasyondan gelen `carry` = 1)
    *   `carry = 8 // 10 = 0`
    *   `current.next = ListNode(8 % 10) = ListNode(8)`
    *   `current` yeni `ListNode(8)`'e geçer.
    *   `l1 = None`, `l2 = None`
5.  **Döngü Sonu:** `l1` ve `l2` `None` oldu, `carry` 0. Döngü biter.
6.  **Dönüş Değeri:** `dummy.next` döndürülür, bu da `[7,0,8]` listesini temsil eder.

**Çıkış:**
*   `[7,0,8]` (Temsil ettiği sayı: 807)

## 🔗 LeetCode Linki

Bu problemin orijinal LeetCode sayfasına aşağıdaki bağlantıdan ulaşabilirsiniz:
[https://leetcode.com/problems/add-two-numbers/](https://leetcode.com/problems/add-two-numbers/)

## 💻 Programlama Dili

python

---

*Bu README dosyası Universal LeetCode GitHub Sync Tool tarafından otomatik olarak oluşturulmuştur.*