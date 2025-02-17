
# JavaScript Crash Course for Beginners

## Day 1: Basics of JavaScript

### 1. Introduction to JavaScript

JavaScript is a programming language that is used to create dynamic and interactive effects within web browsers. It is essential for web development alongside HTML and CSS.

### 2. Basic Syntax

- **Variables**  
  Variables store data values. You can declare them using `var`, `let`, or `const`.

  ```javascript
  let name = "John";  // Using let
  const age = 25;     // Using const
  var location = "New York"; // Using var
  ```

  - Variables declared with `let` can be reassigned, but `const` cannot be.
  - `var` is older and has function scope, unlike `let` and `const` which have block scope.

- **Data Types**  
  JavaScript has several data types:
  - **String**: Textual data
  - **Number**: Numeric values
  - **Boolean**: True or false
  - **Object**: Collection of key-value pairs
  - **Array**: List-like objects

  ```javascript
  let name = "Alice";  // String
  let age = 30;         // Number
  let isStudent = true; // Boolean
  let user = { name: "Alice", age: 30 }; // Object
  let colors = ["red", "green", "blue"]; // Array
  ```

  ```javascript
  let isAvailable = false; // Boolean
  let person = { name: "Jane", age: 25 }; // Object
  let nums = [1, 2, 3, 4]; // Array
  ```

  ```javascript
  let score = 95;   // Number
  let city = "Paris"; // String
  ```

### 3. Operators

- **Arithmetic Operators**: `+`, `-`, `*`, `/`, `%`
- **Comparison Operators**: `==`, `===`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical Operators**: `&&`, `||`, `!`

```javascript
let sum = 10 + 5;   // Addition
let difference = 10 - 5; // Subtraction
let isEqual = (10 === 10);  // Strict comparison (checks value and type)
let remainder = 10 % 3; // Modulus, returns remainder of division
```

```javascript
let x = 5;
let y = 10;
let comparison = (x > y);  // Returns false

let a = true;
let b = false;
let result = (a && b);  // Returns false
```

```javascript
let x = 20;
let y = 30;
let result = (x !== y);  // Returns true
```

### 4. Functions

A function is a block of code designed to perform a task. You can call it whenever needed.

```javascript
function greet(name) {
  return "Hello, " + name;
}

console.log(greet("Alice")); // Outputs: "Hello, Alice"
```

```javascript
function add(a, b) {
  return a + b;
}
console.log(add(5, 7));  // Outputs: 12
```

```javascript
function square(num) {
  return num * num;
}

console.log(square(4)); // Outputs: 16
```

### 5. Conditionals (if-else)

You can control the flow of your program using `if`, `else if`, and `else`.

```javascript
let score = 85;
if (score > 90) {
  console.log("Grade A");
} else if (score > 75) {
  console.log("Grade B");
} else {
  console.log("Grade C");
}
```

```javascript
let age = 18;
if (age >= 18) {
  console.log("You can vote.");
} else {
  console.log("You cannot vote.");
}
```

```javascript
let temperature = 30;
if (temperature > 25) {
  console.log("It's a hot day!");
} else {
  console.log("It's a cool day.");
}
```

### 6. Loops

Loops are used to run a block of code multiple times.

- **for loop**: Executes a block of code a set number of times.

  ```javascript
  for (let i = 0; i < 5; i++) {
    console.log(i);  // Outputs: 0, 1, 2, 3, 4
  }
  ```

  ```javascript
  for (let i = 0; i <= 10; i += 2) {
    console.log(i);  // Outputs: 0, 2, 4, 6, 8, 10
  }
  ```

  ```javascript
  for (let i = 1; i <= 5; i++) {
    console.log(i * i);  // Outputs: 1, 4, 9, 16, 25
  }
  ```

- **while loop**: Executes a block of code while a condition is true.

  ```javascript
  let count = 0;
  while (count < 5) {
    console.log(count);
    count++;
  }
  ```

  ```javascript
  let num = 1;
  while (num <= 10) {
    console.log(num);
    num += 2;
  }
  ```

  ```javascript
  let i = 0;
  while (i < 5) {
    console.log("Hello, World!");
    i++;
  }
  ```

---

## Day 2: Intermediate Concepts and Mini-Project

### 7. Arrays and Objects

