$(document).ready(function() {
    viewTransaction()
    printInvoice()
    
})

function viewTransaction(){
    $('.viewTransaction').click(function ()
    {
        // e.preventDefault()
        $('#invoice').modal('show');
        $id = $(this).data('id');
        $renter = $(this).data('renter');
        $tel = $(this).data('tel');
        $martial = $(this).data('martial');
        $type = $(this).data('type');
        $district = $(this).data('district');
        $houseno = $(this).data('houseno')
        $date = $(this).data('date');
        $price = $(this).data('price');
        $year = $(this).data('year');

        $ref = $houseno +$year +"100"+$id
        $amount = "$"+$price+".00"

        $('#refno').text($ref)

        $('#name').text($renter)
        $('#Intelephone').text($tel)
        $('#Inmartial').text($martial)



        $('#Indistrict').text($district)
        $('#Intype').text($type)
        $('#Inhouseno').text($houseno)

        $('#customerinfo').text($renter)
        $('#datepay').text($date)
        $('#amount').text($amount)
        
        
        
        
    })
}


function printInvoice(){
    $('.printer').click(function (){
        hidden()
        window.print()
        show()
    })
}
function hidden(){
    $('#hiddenNav').hide()
    $('#hiddenSide').hide()
    $('#hiddenSetting').hide()
    $('#hiddenTable').hide()
    $('#hiddenFooter').hide()
    $('#hiddecardheader').hide()
    $('.close').hide()
}
function show(){
    $('#hiddenNav').show()
    $('#hiddenSide').show()
    $('#hiddenSetting').show()
    $('#hiddenTable').show()
    $('#hiddenFooter').show()
    $('#hiddecardheader').show()
    $('.close').show()
}