# Longest Common Prefix

## Problem Açıklaması

Bu problem, bir string dizisi (`strs`) verildiğinde, bu dizideki tüm string'ler arasında bulunan en uzun ortak ön eki (longest common prefix) bulmayı amaçlamaktadır. Eğer string'ler arasında ortak bir ön ek yoksa, fonksiyonun boş bir string `""` döndürmesi gerekmektedir.

**Örnek 1:**
```
Girdi: strs = ["flower","flow","flight"]
Çıktı: "fl"
```
**Örnek 2:**
```
Girdi: strs = ["dog","racecar","car"]
Çıktı: ""
Açıklama: Giriş string'leri arasında ortak bir ön ek bulunmamaktadır.
```

**Kısıtlamalar:**
*   `1 <= strs.length <= 200`
*   `0 <= strs[i].length <= 200`
*   `strs[i]` yalnızca küçük İngilizce harflerden oluşur (boş değilse).

## Çözüm Yaklaşımı

Bu problem için "Dikey Tarama" (Vertical Scanning) yaklaşımı benimsenmiştir. Bu yöntem, verilen string dizisindeki ilk string'i referans alarak karakter karakter ilerler. Her bir karakter pozisyonunda, diğer tüm string'lerin aynı karakteri içerip içermediği ve referans string ile eşleşip eşleşmediği kontrol edilir. Bu yaklaşım, basitliği ve doğrudan uygulanabilirliği nedeniyle tercih edilmiştir. Alternatif olarak yatay tarama (horizontal scanning) veya ikili arama (binary search) gibi yaklaşımlar da düşünülebilir, ancak dikey tarama çoğu durumda yeterince verimlidir.

## Algoritma Adımları

Algoritma aşağıdaki adımları takip eder:

1.  **Boş Dizi Kontrolü:** Eğer `strs` dizisi boşsa, ortak ön ek olamayacağından hemen `""` döndürülür.
2.  **Referans String Seçimi:** Dizinin ilk string'i (`strs[0]`) referans olarak alınır. Ortak ön ekin uzunluğu en fazla bu string'in uzunluğu kadar olabilir.
3.  **Karakter Karakter Tarama:** Referans string'in her bir karakteri (`i` indeksi ile) üzerinde döngü başlatılır.
4.  **Diğer String'lerle Karşılaştırma:** Her `i` indeksi için, `strs` dizisindeki diğer tüm string'ler (`strs[1:]`) üzerinde bir iç döngü başlatılır.
5.  **Eşleşme Kontrolü:** İç döngüde, mevcut string (`s`) için iki durum kontrol edilir:
    *   Eğer `i` indeksi, `s` string'inin uzunluğundan büyük veya eşitse (yani `s` string'i `i` pozisyonuna kadar gelmeden bitmişse),
    *   Veya `s[i]` karakteri, referans string'in `strs[0][i]` karakteri ile eşleşmiyorsa,
    bu, ortak ön ekin `i` pozisyonundan önce bittiği anlamına gelir.
6.  **Ön Eki Döndürme:** Yukarıdaki koşullardan herhangi biri doğru olduğunda, ortak ön ek `strs[0]`'ın `0`'dan `i-1`'e kadar olan kısmıdır (`strs[0][:i]`). Bu kısım döndürülür.
7.  **Tam Eşleşme Durumu:** Eğer dış döngü (referans string'in karakterleri üzerindeki döngü) tamamen biterse, bu, referans string'in tamamının diğer tüm string'lerle ortak bir ön ek olduğu anlamına gelir. Bu durumda `strs[0]` döndürülür.

## Karmaşıklık Analizi

### Zaman Karmaşıklığı: O(N * L)

*   `N`, `strs` dizisindeki string sayısıdır.
*   `L`, dizideki en kısa string'in uzunluğudur.

Algoritma, en kötü durumda (tüm string'lerin ortak ön eki çok uzun olduğunda veya tüm string'ler aynı olduğunda), ilk string'in her karakteri için (`L` kez), diğer tüm `N-1` string'i kontrol eder. Her karakter karşılaştırması sabit zamanda (O(1)) gerçekleştiği için, toplam zaman karmaşıklığı `O

## 🔗 LeetCode Linki

[Problem Linki](https://leetcode.com/problems/longest-common-prefix/)

## 💻 Programlama Dili

python

---

*Bu README dosyası Universal LeetCode GitHub Sync Tool tarafından otomatik olarak oluşturulmuştur.*