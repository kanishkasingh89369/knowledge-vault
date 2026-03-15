const API = "http://127.0.0.1:5000"

function addNote(){

    const title = document.getElementById("title").value
    const content = document.getElementById("content").value

    fetch(API + "/add-note",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            title:title,
            content:content
        })
    })
    .then(res => res.json())
    .then(data => alert(data.message))
}

function searchNote(){

    const title = document.getElementById("searchTitle").value

    fetch(API + "/note/" + encodeURIComponent(title))
    .then(res => res.json())
    .then(data => {

        const result = document.getElementById("result")

        if(data){
            result.innerHTML = `
            <h3>${data[1]}</h3>
            <p>${data[2]}</p>
            `
        }else{
            result.innerHTML="Note not found"
        }

    })
}