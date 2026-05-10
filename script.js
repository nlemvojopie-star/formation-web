function changerMessage() {
    let message = document.getElementById("messageSpecial");
    message.textContent = "🚀 Bravo Jopie ! Tu contrôles la page avec JavaScript !";
    message.style.color = "#2980b9";
    message.style.fontWeight = "bold";
    message.style.fontSize = "1.2rem";
}
function additionner() {
    let n1 = Number(document.getElementById("nombre1").value);
    let n2 = Number(document.getElementById("nombre2").value);
    let resultat = document.getElementById("resultat");
    resultat.textContent = "Résultat : " + (n1 + n2);
    resultat.style.color = "#27ae60";
    resultat.style.fontWeight = "bold";
}

function multiplier() {
    let n1 = Number(document.getElementById("nombre1").value);
    let n2 = Number(document.getElementById("nombre2").value);
    let resultat = document.getElementById("resultat");
    resultat.textContent = "Résultat : " + (n1 * n2);
    resultat.style.color = "#e74c3c";
    resultat.style.fontWeight = "bold";
}