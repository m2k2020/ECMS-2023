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

        $('#refno').text($ref)

        $('#name').text($renter)
        $('#telephone').text($tel)
        $('#martial').text($martial)

        

    })
}


function printInvoice(){
    $('.printer').click(function (){
        window.print()
    })
}