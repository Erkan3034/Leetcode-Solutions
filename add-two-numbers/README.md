
# Add Two Numbers

## 📝 Problem Açıklaması

Bu problemde, negatif olmayan iki tam sayıyı temsil eden, boş olmayan iki tek yönlü bağlı liste (`l1` ve `l2`) verilmiştir. Bu sayılar, basamakları ters sırada depolanmış şekilde bağlı listelerde tutulur ve her düğüm tek bir basamak içerir. Göreviniz, bu iki sayıyı toplamak ve toplamı yeni bir bağlı liste olarak döndürmektir.

Verilen sayılarda, 0 sayısının kendisi hariç, önde gelen sıfır bulunmadığı varsayılabilir.

**Örnek 1:**
*   **Giriş:** `l1 = [2,4,3]`, `l2 = [5,6,4]`
*   **Çıkış:** `[7,0,8]`
*   **Açıklama:** `342 + 465 = 807`. (Basamaklar ters sırada olduğu için `[2,4,3]` aslında 342'yi, `[5,6,4]` ise 465'i temsil eder.)

**Örnek 2:**
*   **Giriş:** `l1 = [0]`, `l2 = [0]`
*   **Çıkış:** `[0]`

**Örnek 3:**
*   **Giriş:** `l1 = [9,9,9,9,9,9,9]`, `l2 = [9,9,9,9]`
*   **Çıkış:** `[8,9,9,9,0,0,0,1]`

**Kısıtlamalar:**
*   Her bağlı listedeki düğüm sayısı `[1, 100]` aralığındadır.
*   `0 <= Node.val <= 9`
*   Listelerin önde gelen sıfır içermediği garanti edilmiştir (0 sayısının kendisi hariç).

## 💡 Çözüm Yaklaşımı

Bu problem, ilkokulda öğrendiğimiz elden toplama (carry-over addition) yöntemini taklit ederek çözülebilir. Basamaklar ters sırada verildiği için, bağlı listelerin başından başlayarak karşılıklı düğümleri toplamak, sayıların en düşük basamaklarından başlayarak toplama işlemine eşdeğerdir.

Kullanılan temel veri yapısı tek yönlü bağlı listelerdir. Algoritma, her iki bağlı listeyi aynı anda dolaşarak ve her adımda karşılıklı basamakları (ve varsa bir önceki adımdan gelen eldeyi) toplayarak yeni bir bağlı liste oluşturur.

Bu yaklaşım, sayıları doğrudan tamsayılara dönüştürme ihtiyacını ortadan kaldırır. Bu, özellikle çok büyük sayılarla (standart tamsayı veri tiplerinin kapasitesini aşabilecek sayılarla) karşılaşıldığında önemlidir. Ayrıca, bağlı listelerin doğasına uygun, doğrudan ve verimli bir çözümdür.

## ⚙️ Algoritma Adımları

1.  **Başlangıç Düğümü Oluşturma:** Sonuç bağlı listesinin başına referans olarak kullanılacak bir "sahte" (dummy) düğüm (`dummy`) oluşturulur. Bu düğümün değeri genellikle 0 olarak ayarlanır. Bu, sonuç listesini oluşturmayı ve döndürmeyi kolaylaştırır, çünkü gerçek başlangıç düğümü `dummy.next` olacaktır.
2.  **Gezici İşaretçi:** Sonuç listesini oluştururken mevcut düğümü takip etmek için bir `current` işaretçisi oluşturulur ve başlangıçta `dummy` düğümüne atanır.
3.  **Elde Değişkeni:** Bir önceki toplama işleminden kalan eldeyi (`carry`) saklamak için `carry` adında bir tamsayı değişkeni oluşturulur ve başlangıçta 0 olarak ayarlanır.
4.  **Döngü:** `l1` listesi bitene, `l2` listesi bitene veya `carry` değeri 0'dan farklı olana kadar bir döngü devam ettirilir. Bu koşul, tüm basamakların işlendiğinden ve son bir eldenin de hesaba katıldığından emin olur.
5.  **Değerleri Alma:** Her döngü adımında, `l1`'den `val1` ve `l2`'den `val2` değerleri alınır. Eğer ilgili liste bitmişse (yani `l1` veya `l2` `None` ise), o basamağın değeri 0 olarak kabul edilir.
6.  **Toplama İşlemi:** `val1`, `val2` ve `carry` değerleri toplanarak `total` elde edilir.
7.  **Elde Güncelleme:** `total` değeri 10'a bölünerek yeni `carry` değeri (`total // 10`) hesaplanır.
8.  **Yeni Düğüm Oluşturma:** `total` değerinin 10'a bölümünden kalan (`total % 10`) ile yeni bir `ListNode` oluşturulur. Bu, toplama işleminin mevcut basamağını temsil eder.
9.  **Listeye Ekleme:** Oluşturulan yeni düğüm, `current.next` olarak atanır.
10. **İşaretçileri İlerletme:** `current` işaretçisi yeni oluşturulan düğüme (`current = current.next`) ilerletilir. Eğer `l1` veya `l2` henüz bitmemişse, ilgili liste işaretçileri de bir sonraki düğüme (`l1 = l1.next`, `l2 = l2.next`) ilerletilir.
11. **Sonuç Döndürme:** Döngü sona erdiğinde, `dummy.next` döndürülür. Bu, sahte başlangıç düğümünü atlayarak gerçek sonuç listesinin başını verir.

