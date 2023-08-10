const container = document.getElementById("append")

function DisplayData() {
    fetch(`https://zomato-backend-vxit.onrender.com/crud/get`)
        .then((res) => res.json())
        .then((data) => {
            console.log(data)
        })
        .catch((err) => console.log(err))
}
function fe