const button = document.querySelector("button");
const modal = document.querySelector("dialog");
const buttonClose = document.getElementById("close");
const salvarBtn = document.getElementById("salvar");

button.onclick = function () {
  modal.showModal();
};

buttonClose.onclick = function () {
  modal.close();
};

salvarBtn.addEventListener("click", function (evento) {
  evento.preventDefaut();

  const formNome = document.getElementById("name").value;
  const formNivel = document.getElementById("nivel").value;
  const formCargo = document.getElementById("cargo").value;
  const formEmail = document.getElementById("email").value;
  const formTelefone = document.getElementById("phone").value;
  const formTurno = document.getElementById("turno").value;
  const formUnidade = document.getElementById("unidade").value;

  const requestOptions = {
    method: "PUT",
    body: JSON.stringify({
      nome,
      nivel,
      cargo,
      email,
      phone,
    }),
  };
});
