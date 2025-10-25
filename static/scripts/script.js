async function getAge() {
    const name = document.getElementById("name").value;
    const year = Number(document.getElementById("year").value);
    let b = true;

    if (year < 1924 || year > 2025) {
        document.getElementById("show").innerHTML = 'Zadej normální rok.';
        b = false;
    }

    if (name === "") {
        document.getElementById("show").innerHTML = 'Zadej normální jméno.';
        b = false;
    }

    if (b) {
        const url = window.location.origin + '/calc' + `?name=${name}&year=${year}`;
        const response = await fetch(url);
        const json = await response.json();
        if (json.status === 'valid') {
            document.getElementById("show").innerHTML = `${json.age}`;
        }
    }
}

document.getElementById("but").addEventListener("click", getAge);