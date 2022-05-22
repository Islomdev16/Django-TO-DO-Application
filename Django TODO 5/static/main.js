let form = document.getElementById("myForm")
function getTodos(){
    let wrapper = document.getElementById('subContainer')
    let url = 'http://127.0.0.1:8000/api/get_todos/'
    fetch(url)
    .then(response=>response.json())
    .then(data=>{

        for(let d of data){
            let listContainer = `
            <div class="wrapper">
                <div class="wrapperText"><p>${d.title} </p></div>
                <div class="iconContainer">
                    <div class="editbtn"><i class="fas fa-pen-alt"></i></div>
                    <div class="delbtn"><i class="fas fa-trash"></i></div>
                </div>
            </div>
            `
            wrapper.innerHTML += listContainer
        }
    })
}
getTodos()

form.addEventListener('submit', function(e){
    e.preventDefault()
    let inputValue = document.getElementById('input').value
    console.log(inputValue)
})