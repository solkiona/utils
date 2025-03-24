let myPromise = new Promise((resolve, reject) => {
    setTimeout(()=>{

        if(!false){
            resolve('Promise fulfilled');
        } else {
            reject('Promise rejected');
        }
       
    }, 2000)
});

function fetchUser(){
    return new Promise(
        (resolve, reject) => {
            setTimeout(
                
            ()=>{
                
                let user = {
                    name: 'John Doe',
                    age: 30,
                    email: 'johndoe@example.com'
                }
                if (user) resolve(user);
                else reject('User not found');
            }
                
                ,2000)
        }
    )
}

fetchUser()
.then(user => console.log(user))
.catch(err=> console.error(err))
.finally(() => console.log("Promise ended"))


fetch("https://jsonplaceholder.typicode.com/users")
.then(response => {
    console.log('status:', response.status);
    if(!response.ok) {
        throw new Error("Error fetching users")
    } else {
        console.log('converting to json...')
        return response.json();
    }
})
.then (users => console.log(users))
.catch(err => console.error(err))


const fetchData = async () => {
    const url = document.getElementById("url").value.trim();

    document.getElementById('result').innerHTML = "Fetching...";
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
       
    }
      const data = await response.json();
      
        const table = document.createElement('table');
  
        const tableHeader = document.createElement('tr');
        Object.keys(data[0]).forEach(key => {
          const th = document.createElement('th');
          th.textContent = key;
          tableHeader.appendChild(th);
        });
        table.appendChild(tableHeader);
  
        data.forEach(item => {
          const row = document.createElement('tr');
          Object.values(item).forEach(value => {
            const cell = document.createElement('td');
            if(typeof value === 'object'){
                let addr = '';
            
                    Object.values(value).forEach(subvalue => {
                        if(typeof(subvalue) !== 'object') addr += `${subvalue}, `
                    })

                console.log(addr.slice(0, -2))
                cell.textContent = addr.slice(0, -2);
            }  else {
                cell.textContent = value;
            }  
            
            row.appendChild(cell);
          });
          table.appendChild(row);
        });

        document.getElementById('result').innerHTML = '';
  
        document.getElementById('result').appendChild(table);
      console.log(data);
    } catch (error) {
        document.getElementById('result').innerHTML= `There has been a problem with your fetch operation: ${error}`;
      console.error('There has been a problem with your fetch operation:', error);
    }
  }

  let filter = document.getElementById("filter");
  filter.addEventListener('keyup', ()=>{
    let filterValue = filter.value.toLowerCase();
    let table = document.querySelector('table');
    let rows = table.getElementsByTagName('tr');

    for (let i = 1; i < rows.length; i++) {
      let cells = rows[i].getElementsByTagName('td');
      let match = false;

      for (let j = 0; j < cells.length; j++) {
        if (cells[j].innerHTML.toLowerCase().indexOf(filterValue) > -1) {
          match = true;
          break;
        }
      }

      if (match) {
        rows[i].style.display = '';
      } else {
        rows[i].style.display = 'none';
      }
    }
  })

