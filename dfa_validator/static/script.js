
document.addEventListener("DOMContentLoaded", function () {


    document.getElementById("checkForm").addEventListener("submit", function (e) {
        e.preventDefault(); 

    //     const type = document.getElementById("type").value;
    //     const value = document.getElementById("value").value;

    //     fetch("/validate", {
    //         method: "POST",
    //         headers: {
    //             "Content-Type": "application/json"
    //         },
    //         body: JSON.stringify({
    //             type: type,
    //             value: value
    //         })
    //     })
    //     .then(response => response.json())
    //     .then(data => {
    //         document.getElementById("result").innerText = data.message;
    //     })
    //     .catch(error => console.error(error));
    // });

})});
