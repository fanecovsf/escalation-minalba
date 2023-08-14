//endpoint contatos
 let contatos = []

const endPointAPIContato = 'https://escalation-minalba.onrender.com/minalba/contatos'

getBuscarContatos()

async function getBuscarContatos() {
    const res = await fetch(endPointAPIContato)
    contato = await res.json()
    console.table(contato)

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