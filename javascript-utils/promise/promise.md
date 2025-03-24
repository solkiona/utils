# JavaScript Promises, Fetch API, and Async/Await

## 1. Promises
A **Promise** is an object representing the eventual completion or failure of an asynchronous operation.

### Why Promises?
In JavaScript, operations like network requests or file reading are asynchronous. Promises help avoid callback hell and provide better code structure.

### Promise States:
- **Pending**: Initial state, neither fulfilled nor rejected.
- **Fulfilled**: Operation completed successfully.
- **Rejected**: Operation failed.

### Creating a Promise
A promise is created using the `Promise` constructor, which accepts a function (executor function) with two parameters: `resolve` and `reject`.
```javascript
let promise = new Promise((resolve, reject) => {
  let success = true; // Simulating success or failure

  if (success) {
    resolve("Operation Successful"); // Moves to 'fulfilled' state
  } else {
    reject("Operation Failed"); // Moves to 'rejected' state
  }
});
```

### Handling Promises with `.then()` and `.catch()`
A promise object has methods that allow handling of results:
- `.then(callback)`: Executes when the promise is resolved (fulfilled).
- `.catch(callback)`: Executes when the promise is rejected (failed).
- `.finally(callback)`: Executes after promise completion (fulfilled or rejected).

```javascript
promise.then(result => {
  console.log(result); // "Operation Successful"
}).catch(error => {
  console.log(error); // "Operation Failed"
}).finally(() => {
  console.log("Operation Completed");
});
```

### Real-World Scenario
Imagine you're fetching user data from an API, but before using `fetch()`, let’s simulate it with a promise:
```javascript
function fetchUserData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      let user = { name: "John Doe", age: 30 };
      resolve(user); // Simulating successful data retrieval
    }, 2000);
  });
}

fetchUserData().then(user => console.log(user));
```

---

## 2. Fetch API
The **Fetch API** is used to make HTTP requests and returns a promise.

### Syntax
```javascript
fetch(url, options)
  .then(response => response.json()) // First .then() extracts JSON data
  .then(data => console.log(data))  // Second .then() handles extracted data
  .catch(error => console.error("Error:", error));
```

### Understanding Fetch Step by Step
1. **`fetch(url)` returns a promise** that resolves with a `Response` object.
2. **First `.then(response => response.json())`**:
   - The `Response` object contains methods to extract data (e.g., `.json()`, `.text()`).
   - Calling `response.json()` returns another promise that resolves with the actual data.
3. **Second `.then(data => console.log(data))`**:
   - This receives the extracted JSON data and processes it.

### Example
Fetching data from a public API:
```javascript
fetch("https://jsonplaceholder.typicode.com/posts/1")
  .then(response => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json(); // Extracting JSON data
  })
  .then(data => console.log(data)) // Handling extracted data
  .catch(error => console.error("Fetch error:", error));
```

---

## 3. Async/Await
**Async/Await** provides a cleaner, more readable way to handle asynchronous code.

### How It Works
- `async` before a function makes it return a promise.
- `await` inside an `async` function pauses execution until the promise resolves.

### Example with Fetch
```javascript
async function fetchData() {
  try {
    let response = await fetch("https://jsonplaceholder.typicode.com/posts/1");
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    let data = await response.json(); // Extracting JSON data
    console.log(data); // Handling extracted data
  } catch (error) {
    console.error("Fetch error:", error);
  }
}

fetchData();
```

### Breaking It Down
1. `async function fetchData()` marks the function as asynchronous.
2. `await fetch(url)` waits for the fetch operation to complete.
3. `await response.json()` waits for the response to be converted to JSON.
4. If an error occurs, it’s caught in the `catch` block.

### Combining Promises with Async/Await
```javascript
function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function delayedMessage() {
  console.log("Start");
  await delay(2000); // Pauses execution for 2 seconds
  console.log("After 2 seconds");
}

delayedMessage();
```

---
## 3. Async/Await
**Async/Await** provides a cleaner, more readable way to handle asynchronous code.

### CRUD Operations with Fetch API
We can perform CRUD (Create, Read, Update, Delete) operations using Fetch API with async/await.

### Create (POST Request)
```javascript
async function createPost() {
  let newPost = { title: "New Post", body: "This is a new post.", userId: 1 };
  try {
    let response = await fetch("https://jsonplaceholder.typicode.com/posts", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newPost)
    });
    let data = await response.json();
    console.log("Post Created:", data);
  } catch (error) {
    console.error("Error creating post:", error);
  }
}

createPost();
```

### Read (GET Request)
```javascript
async function getPost(id) {
  try {
    let response = await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`);
    let post = await response.json();
    console.log("Post:", post);
  } catch (error) {
    console.error("Error fetching post:", error);
  }
}

getPost(1);
```

### Update (PUT Request)
```javascript
async function updatePost(id) {
  let updatedPost = { title: "Updated Title", body: "Updated content." };
  try {
    let response = await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(updatedPost)
    });
    let data = await response.json();
    console.log("Post Updated:", data);
  } catch (error) {
    console.error("Error updating post:", error);
  }
}

updatePost(1);
```

### Delete (DELETE Request)
```javascript
async function deletePost(id) {
  try {
    let response = await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`, {
      method: "DELETE"
    });
    if (response.ok) {
      console.log("Post Deleted");
    } else {
      console.error("Error deleting post");
    }
  } catch (error) {
    console.error("Error deleting post:", error);
  }
}

deletePost(1);
```

---

## Summary
| Concept       | Use Case                          | Syntax Example |
|--------------|----------------------------------|---------------|
| Promises     | Async operations without callback hell | `promise.then().catch()` |
| Fetch API    | HTTP requests                     | `fetch(url).then(response => response.json())` |
| Async/Await  | Clean asynchronous code          | `async function() { await fetch() }` |
| CRUD with Fetch | API interactions (Create, Read, Update, Delete) | `fetch(url, { method: ... })` |

This guide provides an in-depth understanding of JavaScript's asynchronous patterns, making your code more readable and maintainable.