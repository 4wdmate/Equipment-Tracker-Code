const side = document.getElementsByClassName("side")

const sideStuff = [
    {text: "1"},
    {text: "c"},
    {text: "b"},
    {text: "a"},
    {text: "uw"},
]

side.innerHTML = ""
sideStuff.forEach((stuff) => {
    console.log(`uwu: ${stuff.text}`)
    side.innerHTML += `<h6>${stuff.text}</h6>\n`
})