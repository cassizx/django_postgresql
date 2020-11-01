// $(document).ready(function(){
//  
// })
var csrfToken = $('input[name=csrfmiddlewaretoken]').val();
$("#info_btn" ).click(function(evt){
    evt.stopImmediatePropagation();
    evt.preventDefault();
    var val_input =  $("#table_name" ).val()
    console.log(val_input);
    // window.location.href = 'logout/';
    if(val_input){
        $.ajax({
            url: '/select_from_table/',
            type: 'get', // This is the default though, you don't actually need to always mention it
            data:{
                request_data: val_input
            },
        success: function(response) {
            $("#table_name").val('');
            $('.show').remove()
            $('.container-fluid').append('<div class="show card"></div>')
            $(".show").append(
                '<div class="card-body border-dark" style="margin: 0 auto;">'+
                '<span class="close-btn"> <img src="https://cdn4.iconfinder.com/data/icons/miu/22/circle_close_delete_-128.png" class="delete_result_btn"></img> </span>'+
                '<h4 class="card-title">' + 'Table: '+ '<span class="val_input">' + val_input + '</span>' +'</h4>'+
                '<pre>' + response.context + '</pre>'+
                '</div>')
            // alert($('.val_input').html())
        },
        failure: function(response) { 
            alert('Got an error dude');
        }
    })
            }
        });
// CREATE
$(".create_btn" ).click(function(evt){      
    evt.stopImmediatePropagation();
    evt.preventDefault();
    var val_input =  $("#table_name_to_create" ).val()
    console.log(val_input);
    // window.location.href = 'logout/';
    if(val_input){
        $.ajax({
            url: '/create_table/',
            type: 'post', // This is the default though, you don't actually need to always mention it
            data:{
                csrfmiddlewaretoken: csrfToken,
                table_name_to_create: val_input 
            },
        success: function(response) {
            $('.exist_table').remove()
            console.log(response.exist_tables )
            // $(".card-deck").append
            alert( response.status)
            $('<div class="card mb-4 shadow-sm exist_table">' +
                    '<div class="card-body" style="margin: 0 auto;">'+
                        '<h4 class="card-title">Exist table:</h4>' + 
                            '<pre>' +
                                response.exist_tables +
                            '</pre>'+
                        '</div>'+
                   '</div>'
                ).insertBefore('.data_inputs')
            $("#table_name_to_create" ).val(' ')
        },
        failure: function(response) { 
            alert('Got an error dude.');
        }
    })
            }
        });
$(".container-fluid").bind("DOMSubtreeModified", function(){ 
$('.delete_result_btn').click(function(evt){
$('.show').remove();
});
})

$('.drop_btn').click(function(evt){
evt.stopImmediatePropagation();
evt.preventDefault();
var table_name_to_drop = $('#table_name_to_drop').val()
result = confirm('Подтвердите удаление таблицы ' + table_name_to_drop)
if(result){
console.log('drop table ' + table_name_to_drop + ' confirmed')
$.ajax({
            url: '/drop_table/',
            type: 'post', // This is the default though, you don't actually need to always mention it
            data:{
                csrfmiddlewaretoken: csrfToken,
                table_name_to_drop: table_name_to_drop 
            },
        success: function(response) {
            $('.exist_table').remove()
            if($('.show ') | (table_name_to_drop === $('.val_input').html())){
                $('.show').remove()
            }
            console.log(response.exist_tables )
            // $(".card-deck").append
            $('<div class="card mb-4 shadow-sm exist_table">' +
                    '<div class="card-body" style="margin: 0 auto;">'+
                        '<h4 class="card-title">Exist table:</h4>' + 
                            '<pre>' +
                                response.exist_tables +
                            '</pre>'+
                        '</div>'+
                   '</div>'
                ).insertBefore('.data_inputs')
                alert(response.status)
                $('#table_name_to_drop').val('')
        },
        failure: function(response) { 
            alert('Got an error dude.');
        }
        
});

}
});
// $('.custom_query_btn').modal('show')
// $('#myModal').modal('show')

$("#execute_query").on( "click", function() {
$('#myModal1').modal('hide');  
var textarea_custom_query = $('.textarea_custom_query')
if(textarea_custom_query.val() != ''){
    console.log(textarea_custom_query.val())
    $.ajax({
            url: '/custom_query/',
            type: 'post', // This is the default though, you don't actually need to always mention it
            data:{
                csrfmiddlewaretoken: csrfToken,
                custom_query: textarea_custom_query.val()
            },
        success: function(response) {
            console.log(response.custom_query_resp)  
            // $("#execute_query").on( "click", function() {     
            $('#myModal2').modal('show');   
            // });   
            $('.response_custom_query').html('<pre>'+response.custom_query_resp+'</pre>')               
        },
        failure: function(response) { 
            alert('Got an error dude.');
        }    
    });

    // $("#execute_query").on( "click", function() {
    //     $('#myModal2').modal('show'); 

    // });
}else{
    $("#execute_query").on( "click", function() {
        $('#myModal2').modal('show');  
    });
    console.log('textarea_custom_query none')
}
});

$('#disconnect_btn').click(function(evt){
evt.stopImmediatePropagation();
evt.preventDefault();
$.ajax({
url: 'logout/',
type: 'post', // This is the default though, you don't actually need to always mention it
data:{
        csrfmiddlewaretoken: csrfToken,
    },
    success: function() {
        console.log('Disconnected')  
        window.location.href = "/logout/";                  
    },
    failure: function(response) { 
        alert('Got an error dude.');
    }    
});
})
