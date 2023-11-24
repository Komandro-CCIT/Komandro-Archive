import 'package:flutter/material.dart';
import 'package:share/share.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: TodoListScreen(),
    );
  }
}

class TodoListScreen extends StatefulWidget {
  @override
  _TodoListScreenState createState() => _TodoListScreenState();
}

class _TodoListScreenState extends State<TodoListScreen> {
  List<TodoItem> todoItems = [];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        
        title: Text('Todo List'),
      ),
      body: ListView.builder(
        itemCount: todoItems.length,
        itemBuilder: (context, index) {
          return ListTile(
            title: Text(
              todoItems[index].task,
              style: TextStyle(
                decoration: todoItems[index].isCompleted
                    ? TextDecoration.lineThrough
                    : TextDecoration.none,
              ),
            ),
            trailing: Icon(Icons.arrow_forward_ios),
            onTap: () {
              _showTodoDetail(todoItems[index]);
            },
            onLongPress: () {
              _showOptionsDialog(index);
            },
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          _addTodoItem();
        },
        child: Icon(Icons.add),
      ),
    );
  }

  void _addTodoItem() {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        TextEditingController controller = TextEditingController();

        return AlertDialog(
          title: Text('Add Todo Item'),
          content: TextField(
            controller: controller,
            onChanged: (text) {
              // Handle the input text
            },
          ),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.of(context).pop();
              },
              child: Text('Cancel'),
            ),
            TextButton(
              onPressed: () {
                String task = controller.text;
                DateTime now = DateTime.now();
                String date = "${now.day}/${now.month}/${now.year}";
                int index = todoItems.length;
                setState(() {
                  todoItems.add(TodoItem(
                      task: task,
                      isCompleted: false,
                      date: date,
                      index: index));
                });
                Navigator.of(context).pop();
              },
              child: Text('Add'),
            ),
          ],
        );
      },
    );
  }

  void _editTodoItem(int index) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        TextEditingController controller =
            TextEditingController(text: todoItems[index].task);

        return AlertDialog(
          title: Text('Edit Todo Item'),
          content: TextField(
            controller: controller,
            onChanged: (text) {
              // Handle the input text
            },
          ),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.of(context).pop();
              },
              child: Text('Cancel'),
            ),
            TextButton(
              onPressed: () {
                setState(() {
                  todoItems[index].task = controller.text;
                });
                Navigator.of(context).pop();
              },
              child: Text('Save'),
            ),
          ],
        );
      },
    );
  }

  void _deleteTodoItem(int index) {
    setState(() {
      todoItems.removeAt(index);
    });
  }

  void _toggleTodoItem(int index) {
    setState(() {
      todoItems[index].isCompleted = !todoItems[index].isCompleted;
    });
  }

  void _showOptionsDialog(int index) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('Options'),
          actions: [
            TextButton(
              onPressed: () {
                _editTodoItem(index);
                Navigator.of(context).pop();
              },
              child: Text('Edit'),
            ),
            TextButton(
              onPressed: () {
                _deleteTodoItem(index);
                Navigator.of(context).pop();
              },
              child: Text('Delete'),
            ),
          ],
        );
      },
    );
  }

  void _showTodoDetail(TodoItem todoItem) {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) =>
            DetailPage(todoItem: todoItem, onToggle: _toggleTodoItem),
      ),
    ).then((result) {
      if (result != null && result is bool && result) {
        _refreshTodoList();
      }
    });
  }

  void _refreshTodoList() {
    setState(() {
      // Memanggil setState untuk memperbarui tampilan daftar.
    });
  }
}

class DetailPage extends StatelessWidget {
  final TodoItem todoItem;
  final Function(int) onToggle;

  DetailPage({required this.todoItem, required this.onToggle});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Todo Detail'),
        actions: [
          IconButton(
            icon: Icon(Icons.share),
            onPressed: () {
              _shareTask(context);
            },
          ),
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text(
                  'Task: ${todoItem.task}',
                  style: TextStyle(
                    decoration: todoItem.isCompleted
                        ? TextDecoration.lineThrough
                        : TextDecoration.none,
                  ),
                ),
                Checkbox(
                  value: todoItem.isCompleted,
                  onChanged: (value) {
                    onToggle(todoItem.index);
                    Navigator.pop(context, true);
                  },
                ),
              ],
            ),
            SizedBox(height: 8),
            Text(
              'Status: ${todoItem.isCompleted ? 'Completed' : 'Incomplete'}',
            ),
            SizedBox(height: 8),
            Text(
              'Date: ${todoItem.date}',
            ),
          ],
        ),
      ),
    );
  }

  void _shareTask(BuildContext context) {
    // Implementasi berbagi task ke media sosial
    String taskText =
        'Task: ${todoItem.task}\nStatus: ${todoItem.isCompleted ? 'Completed' : 'Incomplete'}\nDate: ${todoItem.date}';

    Share.share(taskText);
  }
}

class TodoItem {
  String task;
  bool isCompleted;
  String date;
  int index;

  TodoItem(
      {required this.task,
      required this.isCompleted,
      required this.date,
      required this.index});
}