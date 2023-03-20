
const url = "http://localhost:8000"
async function showSamples() {
    const tbody = document.querySelector("tbody")
    await fetch(`${url}/samples`)
    .then((res)=> res.json())
    .then((body)=> {
        for (let s in body.samples){
            let newTR = document.createElement('tr')
            newTR.innerHTML = `<th scope="row">${body.samples[s].id}</th><td>${body.samples[s].co}</td><td>${body.samples[s].so2}</td><td>${body.samples[s].no2}</td><td>${body.samples[s].o3}</td><td>${body.samples[s].mp25}</td><td>${body.samples[s].mp10}</td>`;
            tbody.appendChild(newTR);
        }
    })
    .catch(console.error());
}
async function sendSamples() {
    let amostras = {
        id:1,
        so2:12,
        co:24,
        mp10:45,
        mp25:32,
        no2:56,
        o3:21   
    }
    //amostras = JSON.stringify(amostras)
    console.log(amostras)
    await axios.post(`http://localhost:8000/samples`,{
        body:amostras,
        headers: {
          'Content-Type': 'application/json'
        }
    })
    .then((response)=> response.json())
    .then((json)=> console.log(json))
    .catch((error)=> console.log(`Error is : ${error}`))
}

const testeFunc = async () => {
    await axios.post(`http://localhost:8000/teste`,{
    body: `{ "num": 1}`,
    headers: {
      'Content-Type': 'application/json'
    }
})
.then((response)=> response.json())
.then((json)=> console.log(json))
.catch((error)=> console.log(`Error is : ${error}`))
}



