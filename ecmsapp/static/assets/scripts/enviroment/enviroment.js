$(document).ready(function() {
    readEnviroment();
    createEnviroment();
    EditEnviroment();

   

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
                url: '/createEnviroment/',
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
                        readEnviroment()
                        location.reload();
                    })

                },
                error:function(data){
                    swal({
                        title: "Error !",
                        text: "There was an error: "+data,
                        icon: "error",
                        timer: 4000, // time in milliseconds
                        timerProgressBar: true,
                        showConfirmButton: false
                    })
                }
            })

            
        }
        else{
            swal({
                title: "Error !",
                text: "There was an error for Saving",
                icon: "error",
                timer: 4000, // time in milliseconds
                timerProgressBar: true,
                showConfirmButton: false
            })
        }


    })
}

function readEnviroment(){

    $.ajax({
        url: "enviroment/",
        type: "POST",
        async: false,
        data:{
            res : 1,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
            $('#tbody_data').html(response)
        }
    })

}


function EditEnviroment(){

    $('.EnviromentEdit').click(function(){
        
        $id = $(this).data('id');

        $.ajax({
            url: "/getEnviroment/",
            type: "GET",
            data: {
                'id': $id
            },
            success:function (response){

                console.log(response)

                $('#updateEnviroment').modal('show');

                $house = response.house_no

                $('#uid').val($house)
                // $('#urenter').val($renter)
                // $('#uregoster_date').val($date)
                // $('#uid').val($renter)

                
                
            },
            error: function(response) {
                // Handle errors
                console.log('Error:', response);
            }
        })
        // $renter = $(this).data('renter');
        // $house = $(this).data('house');
        // $date = $(this).data('date');

        // alert($id+ " " +$renter+ " " +$house + " " +$date)

        // $('#updateEnviroment').modal('show');

        // $('#uhouseno').val($house)
        // $('#urenter').val($renter)
        // $('#uregoster_date').val($date)
        // $('#uid').val($renter)



    })

}