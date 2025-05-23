import 'package:flutter/material.dart';

void main() {
  runApp(const VocalizeApp());
}

class VocalizeApp extends StatelessWidget {
  const VocalizeApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Vocalize App',
      home: const Scaffold(
        body: Center(
          child: Text('Vocalize App - Coming Soon!'),
        ),
      ),
    );
  }
} 