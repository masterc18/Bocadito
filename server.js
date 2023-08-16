const express = require('express');
const app = express();
const fs = require('fs');
const indexHTML = fs.readFileSync('./bocadito.html')

app.get('/', (req, res)=> res.send(indexHTML))
const PORT = 3000
app.listen(PORT)
console.log('listening in port', PORT)

const inpNombre = document.getElementById('nombre')
 //en la variable inpNombre se está guardando el elemento con el id nombre 
//para que posteriormente se pueda interactuar de manera dinamica con el o los elementos del DOM que seleccionemos, pueden seleccionarse tanto como
//getElementsByClassName o querySelector pero hay algo muy importante que no se debe de olvidar y es que antes de seleccionarlo se 
//se debe tomar como referencia al objeto document ya que se encuentra en la cuspide de la jerarquia de los elementos del DOM
//el DOM (document object model) se refiere a todos los elementos que se encuentran en  un sitio web, pueden ser tags div, section, main, label, hasta un canvas
//el proposito de JS es que podamos darle vida a esos elementos por medio de instrucciones logicas, Js se puede usar para cambiar los estilos de un elemento
//con solo un click hasta enviar y recibir datos del cliente en los servidores