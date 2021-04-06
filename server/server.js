var http = require('http');
var express = require('express');
var cors = require('cors');
var fs = require('fs');
var app = express();

const PORT = 8080;

app.use(cors());

app.get("/results", (req, res) => {
  const rawData = fs.readFileSync("../python/similarityResults.json");
  res.send({ results: JSON.parse(rawData) });
  console.log("We did it bois");
});

app.listen(PORT, () => {
  console.log(`App is listening at port: ${PORT}`);
})
