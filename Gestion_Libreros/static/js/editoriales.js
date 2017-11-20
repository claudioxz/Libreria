$(window).on('load', ()=>{
    $('#crear_editorial').on('click', crearEditorial);
    $('#editar_editorial').on('click', editarEditorial);

    $('#eliminar_editorial').on('click', function () {
        const id = $(this).data("id");
        $.ajax({
            url: base_url+'ajax/eliminar_editorial/',
            dataType: 'json',
            data: {'pk':id},
            type: 'GET',
            success: function () {
                $('#'+id).remove();
            }
        });
    });

    $('#nombre-editar-editorial').on('keypress', function (e) {
        pulsar(e, true)
    });
    $('#nombre-editorial').on('keypress', function (e) {
        pulsar(e)
    });

});

function crearEditorial(){
    $.ajax({
        url: base_url+'ajax/crear_editorial/',
        dataType: "json",
        data: $('#nuevo-editorial').serialize(),
        success: function (data) {
            if(data.error === true){
                messageError(data.nombre, 'nombre-editorial');
            }else{
                messageValid('La editorial ha sido creado con exito!','nombre-editorial');
                const tr =
                    '<tr id="'+data.id+'">' +
                    '<td>'+data.nombre+'</td>' +
                    '<td><a class="modal-trigger" onclick="copiarAModal('+data.id+')" href="#modal-editar-editorial"><i class="material-icons">edit</i> Editar</a></td>'+
                    '<td><a style="cursor: pointer;" onclick="eliminarEditorial('+data.id+')"><i class="material-icons">close</i> Eliminar </a></td>' +
                    '</tr>';
                $('#tabla-editorial').find('tbody').prepend(tr);
            }
            //data.error == bool
        }
    });
}

function editarEditorial() {
    $.ajax({
        url: base_url+'ajax/editar_editorial/',
        dataType: "json",
        data: $('#editar-editorial').serialize(),
        success: function (data) {
            if(data.error){
                messageError(data.nombre, 'nombre-editar-editorial');
            }else{
                messageValid('La editorial se ha modificado','nombre-editar-editorial');
                $('#'+data.id).find('td').first().html(data.nombre);
            }
            //data.error == bool
        }
    });
}

function pulsar(e, mod = false) {
    let key = (document.all) ? e.keyCode : e.which;
    if(key === 13){
        if(mod){
            editarEditorial();
        }else{
            crearEditorial();
        }
        return false;
    }
}

function copiarAModal(id) {
    $('#editorial-id').val(id);
    $('#nombre-editar-editorial').val($('#'+id).find('td').first().html());
}
