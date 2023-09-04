//endpoint contatos
let contatos = [];
const elementoParaInserirContato = document.getElementById("contato");
const endPointAPIContato =
  "https://escalation-minalba.onrender.com/minalba/contatos";

getBuscarContatos();

async function getBuscarContatos() {
  const res = await fetch(endPointAPIContato);
  contato = await res.json();
  console.table(contato);
  exibirContatosnaTela(contato);
}

const endPointAPIAdd =
  "https://escalation-minalba.onrender.com/minalba/contatos/add";

getBuscarContatos();

async function getBuscarContatos() {
  const res = await fetch(endPointAPIAdd);
  addContato = await res.json();
  console.table(addContato);
  exibirContatosnaTela(addContato);
}

let unidades = [];

const endPointAPIUnidade =
  "https://escalation-minalba.onrender.com/minalba/unidades";

getBuscarUnidades();
async function getBuscarUnidades() {
  const respostaUnidade = await fetch(endPointAPIUnidade);
  unidade = await respostaUnidade.json();
  console.table(unidade);

  const selecaoUnidade = document.getElementById("unidade");

  selecaoUnidade.innerHTML = "";

  unidade.forEach((elemento) => {
    const optionElement = document.createElement("option");
    optionElement.value = elemento.id;
    optionElement.textContent = elemento.nome;
    selecaoUnidade.appendChild(optionElement);
  });
}

function exibirContatosnaTela(Contatos) {
  Contatos.forEach((contato) => {
    elementoParaInserirContato.innerHTML += `
        <div class="blog_post" id="contato">
            <div class="container_copy">
                <h3>Nível: ${contato.nivel}</h3>
                <h1>${contato.nome}</h1>
                <p>${contato.cargo}</p>
                <p>${contato.email}</p>
                <p>${contato.telefone}</p>
                <p>Turno: ${contato.turno}</p>   
                <p>Unidade: ${contato.unidade.nome}</p>         
            </div>
        </div>
        `;
  });
}

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
  evento.preventDefault();

  const nome = document.getElementById("name").value;
  const nivel = document.getElementById("nivel").value;
  const cargo = document.getElementById("cargo").value;
  const email = document.getElementById("email").value;
  const telefone = document.getElementById("phone").value;
  const turno = document.getElementById("turno").value;
  const unidade = document.getElementById("unidade").value;
  const unidadeNumero = Number(unidade);

  //   console.log(unidade.value);

  const requestOptions = {
    method: "PUT",
    body: {
      nome: nome,
      cargo: cargo,
      nivel: nivel,
      turno: turno,
      email: email,
      telefone: telefone,
      unidade_id: unidadeNumero,
    },
  };
  fetch(endPointAPIAdd, requestOptions)
    .then((response) => response.json())
    .then((data) => {
      console.table(requestOptions["body"]);
      alert("Dados enviados com sucesso!");
      modal.close(); // Fechar o diálogo
    })
    .catch((error) => alert("Falha ao enviar dados: ", error));
});
