const mensajeSesion = document.getElementById('mensaje-sesion');

// Función para mostrar mensajes de error
function showErrorMessage(message) {
  mensajeSesion.innerHTML = `<div class="alert alert-danger mt-2">${message}</div>`;
}

// Manejar la respuesta del servidor (asumiendo que el servidor envía un JSON con un campo 'error')
const form = document.querySelector('form');
form.addEventListener('submit', async (event) => {
  event.preventDefault(); // Evitar el envío del formulario por defecto

  const formData = new FormData(form);
  const response = await fetch('/login/', { 
    method: 'POST',
    body: formData,
  });

  if (response.ok) {
    // Redireccionar a la página principal o la página deseada después del inicio de sesión exitoso
    window.location.href = '/'; 
  } else {
    const data = await response.json();
    if (data.error === 'invalid_login') {
      showErrorMessage('Contraseña incorrecta.');
    } else if (data.error === 'missing_password') {
      showErrorMessage('Falta contraseña.');
    } else {
      showErrorMessage('Error al iniciar sesión. Por favor, inténtelo de nuevo.');
    }
}