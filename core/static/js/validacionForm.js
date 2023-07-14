function validarFormulario() {
  let rut = document.getElementById("rut").value;
  let nombre = document.getElementById("nombre").value;
  let usuario = document.getElementById("usuario").value;
  let email = document.getElementById("email").value;
  let telefono = document.getElementById("telefono").value;
  let ciudad = document.getElementById("ciudad").value;
  let comuna = document.getElementById("comuna").value;
  let descripcion = document.getElementById("descripcion").value;
  let genero = document.querySelector('input[name="genero"]:checked');

  let rutRegex = /^\d{9}$/;
  let nombreRegex = /^[a-zA-Z\s]+$/;

  if (rut === "") {
    showModal("Por favor, ingresa tu rut.", "error");
    return false;
  }

  if (!rutRegex.test(rut)) {
    showModal("Ingresar rut sin puntos ni guion.", "error");
    return false;
  }

  if (descripcion.length < 5 || descripcion.length > 100) {
    showModal("La descripción debe tener entre 5 y 100 caracteres.", "error");
    return false;
  }

  if (!/^\d{8}$/.test(telefono)) {
    showModal("El número de teléfono debe contener exactamente 8 dígitos.", "error");
    return false;
  }

  return true;
}

document.getElementById("myForm").addEventListener("submit", function(event) {
  event.preventDefault();

  if (validarFormulario()) {
    var rut = document.getElementById("rut").value;
    var nombre = document.getElementById("nombre").value;
    var usuario = document.getElementById("usuario").value;
    var email = document.getElementById("email").value;
    var telefono = document.getElementById("telefono").value;
    var genero = document.querySelector('input[name="genero"]:checked').value;
    var ciudad = document.getElementById("ciudad").value;
    var comuna = document.getElementById("comuna").value;
    var descripcion = document.getElementById("descripcion").value;

    var message =
      "¡Formulario de registro completo!<br><br>" +
      "Rut: " +
      rut +
      "<br>Nombre: " +
      nombre +
      "<br>Usuario: " +
      usuario +
      "<br>Email: " +
      email +
      "<br>Número de Contacto: " +
      telefono +
      "<br>Género: " +
      genero +
      "<br>Ciudad: " +
      ciudad +
      "<br>Comuna: " +
      comuna +
      "<br>Descripción: " +
      descripcion;

    showModal(message, "success");

    document.getElementById("myForm").reset();
  }
});

function showModal(message, status) {
  var modal = document.getElementById("myModal");
  var modalMessage = document.getElementById("modal-message");

  modal.style.display = "block";
  modalMessage.innerHTML = message;

  modal.classList.remove("error", "success");
  modal.classList.add(status);

  var closeBtn = document.getElementsByClassName("close")[0];
  closeBtn.onclick = function() {
    modal.style.display = "none";
  };

  window.onclick = function(event) {
    if (event.target === modal) {
      modal.style.display = "none";
    }
  };
}

document.getElementById("descripcion").addEventListener("input", function() {
  var maxChars = 100;
  var currentChars = this.value.length;
  var remainingChars = maxChars - currentChars;
  
  var counterElement = document.getElementById("caracteres-restantes");
  counterElement.textContent =  + currentChars + "/" + maxChars;
});

