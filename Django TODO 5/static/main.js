let form = document.getElementById("myForm")
function getTodos(){
    let wrapper = document.getElementById('subContainer')
    let url = 'http://127.0.0.1:8000/api/get_todos/'
    fetch(url)
    .then(response=>response.json())
    .then(data=>{

        for(let d of data){
            let listContainer = `
                 <p>${d.title}</p>
        `

            wrapper.innerHTML += listContainer
        }


    })
}
getTodos()

form.addEventListener('submit', function(e){
    e.preventDefault()
    let inputValue = document.getElementById('input').value
//    console.log(inputValue)

    const data = { title: inputValue };
    let url = 'http://127.0.0.1:8000/api/create_todo/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(function(){
        getTodos()
    })

//    .then(data => {
//        console.log("Success:", data);
//    })
})