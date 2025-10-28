async function getAge() {
    const name = document.getElementById("name").value;
    const year = Number(document.getElementById("year").value);

    if (year < 1924 || year > 2025) {
        document.getElementById("show").innerHTML = 'Zadej normální rok (mezi 1925 a 2024).';
    }

    else if (name === "") {
        document.getElementById("show").innerHTML = 'Zadej normální jméno.';
    }

    else {
        const url = window.location.origin + '/calc' + `?name=${name}&year=${year}`;
        const response = await fetch(url);
        const json = await response.json();
        if (json.status === 'valid') {
            document.getElementById("show").innerHTML = `${json.age}`;
        }
    }
}

document.getElementById("but").addEventListener("click", getAge);