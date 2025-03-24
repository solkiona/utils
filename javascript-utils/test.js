const addTodo = ()=>{
    let userInput = document.getElementById('todoInput');
    let todo = userInput.value.trim();
    let index = Math.floor(Math.random()*100);
    createTodo(todo, index);
    localStorage.setItem(`todo${index}`, todo);
    userInput.value = '';
    console.log(todo)
}


const createTodo = (todo, index) => {
    let todoList = document.getElementById('todoList');
    let parentContainer = document.createElement('div');
    parentContainer.style.display='flex';
    parentContainer.style.gap='10px';
    parentContainer.style.justifyContent='space-between';
    let btn = document.createElement('button');
    btn.textContent = 'Delete Todo';
   
    let li = document.createElement('li');
    parentContainer.appendChild(li);
    parentContainer.appendChild(btn);
   
    btn.addEventListener('click', ()=>deleteTodo(index, parentContainer));

    if(todo == ''){
        return
    }
    li.textContent = todo;
    todoList.appendChild(parentContainer);
    
}

const deleteTodo = (index , div) => {
    localStorage.removeItem(`todo${index}`);
    div.remove();
    
}

const loadTodos = () => {

    if(localStorage.length === 0){
        document.getElementById('todoList').innerHTML = "<p style='color:gray; font-size:20px; font-weight:bold;'>Add Items to your Todo</p>"
    }
    let todos = Object.keys(localStorage);
    todos.forEach(key => {
        let todo = localStorage.getItem(key);
        let index  = key.slice(4)
        console.log(index);
        createTodo(todo, index);
    });
   console.log(todos)

}

document.addEventListener("DOMContentLoaded", loadTodos);