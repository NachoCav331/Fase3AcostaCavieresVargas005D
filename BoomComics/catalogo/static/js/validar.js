function validar()
{
    name = document.getElementById('nombre').value;
    email = document.getElementById('correo').value; 
    telephone = document.getElementById('telefono').value;
    tipoM = document.getElementById('tipoDeMensaje').selectedIndex;
    mensaje = document.getElementById('mensaje').value;

    if (tipoM == null || tipoM == 0)
    {
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'Debe seleccionar una opcion'
        })
        document.datos.tipoM.focus();
        return false;
    }

    if(name == null || name.length==0 || /^\s+$/.test(name))
    {
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'Ingresar nombre valido'
        })
        document.getElementById('nombre').value="";
        document.datos.name.focus();
        return false;
    }

    if(!(/^\d{9}$/.test(telephone)) )
    {
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'Ingresar telefono valido'
        })
        document.datos.telephone.focus();
        return false;
    }    
    
    if(email == null || email.length==0 || /^\s+$/.test(email))
     {
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'Ingresar email valido'
        })
        document.datos.email.focus();
        return false;
    }
    if(mensaje == null || mensaje.length==0)
     {
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'Escribir un mensaje'
        })
        document.datos.email.focus();
        return false;
    }
    else
    {
        Swal.fire({
            icon: 'success',
            title: 'Enviado',
            text: 'Su mensaje ha sido enviado, en breve enviaremos la respuesta a su correo',
            timer: 4000,
            showConfirmButton: false
        }).then(function()
        {
            window.location.href = 'http://127.0.0.1:8000/catalogo/';
        });
    }

    return true;
    
    
}



