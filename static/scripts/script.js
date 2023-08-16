//endpoint contatos
 let contatos = []
const elementoParaInserirContato = document.getElementById("contato")
const endPointAPIContato = 'https://escalation-minalba.onrender.com/minalba/contatos'

getBuscarContatos()

async function getBuscarContatos() {
    const res = await fetch(endPointAPIContato)
    contato = await res.json()
    console.table(contato)
    exibirContatosnaTela(contato)

}

function exibirContatosnaTela(Contatos) {
    Contatos.forEach(contato => {
        elementoParaInserirContato.innerHTML += `
        <div class="blog_post" id="contato">
            <div class="container_copy">
                <h3>${contato.nivel}</h3>
                <h1>${contato.nome}</h1>
                <p>${contato.cargo}</p>
                <p>${contato.email}</p>
                <p>${contato.telefone}</p>
                <p>${contato.turno}</p>
                <a class="btn_primary" href='#' target="_blank"><i class="fa-solid fa-pen"></i></a>
            </div>
        </div>
        `
    });
}

//endpoint unidades

let unidades = []

const endPointAPIUnidade = 'https://escalation-minalba.onrender.com/minalba/unidades'

getBuscarUnidades()
async function getBuscarUnidades() {
    const respostaUnidade = await fetch(endPointAPIUnidade)
    unidade = await respostaUnidade.json()
    console.table(unidade)
}