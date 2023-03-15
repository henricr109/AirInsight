/*function sendSamples() {
    let pm25 = document.getElementById('pm25').value,
    pm10 = document.getElementById('pm10').value,
    co = document.getElementById('co').value,
    so2 = document.getElementById('so2').value,
    o3 = document.getElementById('o3').value,
    no2 = document.getElementById('no2').value;
    const samples = {
        pm25,
        pm10,
        co,
        so2,
        o3,
        no2
    }
    JSON.stringify(samples);
    fetch(`http://127.0.0.1:8000/samples/${samples}`,"POST")
    .then((response)=> {
        console.log(response)
    })
    .catch(
        console.log('não recebeu o backend')
    )
};*/

async function showSamples() {
    await fetch("http://localhost:8000/samples")
    .then((res)=> res.json())
    .then((json)=> console.log(json))
    .catch(console.error());
}