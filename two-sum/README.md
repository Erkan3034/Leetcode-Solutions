# Two Sum

Harika bir LeetCode problemi için profesyonel bir README.md dosyası oluşturalım.

---

# Two Sum

## Problem Açıklaması

Bize bir tamsayı dizisi `nums` ve bir tamsayı `target` verilmiştir. Görevimiz, `nums` dizisindeki toplamları `target` değerine eşit olan iki sayının indekslerini döndürmektir.

Problem, her giriş için tam olarak bir çözümün var olduğunu ve aynı elemanın iki kez kullanılamayacağını varsaymaktadır. Sonuç indeksleri herhangi bir sırada döndürülebilir.

**Örnek 1:**
```
Giriş: nums = [2,7,11,15], target = 9
Çıkış: [0,1]
Açıklama: Çünkü nums[0] + nums[1] == 9, [0, 1] döndürüyoruz.
```

**Kısıtlamalar:**
*   `2 <= nums.length <= 10^4`
*   `-10^9 <= nums[i] <= 10^9`
*   `-10^9 <= target <= 10^9`
*   Yalnızca bir geçerli cevap mevcuttur.

**Ek Soru:** Zaman karmaşıklığı O(n^2)'den daha düşük bir algoritma bulabilir misiniz?

## Çözüm Yaklaşımı

Bu problem için en yaygın ve verimli yaklaşım, bir **hash map (Python'da sözlük)** kullanmaktır.

**Neden Hash Map?**

Naive bir yaklaşım, iç içe iki döngü kullanarak her olası çifti kontrol etmek olacaktır. Bu, O(n^2) zaman karmaşıklığına sahip olurdu ki, `n`'nin 10^4'e kadar çıkabileceği düşünüldüğünde, bu çözüm çok yavaş kalabilir (10^8 işlem civarı). Problemin "Follow-up" kısmı da O(n^2)'den daha iyi bir çözüm arayışına işaret etmektedir.

Hash map kullanarak, her bir eleman için `target - current_num` değerini (yani "tamamlayıcı" sayıyı) dizide daha önce görüp görmediğimizi O(1) ortalama zaman karmaşıklığı ile kontrol edebiliriz. Bu sayede, diziyi sadece tek bir geçişle işleyerek O(n) zaman karmaşıklığına ulaşabiliriz.

## Algoritma Adımları

1.  Boş bir hash map (Python'da `dict`) oluşturun. Bu map, anahtar olarak sayıları ve değer olarak bu sayıların `nums` dizisindeki indekslerini saklayacaktır. Adına `seen` diyelim.
2.  `nums` dizisi üzerinde indeksleri (`i`) ve değerleri (`num`) ile birlikte tek bir döngü ile ilerleyin.
3.  Her `num` için, `complement = target - num` değerini hesaplayın. Bu, `num` ile birlikte `target` değerini oluşturacak olan ikinci sayıdır.
4.  `complement` değerinin `seen` hash map'inde olup olmadığını kontrol edin:
    *   Eğer `complement` hash map'te varsa, bu, aradığımız iki sayıdan birini (şu anki `num`) ve diğerini (hash map'teki `complement`) bulduğumuz anlamına gelir. `seen[complement]` bize `complement`'in indeksini verecektir. Bu durumda `[seen[complement], i]` indekslerini döndürün.
    *   Eğer `complement` hash map'te yoksa, şu anki `num`'ı ve onun indeksini (`i`) `seen` hash map'ine ekleyin (`seen[num] = i`). Bu, sonraki elemanlar için `num`'ın bir tamamlayıcı olarak kullanılabileceği anlamına gelir.
5.  Problem kısıtlamalarına göre her zaman tam olarak bir çözüm olduğu için, döngü tamamlanmadan önce bir çift bulunup döndürülecektir.

## Karmaşıklık Analizi

*   **Zaman Karmaşıklığı: O(n)**
    *   Dizi üzerinde yalnızca tek bir geçiş yapıyoruz.
    *   Her adımda, hash map'e ekleme (`seen[num] = i`) ve hash map'te arama (`complement in seen`) işlemleri ortalama O(1) zaman alır.
    *   Bu nedenle, toplam zaman karmaşıklığı dizinin uzunluğu `n` ile doğru orantılıdır, yani O(n)'dir.

*   **Uzay Karmaşıklığı: O(n)**
    *   En kötü durumda, `nums` dizisindeki tüm elemanları `seen` hash map'inde saklamamız gerekebilir (eğer çözüm son elemanlara yakın bulunursa).
    *   Bu durumda, hash map'in boyutu `n`'ye kadar çıkabilir.
    *   Bu nedenle, toplam uzay karmaşıklığı O(n)'dir.

## Kod Açıklaması

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # seen adında boş bir sözlük (hash map) başlatıyoruz.
        # Bu sözlük, daha önce karşılaştığımız sayıları (anahtar) ve
        # bu sayıların orijinal dizideki indekslerini (değer) saklayacak.
        seen = {} 
        
        # nums dizisi üzerinde hem indeks (i) hem de değer (num) ile döngü yapıyoruz.
        for i, num in enumerate(nums):
            # Mevcut sayı (num) ile target'ı tamamlayacak sayıyı hesaplıyoruz.
            # Örneğin, target=9 ve num=2 ise, complement=7 olmalıdır.
            complement = target - num
            
            # Hesapladığımız complement'in daha önce seen sözlüğünde olup olmadığını kontrol ediyoruz.
            # Eğer varsa, bu, aradığımız iki sayıyı bulduğumuz anlamına gelir.
            if complement in seen:
                # seen[complement] bize complement sayısının indeksini verir.
                # i ise şu anki num sayısının indeksidir.
                # Bu iki indeksi içeren bir liste döndürüyoruz.
                return [seen[complement], i]
            
            # Eğer complement henüz görülmediyse, şu anki num'ı ve indeksini
            # seen sözlüğüne ekliyoruz. Böylece sonraki sayılar için
            # bu num bir tamamlayıcı olabilir.
            seen[num] = i

```

## Örnek Test Case

**Giriş:**
```
nums = [2,7,11,15]
target = 9
```

**Çalışma Adımları:**

1.  `seen = {}`
2.  **i = 0, num = 2:**
    *   `complement = 9 - 2 = 7`
    *   `7` `seen` içinde değil.
    *   `seen[2] = 0` -> `seen = {2: 0}`
3.  **i = 1, num = 7:**
    *   `complement = 9 - 7 = 2`
    *   `2` `seen` içinde var mı? Evet, `seen[2]` değeri `0`.
    *   `[seen[2], i]` yani `[0, 1]` döndürülür.

**Çıkış:**
```
[0,1]
```

## LeetCode Linki

Bu problemin orijinal LeetCode sayfasına aşağıdaki bağlantıdan ulaşabilirsiniz:

[Two Sum](https://leetcode.com/problems/two-sum/)

## 💻 Programlama Dili

python

---

*Bu README dosyası Universal LeetCode GitHub Sync Tool tarafından otomatik olarak oluşturulmuştur.*