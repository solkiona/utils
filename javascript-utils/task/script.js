function addTask(){
    let item = document.getElementById('taskInput').value;
    let taskList = document.getElementById('taskList');
    let newList = document.createElement('li');
    let action = document.createElement('button');
    action.style.backgroundColor="red";
    action.style.color="white";
    action.textContent="Delete Task";
    let taskContainer = document.createElement('div');
    newList.textContent=item;
    taskContainer.appendChild(newList);
    taskContainer.appendChild(action);
    taskContainer.style.display="flex";
    taskContainer.style.gap="10px";
    taskContainer.style.justifyContent="space-between";
    taskContainer.style.marginBottom="10px";
    taskList.appendChild(taskContainer);
    document.getElementById('taskInput').value='';
    newList.addEventListener("click", ()=>{

        alert("task completed");
        newList.classList.toggle('completed');
    })
    action.addEventListener("click", ()=>{
        //do nothing for now
        alert('delete task');
        taskContainer.remove();
    })
}