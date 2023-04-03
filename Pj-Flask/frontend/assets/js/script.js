const co = parseFloat(document.getElementById('pollu-co'))
const so2 = parseFloat(document.getElementById('pollu-so2'))
const no2 = parseFloat(document.getElementById('pollu-no2'))
const o3 = parseFloat(document.getElementById('pollu-o3'))
const mp25 = parseFloat(document.getElementById('pollu-mp25'))
const mp10 = parseFloat(document.getElementById('pollu-mp10'))

url = "http://localhost:5000"

function passarAmostraParaOBackend(event) {
  event.preventDefault();
  
  const item = { 
    co:co,
    so2:so2,
    no2:no2,
    o3:o3,
    mp25:mp25,
    mp10:mp10  
  };
  fetch(`${url}/sample`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(item)
  })
  .then((response)=> response.json())
  .then((json)=> console.log(json))
  .catch((error)=> console.log(`Error is : ${error}`))
}

async function mostrarAmostrasNaTabela() {
    const tbody = document.querySelector("tbody")
    await fetch(`${url}/samples`)
    .then((res)=> res.json())
    .then((body)=> {
        for (let s in body.samples){
            let novaLinhaDaTabela = document.createElement('tr')
            novaLinhaDaTabela.innerHTML = `<th scope="row">${body.samples[s].id}</th><td>${body.samples[s].co}</td><td>${body.samples[s].so2}</td><td>${body.samples[s].no2}</td><td>${body.samples[s].o3}</td><td>${body.samples[s].mp25}</td><td>${body.samples[s].mp10}</td>`;
            tbody.appendChild(novaLinhaDaTabela);
        }
    })
    .catch(console.error());
  }
