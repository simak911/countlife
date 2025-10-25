console.log('script loaded');

async function getAge(){
    console.log('getAge() called');
    const name = document.getElementById("name").value;
    const year = document.getElementById("year").value;
    const url = window.location.origin + '/calc' + `?name=${name}&year=${year}`;
    const response = await fetch(url);
    const json = await response.json();
    const status = json.status;
    if (status === 'valid') {
        const age = json.age
        document.getElementById("show").innerHTML = `${age}`;}
}

document.getElementById("but").addEventListener("click", getAge());