$(document).ready(function() {
    createHouse();
})

function createHouse(){
    $('#registerForm').submit(function (e){
        e.preventDefault();
        $('#')
        alert("clicked Button")
        $('#newUser').hide();
        location.reload()
    })
}