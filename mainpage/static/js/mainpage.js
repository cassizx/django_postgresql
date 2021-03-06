$(document).ready(function(){

var csrfToken = $('input[name=csrfmiddlewaretoken]').val();
var loader_div = '<div class="card-body loader_div" style="margin:0 auto;"><div class="card-title"><span class="loader" ></span></div></div>'

$("#info_btn" ).click(function(evt){
    evt.stopImmediatePropagation();
    evt.preventDefault();
    disable_btns_and_inputs()
    var val_input =  $("#table_name" )
    console.log(val_input);
    // window.location.href = 'logout/';
    if(val_input.val()){
        $('.show').remove()
        $('.container-fluid').append('<div class="show card"></div>')
        $('.show').append(loader_div)
        $.ajax({
            url: '/select_from_table/',
            type: 'get', // This is the default though, you don't actually need to always mention it
            data:{
                request_data: val_input.val()
            },
        success: function(response) {
            $('.loader_div').remove()
            $(".show").append(
                '<div class="card-body border-dark" style="margin: 0 auto;">'+
                '<span class="close-btn"> <img src="https://cdn4.iconfinder.com/data/icons/miu/22/circle_close_delete_-128.png" class="delete_result_btn"></img> </span>'+
                '<h4 class="card-title">' + 'Table: '+ '<span class="val_input">' + val_input.val() + '</span>' +'</h4>'+
                '<span class="time_execution">' + response.context.time_execution + '</span>' +
                '<pre>' + response.context.reqested_table + '</pre>'+
                '</div>')
            // alert($('.val_input').html())
            // console.log(response.context["reqested_table"])
            val_input.val('');
            eneable_btns_and_inputs()
        },
        failure: function(response) { 
            alert('Got an error dude');
            eneable_btns_and_inputs();
        }
    })
            }
        });

    
// CREATE BTN
$(".create_btn" ).click(function(evt){      
    evt.stopImmediatePropagation();
    evt.preventDefault();
    disable_btns_and_inputs()
    var val_input =  $("#table_name_to_create" )
    console.log(val_input);
    // window.location.href = 'logout/';
    if(val_input){
        $.ajax({
            url: '/create_table/',
            type: 'post', // This is the default though, you don't actually need to always mention it
            data:{
                csrfmiddlewaretoken: csrfToken,
                table_name_to_create: val_input.val() 
            },
        success: function(response) {
            $('.exist_table').remove()
            console.log(response.exist_tables)
            console.log(response.status)
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
            eneable_btns_and_inputs()
            val_input.val('')
        },
        failure: function(response) { 
            alert('Got an error dude.');
            eneable_btns_and_inputs();
        }
    })
            }
        });

// Кнопка крестик в div-е отображения ответа 
$(".container-fluid").bind("DOMSubtreeModified", function(){ 
    $('.delete_result_btn').click(function(evt){
        $('.show').remove();
    });
})


// DROP table btn
$('.drop_btn').click(function(evt){
evt.stopImmediatePropagation();
evt.preventDefault();
disable_btns_and_inputs()
var table_name_to_drop = $('#table_name_to_drop')
confirm_drop = confirm('Подтвердите удаление таблицы ' + table_name_to_drop.val())
if(confirm_drop){
console.log('drop table ' + table_name_to_drop.val() + ' confirmed')
$.ajax({
            url: '/drop_table/',
            type: 'post', // This is the default though, you don't actually need to always mention it
            data:{
                csrfmiddlewaretoken: csrfToken,
                table_name_to_drop: table_name_to_drop.val() 
            },
        success: function(response) {
            $('.exist_table').remove()
            if($('.show ') | (table_name_to_drop.val() === $('.val_input').html())){
                $('.show').remove()
            }
            console.log(response.exist_tables )
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
            eneable_btns_and_inputs()
            table_name_to_drop.val('')
        },
        failure: function(response) { 
            alert('Got an error dude.');
            eneable_btns_and_inputs();
        }    
});
}
});


// BTN your query
$("#execute_query").on( "click", function() {
$('#myModal1').modal('hide');  
var textarea_custom_query = $('.textarea_custom_query')
if(textarea_custom_query.val() != ''){
    console.log(textarea_custom_query.val())
    disable_btns_and_inputs()
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
            eneable_btns_and_inputs();               
        },
        failure: function(response) { 
            alert('Got an error dude.');
            eneable_btns_and_inputs();
        }    
    });
}else{
    $("#execute_query").on( "click", function() {
        $('#myModal2').modal('show');  
    });
    console.log('textarea_custom_query none')
}
});


// disconnect_btn
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


// Отключение кнопок и полей ввода
function disable_btns_and_inputs(){
    $('.btn').attr('disabled','disabled')
    $('.form-control').attr('disabled','disabled')
}


// Включение кнопок и полей ввода
function eneable_btns_and_inputs(){
    $('.btn').removeAttr('disabled')
    $('.form-control').removeAttr('disabled')
}


})