## 📈 Karmaşıklık Analizi

*   **Zaman Karmaşıklığı: `O(max(m, n))`**
    *   Burada `m`, `l1` bağlı listesinin uzunluğunu ve `n`, `l2` bağlı listesinin uzunluğunu temsil eder.
    *   Algoritma, her iki bağlı listeyi en fazla bir kez dolaşır. Döngü, daha uzun olan listenin uzunluğu kadar veya potansiyel bir son elde basamağı için bir adım daha fazla çalışır. Bu nedenle, zaman karmaşıklığı, iki listenin uzunluğunun maksimumu ile doğru orantılıdır.

*   **Uzay Karmaşıklığı: `O(max(m, n))`**
    *   Algoritma, toplamı depolamak için yeni bir bağlı liste oluşturur.
    *   Bu yeni bağlı listenin uzunluğu, en uzun giriş listesinin uzunluğundan en fazla bir fazla olabilir (örneğin, 99 + 1 = 100 gibi bir durumda).
    *   Bu nedenle, oluşturulan yeni bağlı listenin boyutu, `max(m, n)` ile doğru orantılıdır.

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
        # Sonuç bağlı listesinin başına referans olarak kullanılacak sahte bir düğüm oluşturulur.
        # Bu, listeyi oluşturmayı ve döndürmeyi kolaylaştırır.
        dummy = ListNode(0)
        
        # Sonuç listesini oluştururken mevcut düğümü takip etmek için bir işaretçi.
        # Başlangıçta dummy düğümüne işaret eder.
        current = dummy
        
        # Bir önceki toplama işleminden kalan eldeyi saklamak için değişken.
        carry = 0

        # Döngü, her iki liste de bitene ve elde kalmayana kadar devam eder.
        # Bu, farklı uzunluktaki listeleri ve son eldeyi doğru şekilde ele almayı sağlar.
        while l1 or l2 or carry:
            # l1'den değeri al, eğer l1 bitmişse 0 kabul et.
            val1 = l1.val if l1 else 0
            # l2'den değeri al, eğer l2 bitmişse 0 kabul et.
            val2 = l2.val if l2 else 0

            # Mevcut basamakları ve eldeyi topla.
            total = val1 + val2 + carry
            
            # Yeni eldeyi hesapla (toplamın 10'a bölümü).
            carry = total // 10
            
            # Toplamın birler basamağı ile yeni bir düğüm oluştur.
            # Bu, sonuç listesinin mevcut basamağını temsil eder.
            current.next = ListNode(total % 10)
            
            # current işaretçisini yeni oluşturulan düğüme ilerlet.
            current = current.next

            # Eğer l1 henüz bitmemişse, bir sonraki düğüme geç.
            if l1:
                l1 = l1.next
            # Eğer l2 henüz bitmemişse, bir sonraki düğüme geç.
            if l2:
                l2 = l2.next

        # Sahte başlangıç düğümünü atlayarak gerçek sonuç listesinin başını döndür.
        return dummy.next

```

## 🧪 Örnek Test Case

**Giriş:**
*   `l1 = [2,4,3]` (Bu, 342 sayısını temsil eder)
*   `l2 = [5,6,4]` (Bu, 465 sayısını temsil eder)

**Çalışma Adımları:**

1.  `dummy = ListNode(0)`, `current = dummy`, `carry = 0`
2.  **1. İterasyon:**
    *   `l1.val = 2`, `l2.val = 5`
    *   `total = 2 + 5 + 0 = 7`
    *   `carry = 7 // 10 = 0`
    *   `current.next = ListNode(7 % 10) = ListNode(7)`
    *   `current` şimdi `ListNode(7)`'ye işaret eder.
    *   `l1 = ListNode(4)`, `l2 = ListNode(6)`
3.  **2. İterasyon:**
    *   `l1.val = 4`, `l2.val = 6`
    *   `total = 4 + 6 + 0 = 10`
    *   `carry = 10 // 10 = 1`
    *   `current.next = ListNode(10 % 10) = ListNode(0)`
    *   `current` şimdi `ListNode(0)`'a işaret eder.
    *   `l1 = ListNode(3)`, `l2 = ListNode(4)`
4.  **3. İterasyon:**
    *   `l1.val = 3`, `l2.val = 4`
    *   `total = 3 + 4 + 1 = 8` (carry = 1)
    *   `carry = 8 // 10 = 0`
    *   `current.next = ListNode(8 % 10) = ListNode(8)`
    *   `current` şimdi `ListNode(8)`'e işaret eder.
    *   `l1 = None`, `l2 = None`
5.  **Döngü Sonu:** `l1`, `l2` ve `carry` hepsi 0 olduğu için döngü sona erer.
6.  **Dönüş Değeri:** `dummy.next` döndürülür.

**Çıkış:**
*   `[7,0,8]` (Bu, 807 sayısını temsil eder)

## 🔗 LeetCode Linki

[Add Two Numbers - LeetCode](https://leetcode.com/problems/add-two-numbers/)

---

## 💻 Programlama Dili

python

---

*Bu README dosyası Universal LeetCode GitHub Sync Tool tarafından otomatik olarak oluşturulmuştur.*
