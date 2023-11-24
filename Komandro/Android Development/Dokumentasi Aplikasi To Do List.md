---


---

<h1 id="dokumentasi-aplikasi-to-do-list"><strong>Dokumentasi Aplikasi To Do List</strong></h1>
<h1 id="gambaran-umum"><strong>Gambaran Umum</strong></h1>
<p>Aplikasi Flutter ini adalah daftar tugas sederhana yang memungkinkan pengguna menambahkan, mengedit, menghapus, dan melihat detail dari setiap item tugas. Setiap item tugas memiliki tugas, status penyelesaian, dan tanggal. Pengguna juga dapat berbagi item tugas ke media sosial.</p>
<h1 id="berkas-utama-main.dart"><strong>Berkas Utama (main.dart)</strong></h1>
<p><code>main.dart</code> merupakan berkas utama aplikasi yang berisi semua kode program. Dibagi menjadi beberapa bagian utama, berikut penjelasan fungsionalitas masing-masing bagian.</p>
<p><strong>Import Package</strong></p>
<pre><code>import  'package:flutter/material.dart';

import  'package:share/share.dart';
</code></pre>
<p>Bagian ini mengimpor paket Flutter yang diperlukan, yaitu <code>flutter/material.dart</code> untuk komponen UI dan <code>share/share.dart</code> untuk berbagi konten.</p>
<p><strong>Main Function</strong></p>
<pre><code>void  main() {

runApp(MyApp());

}
</code></pre>
<p>Fungsi <code>main</code> menjalankan aplikasi dengan memanggil fungsi <code>runApp</code> dan memberikan instance dari widget <code>MyApp</code> sebagai root widget.</p>
<p><strong>Kelas <code>MyApp</code></strong></p>
<pre><code>class  MyApp  extends  StatelessWidget {

const  MyApp({Key?  key}) :  super(key:  key);

@override

Widget  build(BuildContext  context) {

return  MaterialApp(

debugShowCheckedModeBanner:  false,

home:  TodoListScreen(),

);

}

}
</code></pre>
<p>Kelas ini mewakili aplikasi utama. Berfungsi sebagai root widget yang menjalankan widget <code>TodoListScreen</code> sebagai layar utama.</p>
<p><strong>Kelas <code>TodoListScreen</code></strong></p>
<pre><code>class  TodoListScreen  extends  StatefulWidget {

@override

_TodoListScreenState  createState() =&gt;  _TodoListScreenState();

}
</code></pre>
<p>Kelas ini merupakan widget dengan keadaan yang mewakili layar utama aplikasi. Menampilkan daftar item tugas dan menyediakan fungsionalitas untuk menambah, mengedit, menghapus, dan melihat detail item tugas.</p>
<p><strong>Kelas <code>DetailPage</code></strong></p>
<pre><code>class  DetailPage  extends  StatelessWidget {

final  TodoItem  todoItem;

final  Function(int) onToggle;

DetailPage({required  this.todoItem, required  this.onToggle});
</code></pre>
<p>Kelas ini merupakan widget tanpa keadaan yang menampilkan informasi detail tentang suatu item tugas. Pengguna dapat beralih status penyelesaian dan berbagi item tugas.</p>
<p><strong>Kelas <code>TodoItem</code></strong></p>
<pre><code>class  TodoItem {

'''String  task;

bool  isCompleted;

String  date;

int  index;

TodoItem(

{required  this.task,

required  this.isCompleted,

required  this.date,

required  this.index});

}
</code></pre>
<p>Kelas ini mewakili item tugas dengan tugas, status penyelesaian, tanggal, dan indeks.</p>
<p><strong>Metode Utama (<code>main()</code>)</strong></p>
<pre><code>void  main() {

runApp(MyApp());

}
</code></pre>
<p>Metode utama menjalankan aplikasi dengan membuat instance dari widget <code>MyApp</code> dan menjalankannya menggunakan <code>runApp</code>.</p>
<p><strong>Struktur UI (<code>build</code> Method)</strong></p>
<pre><code>@override

Widget  build(BuildContext  context) {

return  MaterialApp(

debugShowCheckedModeBanner:  false,

home:  TodoListScreen(),

);

}
</code></pre>
<p>Metode <code>build</code> pada kelas <code>MyApp</code> menetapkan struktur UI utama dengan menggunakan widget <code>MaterialApp</code>. Ini menonaktifkan banner debug dan menetapkan <code>TodoListScreen</code> sebagai layar utama.</p>
<p><strong>Kelas <code>TodoListScreen</code> (<code>build</code> Method)</strong></p>
<pre><code>@override

Widget  build(BuildContext  context) {

return  Scaffold(

appBar:  AppBar(

title:  Text('Todo List'),

),

body:  ListView.builder(

itemCount:  todoItems.length,

itemBuilder: (context, index) {

return  ListTile(

title:  Text(

todoItems[index].task,

style:  TextStyle(

decoration:  todoItems[index].isCompleted

?  TextDecoration.lineThrough
:  TextDecoration.none,

),

),

trailing:  Icon(Icons.arrow_forward_ios),

onTap: () {

_showTodoDetail(todoItems[index]);

},

onLongPress: () {

_showOptionsDialog(index);

},

);

},

),

floatingActionButton:  FloatingActionButton(

onPressed: () {

_addTodoItem();

},

child:  Icon(Icons.add),

),

);

}
</code></pre>
<p>Metode <code>build</code> pada kelas <code>TodoListScreen</code> menetapkan struktur UI untuk layar utama. Ini mencakup AppBar, daftar item tugas dalam ListView.builder, dan FloatingActionButton untuk menambahkan item tugas baru.</p>
<p><strong>Fungsi Menambahkan Tugas (<code>_addTodoItem</code> Method)</strong></p>
<pre><code>void  _addTodoItem() {

showDialog(

context:  context,

builder: (BuildContext  context) {

TextEditingController  controller  =  TextEditingController();

return  AlertDialog(

title:  Text('Add Todo Item'),

content:  TextField(

controller:  controller,

onChanged: (text) {

// Handle the input text

},

),

actions: [

TextButton(

onPressed: () {

Navigator.of(context).pop();

},

child:  Text('Cancel'),

),

TextButton(

onPressed: () {

String  task  =  controller.text;

DateTime  now  =  DateTime.now();

String  date  =  "${now.day}/${now.month}/${now.year}";

int  index  =  todoItems.length;

setState(() {

todoItems.add(TodoItem(

task:  task,

isCompleted:  false,

date:  date,

index:  index));

});

Navigator.of(context).pop();

},

child:  Text('Add'),

),

],

);

},

);

}
</code></pre>
<p>Metode ini menampilkan dialog untuk menambahkan tugas baru ketika pengguna menekan tombol tambah.</p>
<p><strong>Fungsi Menampilkan Pilihan (<code>_showOptionsDialog</code> Method)</strong></p>
<pre><code>void  _showOptionsDialog(int  index) {

showDialog(

context:  context,

builder: (BuildContext  context) {

return  AlertDialog(

title:  Text('Options'),

actions: [

TextButton(

onPressed: () {

_editTodoItem(index);

Navigator.of(context).pop();

},

child:  Text('Edit'),

),

TextButton(

onPressed: () {

_deleteTodoItem(index);

Navigator.of(context).pop();

},

child:  Text('Delete'),

),

],

);

},

);

}
</code></pre>
<p>Metode ini menampilkan dialog dengan pilihan edit atau hapus ketika pengguna melakukan tap dan tahan pada item tugas.</p>
<p><strong>Kelas <code>DetailPage</code></strong></p>
<pre><code>@override

Widget  build(BuildContext  context) {

return  Scaffold(

appBar:  AppBar(

title:  Text('Todo Detail'),

actions: [

IconButton(

icon:  Icon(Icons.share),

onPressed: () {

_shareTask(context);

},

),

],

),

body:  Padding(

padding:  const  EdgeInsets.all(16.0),

child:  Column(

crossAxisAlignment:  CrossAxisAlignment.start,

children: [

Row(

mainAxisAlignment:  MainAxisAlignment.spaceBetween,

children: [

Text(

'Task: ${todoItem.task}',

style:  TextStyle(

decoration:  todoItem.isCompleted

?  TextDecoration.lineThrough

:  TextDecoration.none,

),

),

Checkbox(

value:  todoItem.isCompleted,

onChanged: (value) {

onToggle(todoItem.index);

Navigator.pop(context, true);

},

),

],

),

SizedBox(height:  8),

Text(

'Status: ${todoItem.isCompleted ? 'Completed' : 'Incomplete'}',

),

SizedBox(height:  8),

Text(

'Date: ${todoItem.date}',

),

],

),

),

);

}
</code></pre>
<p>Metode <code>build</code> pada kelas <code>DetailPage</code> menetapkan struktur UI untuk halaman detail item tugas. Ini mencakup informasi seperti tugas, status penyelesaian, dan tanggal. Juga menambahkan ikon berbagi untuk berbagi item tugas.</p>
<p><strong>Fungsi Berbagi Tugas (<code>_shareTask</code> )</strong></p>
<pre><code>void  _shareTask(BuildContext  context) {

// Implementasi berbagi task ke media sosial

String  taskText  =

'Task: ${todoItem.task}\nStatus: ${todoItem.isCompleted ? 'Completed' : 'Incomplete'}\nDate: ${todoItem.date}';

Share.share(taskText);

}

Metode ini mengimplementasikan berbagi item tugas ke media sosial menggunakan paket `share`.

**Fungsi merubah To Do Item ( `_editTodoItem`)**

void  _editTodoItem(int  index) {

showDialog(

context:  context,

builder: (BuildContext  context) {

TextEditingController  controller  =

TextEditingController(text:  todoItems[index].task);

return  AlertDialog(

title:  Text('Edit Todo Item'),

content:  TextField(

controller:  controller,

onChanged: (text) {

// Handle the input text

},

),

actions: [

TextButton(

onPressed: () {

Navigator.of(context).pop();

},

child:  Text('Cancel'),

),

TextButton(

onPressed: () {

setState(() {

todoItems[index].task  =  controller.text;

});

Navigator.of(context).pop();

},

child:  Text('Save'),

),

],

);

},

);

}
</code></pre>
<p>Metode ini digunakan untuk menampilkan dialog pengeditan item tugas ketika pengguna memilih untuk mengedit suatu item pada daftar tugas.</p>
<p><strong>Fungsi menghapus To Do Item( <code>_deleteTodoItem</code>)</strong></p>
<pre><code>void  _deleteTodoItem(int  index) {

setState(() {

todoItems.removeAt(index);

});

}
</code></pre>
<p>Metode ini digunakan untuk menghapus item tugas dari daftar tugas.</p>
<p><strong>Metode _toggleTodoItem(int index)</strong></p>
<pre><code>void  _toggleTodoItem(int  index) {

setState(() {

todoItems[index].isCompleted  =  !todoItems[index].isCompleted;

});

}
</code></pre>
<p>Metode ini digunakan untuk mengalihkan status penyelesaian (completed) dari suatu item tugas. Ini akan mengubah status penyelesaian item tugas yang dipilih. Jika status semula true, maka akan diubah menjadi false, dan sebaliknya.</p>
<h1 id="penggunaan"><strong>Penggunaan</strong></h1>
<ol>
<li>
<p>Jalankan aplikasi dengan menjalankan <code>main.dart</code>.</p>
</li>
<li>
<p>Lihat dan kelola item tugas pada layar utama.</p>
</li>
<li>
<p>Ketuk pada item tugas untuk melihat informasi detail.</p>
</li>
<li>
<p>Edit, hapus, atau alihkan status penyelesaian dari halaman detail.</p>
</li>
<li>
<p>Bagikan item tugas menggunakan ikon berbagi pada halaman detail.</p>
</li>
</ol>

