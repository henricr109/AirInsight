const sendSamples = async () => {
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
    console.log(samples);
    await axios.post(`http://localhost:3000/dataSamples/${samples}`)
    .then(
        console.log('tentei enviar')
    )
    .catch(
        console.log('não recebeu o backend')
    )
};