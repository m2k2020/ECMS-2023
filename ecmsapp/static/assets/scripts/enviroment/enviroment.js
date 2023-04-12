$(document).ready(function() {
    createEnviroment();

   

})

function createEnviroment(){
    $('#registerForm').submit(function (e){
        e.preventDefault();

        $HouseNo = $('#houseno').val();
        $Renter = $('#renter').val();
        $Data = $('#regoster_date').val();
        $status = 0

        if($HouseNo != null && $Renter != null && $Data != null && $status == 0) {
            
            // console.log($District + " " + $Type + " " + $HouseNo+ " " + $status)
            $.ajax({
                url: '',
                type: "POST",
                data: {
                    'houseno': $HouseNo,
                    'renter': $Renter,
                    'regoster_date': $Data,
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

                        $('#newEnviroment').hide();
                        // readHouse()
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

// function readHouse(){

//     $.ajax({
//         url: "house/",
//         type: "POST",
//         async: false,
//         data:{
//             res : 1,
//             csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
//         },
//         success: function(response){
//             $('#tbody_data').html(response)
//         }
//     })

// }

// function EditHouse(){

//     $('#houseEdit').click(function(){
//         $id=$(this).attr('name');
//         alert($id)
//         // $('#updateHouse').modal('show');
//         // $('#udistrict').val($id)


//     })

// }