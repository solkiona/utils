

function addTask(){

    if(localStorage.length == 0){

    }
    let taskInput = document.getElementById('taskInput');

    let task = taskInput.value.trim();
    let index = Math.floor(Math.random() * 100);
    

    if(task == ''){
        alert('Please enter a task');
        return;
    }

    let taskList = document.getElementById('taskList');
    if(localStorage.length == 0){
        taskList.innerHTML = ""
    }

    localStorage.setItem(`task${index}`, task);
    let taskContainer = document.createElement('div');
    let li = document.createElement('li');
    li.textContent = task;
    let btn = document.createElement('button');
    btn.textContent = 'Delete Task';
    taskContainer.appendChild(li);
    taskContainer.appendChild(btn);
    taskContainer.style.display = 'flex';
    taskContainer.style.gap = '10px';
    taskContainer.style.justifyContent ='space-between';
    taskContainer.style.padding='10px';

    btn.addEventListener('click', ()=>{

        localStorage.removeItem(`task${index}`);
        taskContainer.remove();
    })

    li.addEventListener('click', ()=>{
        li.classList.toggle('completed');
    })

    taskList.appendChild(taskContainer);

    document.getElementById("taskInput").value=''
    // alert(task);
}


function clearTask(){
    localStorage.clear();
    let taskList = document.getElementById('taskList');
    taskList.innerHTML = "<p style='color:gray; font-size:20px; font-weight:bold;'>Add Items to your Todo</p>"
    // alert('All tasks cleared');
}

document.addEventListener('DOMContentLoaded', ()=>{
    
    if(localStorage.length == 0 ){
        let taskList = document.getElementById('taskList');
        taskList.innerHTML = "<p style='color:gray; font-size:20px; font-weight:bold;'>Add Items to your Todo</p>"
        }
    Object.keys(localStorage).forEach((key)=>{
        task = localStorage.getItem(key);
        let taskList = document.getElementById('taskList');
        
    let taskContainer = document.createElement('div');
    let li = document.createElement('li');
    li.textContent = task;
    let btn = document.createElement('button');
    btn.textContent = 'Delete Task';
    taskContainer.appendChild(li);
    taskContainer.appendChild(btn);
    taskContainer.style.display = 'flex';
    taskContainer.style.gap = '10px';
    taskContainer.style.justifyContent ='space-between';
    taskContainer.style.padding='10px';

    btn.addEventListener('click', ()=>{
        localStorage.removeItem(key);
        taskContainer.remove();
    })

    li.addEventListener('click', ()=>{
        li.classList.toggle('completed');
    })

    taskList.appendChild(taskContainer);

    

    document.getElementById("taskInput").value=''
            
    })
})

