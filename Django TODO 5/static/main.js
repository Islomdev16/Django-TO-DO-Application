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
                <div style="margin-top: 1px;"><p>Lorem ipsum dolor sit amet</p></div>
                <div class="d-flex">
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

    const data = {title: "inputValue"};
    let url = 'http://127.0.0.1:8000/api/create_todo'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())

    .then(data => {
        console.log("Success:", data);
    })
//    .catch((error) => {
//    console.error("Error:", error);
//    });
})