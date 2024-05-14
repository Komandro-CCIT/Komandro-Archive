
# JavaScript Basics   
  
  

Author : M.Fauzan Arrafi  
  

---  
  

![](https://it.telkomuniversity.ac.id/wp-content/uploads/2023/01/Javascript-adalah-1.jpg)  
  
  

## Introduction   
  


JavaScript adalah bahasa pemrograman yang sangat populer dan serbaguna yang terutama digunakan untuk pengembangan web. Kemampuannya untuk menambahkan perilaku dinamis dan interaktif ke halaman web telah menjadikannya dasar pengembangan web modern. Dalam tutorial komprehensif ini, kita akan menjelajahi dasar-dasar JavaScript, memberikan kita pengetahuan untuk membuat aplikasi web yang kuat dan menarik.

JavaScript, sering disingkat sebagai JS, dibuat oleh Brendan Eich pada tahun 1995 dengan tujuan utama untuk meningkatkan pengalaman pengguna di web. Ini adalah bahasa pemrograman tingkat tinggi yang diinterpretasikan langsung di browser, memungkinkan scripting di sisi klien. Seiring waktu, JavaScript telah berkembang menjadi bahasa multiparadigma, mendukung gaya pemrograman imperatif, fungsional, dan berbasis objek.

JavaScript memberdayakan pengembang web untuk membangun halaman web yang dinamis dan interaktif yang merespons tindakan pengguna secara real-time. Dengan JavaScript, kalian dapat memanipulasi Model Objek Dokumen (DOM) untuk mengubah elemen-elemen HTML, mengubah style, menangani event, memvalidasi input formulir, melakukan perhitungan, dan mengambil data dari server secara asinkron. Kemungkinannya hampir tanpa batas.
  

## Basic Syntax  

Memahami syntax dasar JavaScript sangat penting untuk menulis kode yang efektif. Kita akan menjelajahi struktur program JavaScript, termasuk deklarasi variabel, operator, fungsi, kondisional, dan perulangan. kalian akan belajar tentang tipe data bawaan JavaScript, seperti angka, string, boolean, array, objek, null, dan undefined. Kita akan membahas bagaimana cara bekerja dengan tipe data ini dan melakukan operasi pada mereka.

Kode JavaScript biasanya disisipkan dalam dokumen HTML menggunakan tag `<script>`. Atau, kode tersebut dapat ditulis dalam file terpisah dengan ekstensi `.js` dan dihubungkan dengan dokumen HTML.
  

```javascript  
// Example of a basic JavaScript function  
function greet(name) {  
  console.log("Hello, " + name + "!");  
}  
```  
  

## Data Types  
  

JavaScript mendukung berbagai jenis tipe data, termasuk:
  

- **Number**: Mewakili nilai numerik.
- **String**: Mewakili data teks.
- **Boolean**: Mewakili nilai `true` atau `false`.
- **Array**: Mewakili kumpulan nilai yang terurut.
- **Object**: Mewakili kumpulan pasangan kunci-nilai.
- **Null**: Mewakili ketiadaan nilai apapun.
- **Undefined**: Mewakili variabel yang belum diinisialisasi.
  

## Control Structures  
  

JavaScript menyediakan struktur kontrol yang kuat untuk mengatur alur program dan menjalankan kode berdasarkan kondisi-kondisi tertentu.
  

### Conditional Statements  
  

Conditional statements memungkinkan kita menjalankan blok kode yang berbeda berdasarkan kondisi-kondisi tertentu. JavaScript menyediakan pernyataan kondisional berikut: 
  

- **if statement**: Pernyataan `if` memungkinkan kita menjalankan blok kode jika kondisi tertentu adalah benar.
  

```javascript  
if (condition) {  
  // Code to be executed if the condition is true  
}  
```  
  

- **else statement**: Pernyataan `else` digunakan bersama dengan pernyataan `if` dan memungkinkan kita untuk menentukan blok kode yang akan dieksekusi jika kondisinya adalah salah (false).
  

```javascript  
if (condition) {  
  // Code to be executed if the condition is true  
} else {  
  // Code to be executed if the condition is false  
}  
```  
  

- **else if statement**: Pernyataan `else if` memungkinkan kita untuk memeriksa kondisi tambahan jika kondisi sebelumnya adalah salah `false`. Pernyataan ini dapat diantrekan beberapa kali.
  

```javascript  
if (condition1) {  
  // Code to be executed if condition1 is true  
} else if (condition2) {  
  // Code to be executed if condition1 is false and condition2 is true  
} else {  
  // Code to be executed if both condition1 and condition2 are false  
}  
```  
  

## Loop
  

Loop memungkinkan kita untuk mengulang blok kode beberapa kali hingga kondisi tertentu terpenuhi. JavaScript menyediakan struktur perulangan berikut:  


- **for loop**: Pengulangan `for` digunakan ketika kalian sudah mengetahui sebelumnya jumlah iterasi yang ingin kalian lakukan.  
  

```javascript  
for (initialization; condition; iteration) {  
  // Code to be executed in each iteration  
}  
```  
  

- **while loop**: Pernyataan `while` digunakan ketika jumlah iterasi tidak diketahui sebelumnya tetapi bergantung pada kondisi tertentu.
  

```javascript  
while (condition) {  
  // Code to be executed while the condition is true  
}  
```  
  

- **do-while loop**: Pernyataan `do-while` mirip dengan perulangan `while`, tetapi menjamin bahwa blok kode dieksekusi setidaknya sekali sebelum memeriksa kondisi.
  

```javascript  
do {  
  // Code to be executed at least once  
} while (condition);  
```  
  

Struktur kontrol ini memberikan fleksibilitas dan pengendalian terhadap alur program JavaScript kalian. Dengan memanfaatkan pernyataan kondisional dan perulangan secara efektif, kalian dapat menciptakan aplikasi yang dinamis dan responsif.
  

## Functions  
  

Fungsi adalah blok kode yang dapat digunakan kembali yang melakukan tugas-tugas tertentu. Mereka dapat menerima parameter dan mengembalikan nilai.
  

```javascript  
// Function with default parameters  
function greet(name = "Anonymous") {  
  console.log("Hello, " + name + "!");  
}  
  
greet(); // Output: Hello, Anonymous!  
greet("John"); // Output: Hello, John!  
```  
  

Dalam contoh ini, fungsi `greet` memiliki parameter default untuk `name` yang diatur sebagai "Anonymous". Jika tidak ada argumen yang diberikan, itu akan menggunakan nilai default tersebut.
  

### Anonymous Function:  
  

```javascript  
// Anonymous function assigned to a variable  
const sayHello = function() {  
  console.log("Hello!");  
};  
  
sayHello(); // Output: Hello!  
```  
  

Fungsi anonim adalah fungsi tanpa nama. Mereka dapat ditetapkan ke variabel dan dipanggil sama seperti fungsi bernama.  
  

### Arrow Function:  
  

```javascript  
// Arrow function  
const multiply = (a, b) => a * b;  
  
console.log(multiply(2, 3)); // Output: 6  
```  
  

Arrow functions menyediakan syntax yang ringkas untuk menulis fungsi. Mereka sangat berguna untuk menulis fungsi satu baris.
  

### Higher-Order Function:  
  

```javascript  
// Higher-order function  
function calculate(operation, a, b) {  
  return operation(a, b);  
}  
  
function add(a, b) {  
  return a + b;  
}  
  
console.log(calculate(add, 2, 3)); // Output: 5  
```  
  

Fungsi orde tinggi (higher-order functions) adalah fungsi yang menerima fungsi lain sebagai argumen atau mengembalikan fungsi sebagai hasil. Dalam contoh ini, `calculate` adalah fungsi berorde tinggi yang mengambil fungsi operasi sebagai parameter.
  

### Recursive Function:  
  

```javascript  
// Recursive function to calculate factorial  
function factorial(n) {  
  if (n === 0) {  
    return 1;  
  }  
  return n * factorial(n - 1);  
}  
  
console.log(factorial(5)); // Output: 120  
```  
  

Fungsi rekursif adalah fungsi yang memanggil dirinya sendiri. Dalam contoh ini, fungsi `factorial` menghitung faktorial suatu bilangan menggunakan rekursi.

Ini hanya beberapa variasi dan jenis fungsi dalam JavaScript. Fungsi sangat kuat dan serbaguna, memungkinkan kalian menulis kode yang modular dan dapat digunakan kembali.
  

## DOM Manipulation  
  

Integrasi JavaScript dengan Document Object Model (DOM) memungkinkan kalian memanipulasi dan berinteraksi dengan elemen HTML secara dinamis. Kami akan membahas cara memilih dan mengubah elemen, membuat elemen baru, menangani event, dan menjelajahi struktur DOM. kalian akan memperoleh keterampilan untuk membuat formulir interaktif, membangun menu responsif, dan mengimplementasikan animasi yang halus.
  

![](https://miro.medium.com/v2/resize:fit:1120/0*dcpjTwj_qSjTdaUc.jpg)  
  

JavaScript memungkinkan manipulasi dari Document Object Model (DOM) untuk secara dinamis mengubah elemen-elemen HTML dan properti-propertinya.
  
  

###  **Selecting and Modifying Elements**:  
  

```javascript  
// Selecting an element by its ID and changing its text content  
const heading = document.getElementById("myHeading");  
heading.textContent = "New Heading";  
  
// Selecting elements by class name and modifying their styles  
const paragraphs = document.getElementsByClassName("myParagraph");  
for (let i = 0; i < paragraphs.length; i++) {  
  paragraphs[i].style.color = "blue";  
}  
```  
  
Dalam contoh ini, kita memilih elemen dengan ID "myHeading" dan mengubah konten teksnya. Kemudian, kita memilih elemen-elemen dengan nama kelas "myParagraph" dan mengubah gaya mereka dengan mengubah warnanya.

  

###  **Creating and Appending New Elements**:  
  

```javascript  
// Creating a new paragraph element and appending it to an existing div  
const newParagraph = document.createElement("p");  
newParagraph.textContent = "This is a new paragraph.";  
const existingDiv = document.getElementById("myDiv");  
existingDiv.appendChild(newParagraph);  
```  
  

Di sini, kita membuat elemen baru `<p>`, mengatur konten teksnya, dan kemudian menambahkannya ke elemen `<div>` yang sudah ada dengan ID "myDiv".
  

###  **Handling Events**:  
  

```javascript  
// Adding an event listener to a button element  
const myButton = document.getElementById("myButton");  
myButton.addEventListener("click", function() {  
  alert("Button clicked!");  
});  
```  
  
  
Dalam contoh ini, kita menambahkan pendengar acara (event listener) ke elemen tombol dengan ID "myButton". Ketika tombol diklik, akan ditampilkan pesan peringatan (alert) "Button clicked!".


###  **Traversing the DOM Tree**:  
  

```javascript  
// Accessing child elements and modifying their properties  
const parentElement = document.getElementById("parent");  
const childElements = parentElement.children;  
for (let i = 0; i < childElements.length; i++) {  
  const child = childElements[i];  
  child.textContent = "Modified";  
}  
```  
  

Di sini, kita memilih elemen induk dengan ID "parent" dan mengakses elemen-elemennya. Kemudian, kita melakukan perulangan melalui elemen-elemen anak tersebut dan mengubah konten teks mereka.

Ini hanya beberapa contoh bagaimana kalian dapat memanipulasi DOM menggunakan JavaScript. Dengan manipulasi DOM, kalian dapat secara dinamis memperbarui konten, tampilan, dan perilaku halaman web kalian, memungkinkan kalian membuat formulir interaktif, menu responsif, animasi, dan banyak lagi. DOM menyediakan antarmuka yang kuat bagi JavaScript untuk berinteraksi dengan elemen-elemen HTML dan menghidupkan aplikasi web kalian.
  

## Event Handling  
  

JavaScript memungkinkan penanganan acara (event handling) untuk merespons interaksi pengguna atau acara lainnya pada halaman web. 
  

###  **Handling Form Submission**:  
  

```javascript  
// Handling form submission event  
const form = document.getElementById("myForm");  
form.addEventListener("submit", function(event) {  
  event.preventDefault(); // Prevent form submission  
  const input = document.getElementById("myInput");  
  console.log("Input value: " + input.value);  
});  
```  
  

Dalam contoh ini, kita menangani acara pengiriman formulir (form submission) dan mencegah perilaku pengiriman formulir default. Kemudian, kita mengakses elemen input dan mencatat nilainya ke konsol. 
  

###  **Handling Mouse Events**:  
  

```javascript  
// Handling mouse over and mouse out events  
const element = document.getElementById("myElement");  
element.addEventListener("mouseover", function() {  
  console.log("Mouse over!");  
});  
  
element.addEventListener("mouseout", function() {  
  console.log("Mouse out!");  
});  
```  
  

Di sini, kita menangani acara mouse over dan mouse out pada elemen dengan ID "myElement". Ketika kursor mouse masuk atau keluar dari elemen tersebut, fungsi penangan acara yang sesuai akan dijalankan, dan pesan akan dicatat ke konsol.
  

###  **Handling Keyboard Events**:  
  

```javascript  
// Handling keydown event  
document.addEventListener("keydown", function(event) {  
  console.log("Key pressed: " + event.key);  
});  
```  
  

Dalam contoh ini, kita menangani acara keydown pada seluruh dokumen. Ketika tombol apa pun ditekan, fungsi penangan acara akan mencatat tombol yang ditekan ke konsol. 
  

###  **Handling Window Resize Event**:  
  

```javascript  
// Handling window resize event  
window.addEventListener("resize", function() {  
  console.log("Window resized!");  
});  
```  
  


Di sini, kita menangani event resize pada jendela (window). Setiap kali pengguna mengubah ukuran jendela browser, fungsi penangan event akan dijalankan dan mencatat pesan ke konsol.

Penanganan event (event handling) dalam JavaScript memungkinkan kalian merespons interaksi pengguna dan event lainnya pada halaman web. Dengan melekatkan pendengar event (event listener) pada elemen-elemen atau jendela, kalian dapat menjalankan kode tertentu atau melakukan tindakan berdasarkan berbagai acara yang terjadi dalam aplikasi web kalian. Jangan ragu untuk menjelajahi jenis acara lainnya dan bereksperimen dengan skenario penanganan acara yang berbeda untuk meningkatkan pemahaman kalian tentang penanganan acara dalam JavaScript.
  

## Error Handling  
  


JavaScript menyediakan struktur kontrol aliran program, seperti pernyataan if-else, pernyataan switch, dan perulangan, untuk mengontrol aliran eksekusi program. Kita akan mempelajari secara mendalam konstruksi-konstruksi tersebut dan mengeksplorasi bagaimana membuat keputusan dan mengulangi kode berdasarkan kondisi-kondisi tertentu. Selain itu, kita akan membahas teknik penanganan kesalahan menggunakan blok try-catch untuk menangani pengecualian dengan baik dan mencegah terjadinya kegagalan program.

JavaScript menyediakan mekanisme penanganan kesalahan untuk menangkap dan menangani pengecualian yang mungkin terjadi selama eksekusi program.
  

```javascript  
// Example of try-catch block for error handling  
try {  
  // Code that may throw an error  
  throw new Error("Something went wrong!");  
} catch (error) {  
  console.error("An error occurred:", error);  
}  
```  
  

## Object-Oriented Programming  
  

JavaScript mendukung konsep pemrograman berorientasi objek (OOP) seperti kelas, objek, inheritance, dan enkapsulasi. Kita akan membahas pembuatan kelas, instansiasi objek, definisi metode, dan penggunaan prototipe. Memahami OOP dalam JavaScript akan memungkinkan kalian membangun kode yang modular dan mudah dipelihara.
  

![](https://res.cloudinary.com/practicaldev/image/fetch/s--2026kdwz--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/59nlnyqioosaowj09xn8.gif)  
  

JavaScript mendukung konsep pemrograman berorientasi objek seperti class, object, dan inheritance.
  

```javascript  
// Example of class and object instantiation  
class Person {  
  constructor(name, age) {  
    this.name = name;  
    this.age = age;  
  }  
  
  greet() {  
    console.log("Hello, my name is " + this.name);  
  }  
}  
  
let person = new Person("John", 30);  
person.greet();  
```  
  

## Asynchronous Programming  
  

Aplikasi web modern sering kali membutuhkan pengambilan data dari server atau melakukan panggilan API. JavaScript asinkron memungkinkan kita melakukan operasi-operasi ini tanpa menghalangi antarmuka pengguna. Kita akan menjelajahi fungsi callback, promise, dan syntax async/await yang lebih baru untuk menangani operasi-asinkron dengan efektif. kalian akan belajar bagaimana melakukan permintaan HTTP, memproses respons, dan memperbarui antarmuka pengguna sesuai dengan itu.
  

![](https://res.cloudinary.com/practicaldev/image/fetch/s--wN7yFTnt--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/9wqej2269vmntfcuxs9t.gif)  
  

JavaScript memungkinkan pemrograman asinkron menggunakan promise dan syntax async/await untuk menangani operasi yang membutuhkan waktu, seperti pengambilan data dari sebuah API.
  

```javascript  
// Example of asynchronous function using async/await  
async function fetchData() {  
  try {  
    const response = await fetch('https://api.example.com/data');  
    const data = await response.json();  
    console.log(data);  
  } catch (error) {  
    console.error("Failed to fetch data:", error);  
  }  
}  
```  
  

## Frameworks and Libraries  
  
JavaScript memiliki ekosistem yang luas dari pustaka (libraries) dan kerangka kerja (frameworks) yang dapat secara signifikan mempercepat pengembangan web. Kami akan memperkenalkan kalian pada kerangka kerja populer seperti React, Angular, dan Vue.js. kalian akan belajar bagaimana memanfaatkan kerangka kerja ini untuk membuat aplikasi web yang kompleks dan dapat diskalakan.