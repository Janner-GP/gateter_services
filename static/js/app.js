// Eventos que deben ocurrir al cargar cualquier página
document.addEventListener('DOMContentLoaded', (event) => {
    launchToast("statusSave");
    removeLocalStorage("statusSave");
});

// Funcion para guardar en el LocalStorage
function saveLocalStorage(key, value) {
    localStorage.setItem(key, value)
}

// Funcion para obtener un valor del LocalStorage
function getLocalStorage(key) {
    return localStorage.getItem(key)
}

// Funcion para remover un valor del LocalStorage
function removeLocalStorage(key) {
    localStorage.removeItem(key)
}

// Funcion para inicializar el Toast
function initializeToast(){
    const Toast = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 4000, // El Toast se muestra por 3 segundos
        timerProgressBar: true,
        didOpen: (toast) => {
          toast.addEventListener('mouseenter', Swal.stopTimer)
          toast.addEventListener('mouseleave', Swal.resumeTimer)
        }
    });

    return Toast;
}

// Funcion para lanzar el Toast
function launchToast(storageKey){
    const isSave = getLocalStorage(storageKey)
    const Toast = initializeToast()

    if (isSave) {
        Toast.fire({
            icon: 'success',
            title: 'Maullido guardado correctamente'
        })
    }
}