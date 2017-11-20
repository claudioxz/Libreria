$(window).on('load',() =>{
    $('#crear_sello').on('click', ()=>{
        $.ajax({
            url: base_url+'ajax/nuevo_sello/',
            dataType: "json",
            data: $('#nuevo-sello').serialize(),
             type: 'POST',
            success: function (data) {
                //data.error == bool
                if(data.error){
                    showErrors(data);
                }else{
                    const id_tags =$('#id_sello');
                    id_tags.append('<option value="'+data.id+'" selected>'+data.nombre+'</option>');
                    id_tags.trigger('contentChanged');
                    messageValid('El sello ha sido creado correctamente','id_editorial');
                }
            }
        });
    });

    $('#crear_edicion').on('click',()=>{
        const data = $('#nuevo-edicion').serialize()+'&imagen='+$('#id_imagen').val();
        $.ajax({
            url: base_url+'ajax/crear_edicion/',
            dataType: "json",
            method: "POST",
            data: data,
            success: function (data) {
                //data.error == bool
                if(data.error){
                    showErrors(data);;
                }else{
                    const tags = $('#id_tags');
                    tags.append('<option value="'+data.id+'" selected>'+data.nombre+'</option>');
                    tags.trigger('contentChanged');
                    messageValid('La edicion ha sido creado correctamente','nombre-tag');
                }
            }
        });
    });

});