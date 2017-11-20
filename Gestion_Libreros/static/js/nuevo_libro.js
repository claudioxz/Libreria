$(window).on('load', ()=>{
    $('#crear_autor').on('click', ()=>{
       $.ajax({
            url: base_url+'ajax/crear_autor/',
            dataType: "json",
            data: $('#nuevo-autor').serialize(),
            success: function (data) {
                //data.error == bool
                if(data.error){
                    showErrors(data);
                }else{
                    $('#id_autor').append('<option value="'+data.id+'" selected>'+data.nombre+'</option>');
                    $('#id_autor').trigger('contentChanged');
                    messageValid('El autor ha sido creado con exito!','pais');
                }
            }
        });
    });

    $('#crear_tag').on('click', ()=>{
       $.ajax({
            url: base_url+'ajax/crear_tag/',
            dataType: "json",
            data: $('#nuevo-tag').serialize(),
            success: function (data) {
                //data.error == bool
                if(data.error){
                    messageError(data.nombre, 'nombre-tag');
                }else{
                    const id_tags =$('#id_tags');
                    id_tags.append('<option value="'+data.id+'" selected>'+data.nombre+'</option>');
                    id_tags.trigger('contentChanged');
                    messageValid('El tag ha sido creado correctamente','nombre-tag');
                }
            }
        });
    });

    $('#crear_coleccion').on('click', ()=>{
        $.ajax({
            url: base_url+'ajax/crear_coleccion/',
            dataType: "json",
            data: $('#nuevo-coleccion').serialize(),
            success: function (data) {
                //data.error == bool
                if(data.error){
                    messageError(data.nombre, 'nombre-coleccion');
                }else{
                    $('#id_coleccion').append('<option value="'+data.id+'" selected>'+data.nombre+'</option>');
                    $('#id_coleccion').trigger('contentChanged');
                    messageValid('La coleccion ha sido creada correctamente','nombre-coleccion');
                }
            }
        });
    });
});