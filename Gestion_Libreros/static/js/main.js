/**
 * Created by claudio on 08-08-17.
 */
window.base_url = 'http://127.0.0.1:8000/';
$(document).ready(function() {
    const selects = $('select');
    selects.material_select();
    $('.datepicker').pickadate({
        selectMonths: true,
        selectYears: 500,
        format: 'yyyy-mm-dd',
        closeOnSelect: false,
        labelMonthNext: 'Mes siguiente',
        labelMonthPrev: 'Mes anterior',
        labelMonthSelect: 'Selecciona un mes',
        labelYearSelect: 'Selecciona un año',
        monthsFull: [ 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre' ],
        monthsShort: [ 'Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic' ],
        weekdaysFull: [ 'Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado' ],
        weekdaysShort: [ 'Dom', 'Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab' ],
        weekdaysLetter: [ 'D', 'L', 'M', 'X', 'J', 'V', 'S' ],
        today: 'Hoy',
        clear: 'Limpiar',
        close: 'Cerrar',
        width: 50
    });
    $('.modal').modal();
    selects.on('contentChanged', function() {
        $(this).material_select();
    });
    if(window.location.pathname.indexOf("/gestion_libros/") !== -1){
        $('.collapsible').collapsible("open",0)
    }
    $('.collapsible-body a[href="'+window.location.pathname+'"]').parent('li').addClass('active red');
    $('.collapsible-header').on('click', function () {
        if(window.location.pathname !== $(this).data("href")){
            if($(this).data("href")){
                window.location = $(this).data("href");
            }
        }
    });
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });
    $('input[type=text], input[type=number]').attr('placeholder', '""');
});
function showErrors(data){
    for(let prop in data){
        if(data.hasOwnProperty(prop) && typeof data[prop] !== 'function' && prop !== "error"){
            let value = data[prop];
            let input_id = "id_" + prop;
            const input = document.getElementById(input_id);

            if(input.tagName === "SELECT"){
                messageErrorSelect(value, input_id)
            }else if(input.type === "file"){
                messageErrorFile(value, input_id);
            }else{
                messageError(value, input_id);
            }
        }
    }
}

function messageErrorSelect(message, id) {
    const select = $('#'+id);
    select.unbind('change');
    if(message){
        if(exist('error-'+id)){
            $('#error-'+id).remove();
        }
        select.siblings('.select-dropdown').addClass('invalid');
        select.parent('div').next('label').after('<span id="error-'+id+'" class="error-message">'+message+'</span>');
        select.on('change',function () {
            select.siblings('.select-dropdown').removeClass('invalid');
            $('#error-'+id).remove();
        });

    }else{
        select.siblings('.select-dropdown').removeClass('invalid');
        $('#error-'+id).remove();
    }
}
function messageErrorFile(message, id){
    if(message){
        const divPath = $('#path-'+id);
        if(exist('error-'+id)){
            $('#error-'+id).remove();
        }
        divPath.after('<span id="error-'+id+'" class="error-message">'+message+'</span>');
        divPath.find('input').addClass('invalid');
        divPath.find('input').unbind('change');
        divPath.find('input').change(function () {
            $(this).removeClass("invalid");
            $('#error-'+id).remove();
        });
    }else{
        $('#error-'+id).remove();
    }
}
function messageError(message, id) {
    if(message){
        $('.green').remove();
        const element = $('#'+id);
        element.addClass('invalid');
        element.next('label').attr('data-error', message);
        element.unbind('keydown');
        element.unbind('change');
        element.on('keydown',function () {
           element.removeClass('invalid');
           element.next('label').removeData('error');
        });
        element.on('change',function () {
           element.removeClass('invalid');
           element.next('label').removeData('error');
        });
    }
}
function messageValid(message, id) {
    if($('#mes-'+id)[0] === undefined){
        $('#'+id).after('<span class="valid-message" id="mes-'+id+'">'+message+'</span>');
    }
}
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function exist(id) {
    return $('#' + id)[0] !== undefined;
}
