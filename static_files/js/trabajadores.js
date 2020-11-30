

function ActualizarTablas(data){

    /* Evento */
    if(data.nuevo_evento){
        $("#tb_trabajador_eventos").append(
            "<tr><td><input type='checkbox' name='post[]' value='255'></td><td>"+ 
            data.nuevo_evento.fecha +"</td><td>"+
            data.nuevo_evento.nombre +"</td><td>"+
            data.nuevo_evento.lugar +"</td><td>"+
            data.nuevo_evento.nivel +"</td>"+
            "<td class='text-right'>"+
            "<a class='ver_evento' data-id='/docencia/ver/evento/"+data.nuevo_evento.id+"'><i class='fa fa-eye icon-muted'></i></a>"+
            "<a id='evento_"+data.nuevo_evento.id+"' class='modificar_evento' data-id='/docencia/modificar/evento/"+data.nuevo_evento.id+"'><i class='fa fa-pen icon-muted'></i></a>"+
            "<a class='eliminar_evento' data-id='/docencia/eliminar/evento/"+data.nuevo_evento.id+"'><i class='fa fa-trash icon-muted'></i></a>"+
            "</td></tr>"
        );
    }   

    /* Tesis */
    if(data.nueva_tesis){
        $("#tb_trabajador_tesis").append(
            "<tr><td><input type='checkbox' name='post[]' value='255'></td><td>"+ 
            data.nueva_tesis.fecha +"</td><td>"+
            data.nueva_tesis.titulo +"</td><td>"+
            data.nueva_tesis.grado +"</td><td>"+
            data.nueva_tesis.especialidad +"</td><td>"+
            data.nueva_tesis.lugar +"</td><td></tr>"
        );

  
    }   

    /* Tribunal */
    if(data.nuevo_tribunal){
        $("#tb_trabajador_tribunales").append(
            "<tr><td><input type='checkbox' name='post[]' value='255'></td><td>"+ 
            data.nuevo_tribunal.fecha +"</td><td>"+
            data.nuevo_tribunal.tesis +"</td><td></tr>"
        );
    }   

    /* Certificación */
    if(data.nueva_certificacion){
        $("#tb_trabajador_certificaciones").append(
            "<tr><td><input type='checkbox' name='post[]' value='255'></td><td>"+ 
            data.nueva_certificacion.fecha_inicio +"</td><td>"+
            data.nueva_certificacion.fecha_terminacion +"</td><td>"+
            data.nueva_certificacion.centro_estudios +"</td><td>"+
            data.nueva_certificacion.nombre_profesor +"</td><td>"+
            data.nueva_certificacion.cantidad_horas +"</td><td>"+
            data.nueva_certificacion.creditos +"</td><td></tr>"
        );
    }   

    /* Ponencia */
    if(data.nueva_ponencia){
        $("#tb_trabajador_ponencias").append(
            "<tr><td><input type='checkbox' name='post[]' value='255'></td><td>"+ 
            data.nueva_ponencia.fecha +"</td><td>"+
            data.nueva_ponencia.evento +"</td><td>"+
            data.nueva_ponencia.ponencia +"</td><td>"+
            data.nueva_ponencia.participacion +"</td><td></tr>"
        );
    }   

    /* Oponencia */
    if(data.nueva_oponencia){
        $("#tb_trabajador_oponencias").append(
            "<tr><td><input type='checkbox' name='post[]' value='255'></td><td>"+ 
            data.nueva_oponencia.fecha +"</td><td>"+
            data.nueva_oponencia.elemento +"</td><td></tr>"
        );
    }   

    /* Artículo */
    if(data.nuevo_articulo){
        $("#tb_trabajador_articulos").append(
            "<tr><td><input type='checkbox' name='post[]' value='255'></td><td>"+ 
            data.nuevo_articulo.fecha_publicado +"</td><td>"+
            data.nuevo_articulo.doi +"</td><td>"+
            data.nuevo_articulo.issn +"</td><td>"+      
            data.nuevo_articulo.titulo +"</td><td>"+
            data.nuevo_articulo.revista +"</td><td>"+
            data.nuevo_articulo.numero +"</td><td>"+ 
            data.nuevo_articulo.paginas +"</td><td></tr>"
        );
    }   

    /* Libro */
    if(data.nuevo_libro){
        $("#tb_trabajador_libros").append(
            "<tr><td><input type='checkbox' name='post[]' value='255'></td><td>"+ 
            data.nuevo_libro.fecha_publicado +"</td><td>"+
            data.nuevo_libro.isbn +"</td><td>"+
            data.nuevo_libro.editorial +"</td><td>"+     
            data.nuevo_libro.titulo +"</td><td>"+
            data.nuevo_libro.paginas +"</td><td>"+
            data.nuevo_libro.capitulo +"</td><td>"+                            
            data.nuevo_libro.pais +"</td><td></tr>"
        );
    }   


    /* Proyecto */
    if(data.nuevo_proyecto){
        $("#tb_trabajador_proyectos").append(
            "<tr><td><input type='checkbox' name='post[]' value='255'></td><td>"+ 
            data.nuevo_proyecto.fecha_inicio +"</td><td>"+
            data.nuevo_proyecto.fecha_terminacion +"</td><td>"+
            data.nuevo_proyecto.centro_costo +"</td><td>"+        
            data.nuevo_proyecto.programa +"</td><td>"+
            data.nuevo_proyecto.nombre +"</td><td>"+
            data.nuevo_proyecto.tipo +"</td><td>"+            
            data.nuevo_proyecto.nivel +"</td><td>"+
            data.nuevo_proyecto.presupuesto_anno +"</td><td>"+            
            data.nuevo_proyecto.presupuesto_total +"</td><td></tr>"
        );
    }   

    /* Servicios */
    if(data.nuevo_servicio){
        $("#tb_trabajador_servicios").append(
            "<tr><td><input type='checkbox' name='post[]' value='255'></td><td>"+ 
            data.nuevo_servicio.fecha_inicio +"</td><td>"+
            data.nuevo_servicio.fecha_terminacion +"</td><td>"+
            data.nuevo_servicio.centro_costo +"</td><td>"+        
            data.nuevo_servicio.nombre +"</td><td>"+
            data.nuevo_servicio.tipo +"</td><td>"+
            data.nuevo_servicio.dim +"</td><td>"+
            data.nuevo_servicio.cliente +"</td><td>"+            
            data.nuevo_servicio.monto +"</td><td></tr>"
        );
    }  

    /* Servicios */
    if(data.nuevo_proyecto){
        $("#tb_trabajador_proyectos").append(
            "<tr><td><input type='checkbox' name='post[]' value='255'></td><td>"+ 
            data.nuevo_proyecto.fecha_inicio +"</td><td>"+
            data.nuevo_proyecto.fecha_terminacion +"</td><td>"+
            data.nuevo_proyecto.centro_costo +"</td><td>"+
            data.nuevo_proyecto.programa +"</td><td>"+
            data.nuevo_proyecto.titulo +"</td><td>"+
            data.nuevo_proyecto.tipo +"</td><td>"+
            data.nuevo_proyecto.nivel +"</td><td>"+
            data.nuevo_proyecto.presupuesto_anno +"</td><td>"+
            data.nuevo_proyecto.presupuesto_total +"</td><td></tr>"
        );
    }   

};