- **Array Methods**: Arrays have built-in methods to manipulate them.  
  Examples: `push()`, `pop()`, `shift()`, `unshift()`, `forEach()`

  ```javascript
  let fruits = ["apple", "banana", "cherry"];
  fruits.push("orange"); // Adds to the end
  console.log(fruits);
  ```

  ```javascript
  let numbers = [1, 2, 3];
  numbers.pop(); // Removes the last element
  console.log(numbers);
  ```

  ```javascript
  let colors = ["red", "green", "blue"];
  colors.shift(); // Removes the first element
  console.log(colors);
  ```

- **Object Methods**: Objects can have methods (functions inside objects).

  ```javascript
  let person = {
    name: "John",
    age: 30,
    greet: function() {
      console.log("Hello, " + this.name);
    }
  };

  person.greet();  // Outputs: "Hello, John"
  ```

  ```javascript
  let car = {
    brand: "Toyota",
    model: "Corolla",
    startEngine: function() {
      console.log("The engine has started.");
    }
  };

  car.startEngine();  // Outputs: "The engine has started."
  ```

  ```javascript
  let student = {
    name: "Alice",
    grade: "A",
    sayGrade: function() {
      console.log(this.name + " has grade: " + this.grade);
    }
  };

  student.sayGrade();  // Outputs: "Alice has grade: A"
  ```

### 8. DOM Manipulation

The **Document Object Model (DOM)** is a representation of the HTML structure. You can manipulate HTML elements using JavaScript.

```javascript
// Changing text content
document.getElementById("myElement").textContent = "New Text";
```

```javascript
// Changing background color
document.body.style.backgroundColor = "lightblue";
```

```javascript
// Changing style
document.getElementById("myElement").style.color = "red";
```

### 9. Events

Events are actions that happen in the browser (like clicks, key presses, etc.).

```javascript
document.getElementById("myButton").addEventListener("click", function() {
  alert("Button clicked!");
});
```

```javascript
document.getElementById("hoverButton").addEventListener("mouseover", function() {
  alert("Mouse is over the button!");
});
```

```javascript
let inputField = document.getElementById("textInput");
inputField.addEventListener("change", function() {
  console.log("Input field value changed!");
});
```

### 10. Introduction to ES6 (Modern JavaScript)

- **Arrow Functions**: A more concise way to write functions.

  ```javascript
  const greet = (name) => `Hello, ${name}`;
  console.log(greet("Alice"));
  ```

  ```javascript
  const add = (a, b) => a + b;
  console.log(add(5, 7));  // Outputs: 12
  ```

  ```javascript
  const double = (num) => num * 2;
  console.log(double(4));  // Outputs: 8
  ```

- **Template Literals**: Allows embedding expressions inside strings.

  ```javascript
  let age = 25;
  let message = `I am ${age} years old.`;
  console.log(message);
  ```

  ```javascript
  let firstName = "John";
  let lastName = "Doe";
  let fullName = `My name is ${firstName} ${lastName}`;
  console.log(fullName);
  ```

  ```javascript
  let product = "Laptop";
  let price = 1000;
  let message = `The price of the ${product} is $${price}.`;
  console.log(message);
  ```

---

## Mini-Project: Build a Responsive Navbar

### HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Responsive Navbar</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <nav>
      <ul id="navbar">
        <li><a href="#">Home</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Services</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
      <button id="menu-btn">☰</button>
    </nav>
  </header>
  
  <script src="script.js"></script>
</body>
</html>
```

### CSS

```css
body {
  font-family: Arial, sans-serif;
}

header {
  background-color: #333;
}

nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
}

ul {
  list-style: none;
  display: flex;
}

li {
  margin-right: 20px;
}

a {
  color: white;
  text-decoration: none;
}

#menu-btn {
  display: none;
}

@media (max-width: 600px) {
  ul {
    display: none;
    flex-direction: column;
    width: 100%;
  }

  #menu-btn {
    display: block;
    background-color: #333;
    color: white;
    border: none;
    padding: 10px;
    font-size: 20px;
  }

  ul.show {
    display: block;
  }
}
```

### JavaScript

```javascript
const menuBtn = document.getElementById("menu-btn");
const navbar = document.getElementById("navbar");

menuBtn.addEventListener("click", () => {
  navbar.classList.toggle("show");
});
```

---

## **Wrap-Up**

### What You've Learned:
- Basic and intermediate JavaScript concepts (variables, functions, DOM manipulation, etc.)
- How to create a simple responsive navbar using HTML, CSS, and JavaScript.

### Challenge:
- Customize the navbar further and add features like smooth scrolling or dropdown menus.
