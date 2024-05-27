function confirmarDelete(id) {
    Swal.fire({
        title: "Estas seguro de eliminar a este Mecanico?",
        text: "Una vez borrado no puedes recuperar la información!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Si, deseo borrarlo",
        input: "text",
        inputPlaceholder: "Escribe 'Confirmar' para continuar",
        inputValidator: (value) => {
            if (value !== "Confirmar") {
                return "Debes ingresar 'Confirmar' para continuar";
            }
        }
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: "Borrado!",
                text: "El Mecanico seleccionado fue borrado",
                icon: "success"
            }).then(function() {
                window.location.href = "/empleados/delete/" + id + "/";
            });
        }
    });
}
