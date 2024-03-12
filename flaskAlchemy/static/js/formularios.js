

setTimeout(function () {
    document.getElementById('alert').remove();
}, 2000);

function confirmarEliminacion() {
    // Mostrar un cuadro de diálogo de confirmación
    if (confirm("¿Estás seguro de eliminar el registro?")) {
        // Si el usuario hace clic en "Aceptar", enviar el formulario
        document.getElementById("eliminar-form").submit();
    } else {
        // Si el usuario hace clic en "Cancelar", no hacer nada
        return false;
    }
}