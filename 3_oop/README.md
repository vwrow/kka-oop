--Analisis 1--

Apa yang terjadi jika kamu mengubah hero1.hp menjadi 500 setelah baris 
hero1 = Hero...? Coba lakukan print(hero1.hp).

Darah Hero1 bertambah menjadi 500


--Analisis 2--

Perhatikan parameter lawan pada method serang. Parameter tersebut 
menerima sebuah objek utuh, bukan hanya string nama. Mengapa ini 
penting?

Jika parameter hanya memanggil nama maka program tidak bisa menampilkan statistika lain


--Analisis 3--

• Eksperimen Fungsi super(): Pada class Mage, coba hapus (atau jadikan 
komentar #) baris kode super().__init__(name, hp, attack_power). Kemudian 
jalankan programnya. 
• Pertanyaan: Error apa yang muncul saat kamu mencoba melihat info Eudora 
(eudora.info())? Mengapa error tersebut mengatakan Mage object has no 
attribute 'name', padahal kita sudah mengirim nama "Eudora" saat 
pembuatan objek? 
• Jelaskan peran fungsi super() dalam menghubungkan data dari class Anak ke 
class Induk! 

Nama tidak terdeteksi memiliki atribute karena super() berfungsi untuk mewariskan data dari class induk sementara tadi super() telah dijadikan comment (#)


--Analisis 4--

• Apakah nilai HP muncul atau Error? Jika muncul, diskusikan dengan temanmy mengapa Python masih mengizinkan akses ini (konsep Name Mangling) 
Python menganut filosofi "we are all consenting adults here". Artinya, Python tidak benar-benar melarang akses, hanya menyamarkan nama atribut agar tidak sengaja diakses.

• Mengapa kita tetap tidak boleh melakukannya dalam standar pemrograman 
yang baik?
Karena tidak etis dan melanggar prinsip OOP.

• Apa yang terjadi pada data HP Hero? Jelaskan mengapa keberadaan method 
Setter sangat penting untuk menjaga integritas data dalam game!
HP Hero akan langsung berubah menjadi -100, Karena setter berfungsi sebagai penjaga data agar sesuai dengan perimeter


--Analisis 5--

• Apa arti pesan error Can't instantiate abstract class Hero with abstract method...?  
Error ini adalah pengingat bahwa kontrak OOP harus dipenuhi sebelum sebuah class bisa digunakan sebagai objek nyata.

• Apa konsekuensinya jika kita lupa membuat method yang sudah dijanjikan di 
Interface?
Class tidak bisa dipakai untuk membuat objek karena Python menolak instansiasi.

• Mengapa class GameUnit dilarang untuk dibuat menjadi objek? Apa gunanya ada class GameUnit jika tidak bisa dibuat menjadi objek nyata?
GameUnit tidak bisa dibuat objek karena ia hanya berisi kontrak abstrak, Gunanya adalah sebagai kerangka dasar agar semua class turunan konsisten, mudah dipelihara, dan mendukung prinsip OOP.


--Analisis 6--

• Apakah program berjalan lancar? Kesimpulannya, apa keuntungan Polimorfisme bagi seorang programmer 
ketika harus mengupdate game dengan karakter baru di masa depan? 
Healer berjalan lancar, bukti polimorfisme memudahkan penambahan fitur tanpa mengubah kode utama.

• Apa yang terjadi? Mengapa dalam konsep Polimorfisme, nama method antara Parent Class dan berbagai Child Class harus persis sama? 
Archer error setelah ganti nama method, bukti bahwa konsistensi nama method adalah syarat agar polimorfisme bekerja.
•

•