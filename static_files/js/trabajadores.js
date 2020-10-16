function ActualizarEventos(data){

    $("#tb_trabajador_eventos").append(
        "<tr><td><input type='checkbox' name='post[]' value='255'></td><td>"+ 
        data.nuevo_evento.fecha +"</td><td>"+
        data.nuevo_evento.nombre +"</td><td>"+
        data.nuevo_evento.lugar +"</td><td>"+
        data.nuevo_evento.nivel +"</td><td></tr>"
    );
};