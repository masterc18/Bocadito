const express = require('express');
const app = express();
const fs = require('fs');
const indexHTML = fs.readFileSync('./bocadito.html')

app.get('/', (req, res)=> res.send(indexHTML))
const PORT = 3000
app.listen(PORT)
console.log('listening in port', PORT)