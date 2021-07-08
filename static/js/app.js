$(document).ready(function() {

    $('#valor_1').hide();
    $('#valor_2').hide();
    $('#valor_3').hide();
    $('#valor_4').hide();
    $('#valor_5').hide();
    $('#matriz').hide();
    $('#fasta1').hide();
    $('#fasta2').hide();
    //$('#valor_r').hide();
    $('#out').hide();

    $("#operador").on('change',  function (event) {


        if(this.value=="global") {

            $('#valor_1').hide();
            $('#valor_2').hide();
            $('#valor_3').hide();
            $('#valor_4').hide();
            $('#valor_5').hide();
            $('#matriz').hide();
            $('#fasta1').hide();
            $('#fasta2').hide();
            
            $('#label_1').text("");
            $('#label_2').text("");
            $('#label_3').text("");
            $('#label_4').text("");
            $('#label_5').text("");
            $('#matriz_label').text("");
            $('#fasta1_label').text("");
            $('#fasta2_label').text("");

            $("#label_1").text("s1");
            $('#valor_1').show();

            $("#label_2").text("s2");
            $('#valor_2').show();

            $("#label_3").text("Match");
            $('#valor_3').show();

            $("#label_4").text("misMath");
            $('#valor_4').show();

            $("#label_5").text("d");
            $('#valor_5').show();

            $("#matriz_label").text("Matriz");
            $('#matriz').show();
        }
        else if(this.value=="global2") {
            $('#valor_1').hide();
            $('#valor_2').hide();
            $('#valor_3').hide();
            $('#valor_4').hide();
            $('#valor_5').hide();
            $('#matriz').hide();
            $('#fasta1').hide();
            $('#fasta2').hide();
            
            $('#label_1').text("");
            $('#label_2').text("");
            $('#label_3').text("");
            $('#label_4').text("");
            $('#label_5').text("");
            $('#matriz_label').text("");
            $('#fasta1_label').text("");
            $('#fasta2_label').text("");


            $("#label_1").text("Match");
            $('#valor_1').show();

            $("#label_2").text("misMath");
            $('#valor_2').show();

            $("#label_3").text("d");
            $('#valor_3').show();

            $("#fasta1_label").text("fasta1");
            $('#fasta1').show();

            $("#fasta2_label").text("Fasta2");
            $('#fasta2').show();


        }

        else if (this.value=="local") {
             $('#valor_1').hide();
            $('#valor_2').hide();
            $('#valor_3').hide();
            $('#valor_4').hide();
            $('#valor_5').hide();
            $('#matriz').hide();
            $('#fasta1').hide();
            $('#fasta2').hide();
            
            $('#label_1').text("");
            $('#label_2').text("");
            $('#label_3').text("");
            $('#label_4').text("");
            $('#label_5').text("");
            $('#matriz_label').text("");
            $('#fasta1_label').text("");
            $('#fasta2_label').text("");

        
        }
        else if(this.value=="blast") {
             $('#valor_1').hide();
            $('#valor_2').hide();
            $('#valor_3').hide();
            $('#valor_4').hide();
            $('#valor_5').hide();
            $('#matriz').hide();
            $('#fasta1').hide();
            $('#fasta2').hide();
            
            $('#label_1').text("");
            $('#label_2').text("");
            $('#label_3').text("");
            $('#label_4').text("");
            $('#label_5').text("");
            $('#matriz_label').text("");
            $('#fasta1_label').text("");
            $('#fasta2_label').text("");

        }
        else if(this.value=="muscle") {
             $('#valor_1').hide();
            $('#valor_2').hide();
            $('#valor_3').hide();
            $('#valor_4').hide();
            $('#valor_5').hide();
            $('#matriz').hide();
            $('#fasta1').hide();
            $('#fasta2').hide();
            
            $('#label_1').text("");
            $('#label_2').text("");
            $('#label_3').text("");
            $('#label_4').text("");
            $('#label_5').text("");
            $('#matriz_label').text("");
            $('#fasta1_label').text("");
            $('#fasta2_label').text("");

        
        }
        else if(this.value=="jukes") {
             $('#valor_1').hide();
            $('#valor_2').hide();
            $('#valor_3').hide();
            $('#valor_4').hide();
            $('#valor_5').hide();
            $('#matriz').hide();
            $('#fasta1').hide();
            $('#fasta2').hide();
            
            $('#label_1').text("");
            $('#label_2').text("");
            $('#label_3').text("");
            $('#label_4').text("");
            $('#label_5').text("");
            $('#matriz_label').text("");
            $('#fasta1_label').text("");
            $('#fasta2_label').text("");

        }
        else if(this.value=="kimura") {
             $('#valor_1').hide();
            $('#valor_2').hide();
            $('#valor_3').hide();
            $('#valor_4').hide();
            $('#valor_5').hide();
            $('#matriz').hide();
            $('#fasta1').hide();
            $('#fasta2').hide();
            
            $('#label_1').text("");
            $('#label_2').text("");
            $('#label_3').text("");
            $('#label_4').text("");
            $('#label_5').text("");
            $('#matriz_label').text("");
            $('#fasta1_label').text("");
            $('#fasta2_label').text("");

        }
        else if(this.value=="upgma") {
             $('#valor_1').hide();
            $('#valor_2').hide();
            $('#valor_3').hide();
            $('#valor_4').hide();
            $('#valor_5').hide();
            $('#matriz').hide();
            $('#fasta1').hide();
            $('#fasta2').hide();
            
            $('#label_1').text("");
            $('#label_2').text("");
            $('#label_3').text("");
            $('#label_4').text("");
            $('#label_5').text("");
            $('#matriz_label').text("");
            $('#fasta1_label').text("");
            $('#fasta2_label').text("");

        }
  
        else { 

 
        }
       
    });


       $("#matriz").on('change', function (event){

        event.preventDefault();
        var propiedad = document.getElementById("matriz").files[0];
        
        //var nombre_imagen = propiedad.name;
        //var extension_image = nombre_imagen.split('.').pop().toLowerCase();
       // if(jQuery.inArray(extension_image, ['gif', 'png', 'jpg', 'jpeg']) == -1)
        //{
         //   alert("No es un archivo de imagen");
        //}
        var image_size = propiedad.size;
        if(image_size > 2000000) {
            alert("El archivo es muy grande");
        }
        else {
            var form_data = new FormData();
            form_data.append("file", propiedad);

            $.ajax({
                data : form_data,
                type : 'POST', 
                url: '/mostrar',
                contentType: false,
                cache: false,
                processData: false
            })
            .done(function(data) {
                if(data.error) {
                    console.log("Error");
                }
                else {
                   // $("#imagen").prop("src", '/static/images/' + data.name);
                }
            });
        }        
    });

     $("#fasta1").on('change', function (event){

        event.preventDefault();
        var propiedad = document.getElementById("fasta1").files[0];
        
        //var nombre_imagen = propiedad.name;
        //var extension_image = nombre_imagen.split('.').pop().toLowerCase();
       // if(jQuery.inArray(extension_image, ['gif', 'png', 'jpg', 'jpeg']) == -1)
        //{
         //   alert("No es un archivo de imagen");
        //}
        var image_size = propiedad.size;
        if(image_size > 2000000) {
            alert("El archivo es muy grande");
        }
        else {
            var form_data = new FormData();
            form_data.append("file", propiedad);

            $.ajax({
                data : form_data,
                type : 'POST', 
                url: '/guardar_fasta1',
                contentType: false,
                cache: false,
                processData: false
            })
            .done(function(data) {
                if(data.error) {
                    console.log("Error");
                }
                else {
                   // $("#imagen").prop("src", '/static/images/' + data.name);
                }
            });
        }        
    });


     $("#fasta2").on('change', function (event){

        event.preventDefault();
        var propiedad = document.getElementById("fasta2").files[0];
        
        //var nombre_imagen = propiedad.name;
        //var extension_image = nombre_imagen.split('.').pop().toLowerCase();
       // if(jQuery.inArray(extension_image, ['gif', 'png', 'jpg', 'jpeg']) == -1)
        //{
         //   alert("No es un archivo de imagen");
        //}
        var image_size = propiedad.size;
        if(image_size > 2000000) {
            alert("El archivo es muy grande");
        }
        else {
            var form_data = new FormData();
            form_data.append("file", propiedad);

            $.ajax({
                data : form_data,
                type : 'POST', 
                url: '/guardar_fasta2',
                contentType: false,
                cache: false,
                processData: false
            })
            .done(function(data) {
                if(data.error) {
                    console.log("Error");
                }
                else {
                   // $("#imagen").prop("src", '/static/images/' + data.name);
                }
            });
        }        
    });

    $('form').on('submit', function(event) {
        event.preventDefault();     
        $.ajax({ 
            url: '/calcular',
            data: { valor_1: $('#valor_1').val(),
                    valor_2: $('#valor_2').val(),
                    valor_3: $('#valor_3').val(),
                    valor_4: $('#valor_4').val(),
                    valor_5: $('#valor_5').val(),

                   // valor_r: $('#valor_r').val(),
                    operador: $('#operador').val()
                },
            type: 'POST'
        }).done(function(data) {
     
           // var file = '/static/output/'+data.metodo
            var file = '/static/output/' +data.metodo+'.txt',
            timestamp = (new Date()).getTime(),
            new_file = file + '?_=' + timestamp;

            $('#resultado_bio').empty();

             jQuery.get(new_file, function (txt) {

                var lines = txt.split("\n");
                $.each(lines, function (n, elem) {
                    $('#resultado_bio').append('<div>' + elem + '</div>');

                });
                console.log(lines);    
            });

            
        }).fail(function() {
            console.log('Failed');
        });        
    });     

});