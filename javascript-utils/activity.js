const addTodo = ()=>{
    let userInput = document.querySelector("#userInput").value.trim();
    let li = document.createElement('li');
    let index = Math.floor(Math.random()*100);
    li.textContent=userInput;
    let listContainer = document.querySelector('.listContainer');
    listContainer.appendChild(li);
    localStorage.setItem(`todo${index}`, userInput);
    li.addEventListener('click',()=>{
        li.classList.toggle('completed');
    })

    console.log(`${userInput} was saved as todo${index}`);

}

const deleteTodos = ()=>{
    localStorage.clear();
    let listContainer = document.querySelector('.listContainer');
    listContainer.innerHTML = '<p style="color: gray; font-size: 20px">No todos</p>';
}


document.addEventListener('DOMContentLoaded', () => {
    let ul = document.querySelector('.listContainer');
    
    if(localStorage.length == 0){
        ul.innerHTML = '<p style="color: gray; font-size: 20px">No todos</p>';
        return;
    }
    let todos = Object.values(localStorage);
    todos.reverse(); // Sort in descending order
    console.log(todos.reverse())
    todos.forEach((value) => {
        let li = document.createElement('li');
        
        li.textContent = value;
        ul.appendChild(li);
        console.log(value);
    });
});