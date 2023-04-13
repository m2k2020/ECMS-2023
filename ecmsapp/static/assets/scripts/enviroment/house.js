$(document).ready(function() {
    readHouse();
    createHouse();
    // EditHouse();
})

function createHouse(){
    $('#registerForm').submit(function (e){
        e.preventDefault();

        $District = $("#district").val();
        $DistrictApr = $("#district option:selected").data("foo");
        $Type = $('#type').val();
        $HouseNo = $('#houseno').val();
        $HouseNumber = $DistrictApr + "" + $HouseNo
        $status = 0

        
        if($District != null && $DistrictApr != null && $Type != null && $HouseNo != null && $HouseNumber != null && $status == 0) {
            
            // alert(`Option Value: ${$District}\ndata-foo: ${$DistrictApr}\nHouseNumer: ${$HouseNumber}`);
       
     
            // console.log($District + " " + $Type + " " + $HouseNo+ " " + $status)
            $.ajax({
                url: '',
                type: "POST",
                data: {
                    'district': $District,
                    'type': $Type,
                    'houseno': $HouseNumber,
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
                    swal({
                        title: "Error !",
                        text: "There was an error: "+data,
                        icon: "error",
                        timer: 4000, // time in milliseconds
                        timerProgressBar: true,
                        showConfirmButton: false
                    })
                    // console.log("Erro is "+data)
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

// function EditHouse(){

//     $('#houseEdit').click(function(){
//         $id=$(this).attr('name');
//         alert($id)
//         // $('#updateHouse').modal('show');
//         // $('#udistrict').val($id)


//     })

// }