// Funcion para guardar un nuevo maullido
function saveMeow(event) {

    console.log(event);

    // Obtener el formulario
    const form = document.getElementById("meowFormSave");
    const data = new FormData(form);

    // Enviar los datos al servidor
    fetch(
        '/meows/create',
        {
            method: 'POST',
            body: data
        }
    )
    .then((response) => {
        saveLocalStorage("statusSave", true)
        form.reset();
        window.location.href = response.url;
    })
    .catch(
        error => console.error('Error:', error)
    );

}

// Funcion para cerrar la sesion
function logoutUser() {
    fetch(
        '/accounts/user/logout',
        {
            method: 'GET'
        }
    )
    .then((response) => {
        window.location.href = response.url;
    })
    .catch(
        error => console.error('Error:', error)
    );
}

// Funcion para Loguear un usuario
function userLogin() {

    // Obtener el formulario
    const form = document.getElementById("userLoginForm");
    const data = new FormData(form);

    // Enviar los datos al servidor
    fetch(
        '/accounts/user/login',
        {
            method: 'POST',
            body: data
        }
    )
    .then((response) => {
        form.reset();
        if (response.status != 200) {
            const Toast = initializeToast();
            Toast.fire({
                icon: 'error',
                title: 'Usuario o contraseña incorrectos'
            })
        }
        else {
            window.location.href = response.url;
        }
    })
    .catch(
        error => console.error('Error:', error)
    );

}

// Funcion para agregar un nuevo usuario
function userRegister() {

    // Obtener el formulario
    const form = document.getElementById("userRegisterForm");
    const data = new FormData(form);

    // Enviar los datos al servidor
    fetch(
        '/accounts/user/register',
        {
            method: 'POST',
            body: data
        }
    )
    .then((response) => {
        console.log(response);
        if (response.status != 200) {
            const Toast = initializeToast();
            Toast.fire({
                icon: 'error',
                title: response.message ?? 'Verifica que los campos esten correctos y las contraseñas coincidan'
            })
        }
        else {
            form.reset();
            window.location.href = response.url;
        }
    })
    .catch(
        error => console.error('Error:', error)
    );

}