$(document).ready(function() {
    createHouse();
})

function createHouse(){
    $('#registerForm').submit(function (e){
        e.preventDefault();

        $District = $('#district').val();
        $Type = $('#type').val();
        $HouseNo = $('#houseno').val();
        $status = 0

        if($District != null && $Type != null && $HouseNo != null && $status == 0) {
            
            // console.log($District + " " + $Type + " " + $HouseNo+ " " + $status)


            $.ajax({
                url: '',
                type: "POST",
                data: {
                    'district': $District,
                    'type': $Type,
                    'houseno': $HouseNo,
                    'status': $status,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()                    
                },
                success: function(data) {
                    swal({
                        title: "Success !",
                        text: "You have successfully Created",
                        icon: "success",
                        timer: 1000, // time in milliseconds
                        timerProgressBar: true,
                        showConfirmButton: false
                    })
                    .then(function(){

                        $('#newUser').hide();
                        location.reload();
                    })

                },
                error:function(data){
                    console.log("Erro is "+data)
                }
            })

            
        }
        else{
            alert("Error");
        }


    })
}