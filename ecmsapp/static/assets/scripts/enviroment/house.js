$(document).ready(function() {
    readHouse();
    createHouse();
    EditHouse();
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
                        readHouse()
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

function readHouse(){

    $.ajax({
        url: "house/",
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

function EditHouse(){

    $('#houseEdit').click(function(){
        $id=$(this).attr('name');
        alert($id)
        // $('#updateHouse').modal('show');
        // $('#udistrict').val($id)


    })

}