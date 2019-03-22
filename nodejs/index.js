var express = require('express')
var fs = require('fs')
var app = express()

app.locals.pretty = true
app.set('views', './view_file')
app.set('view engine', 'pug')
app.listen(3000, () => {
	console.log("Server has been started")
})

app.get("/", (req, res) => {
	res.redirect('/hello')
})

app.get("/hello", (req, res) => {

	fs.readFile('index.html', (error, data) => {
		if(error) {
			console.log('error : '+error)
		}
		else {
			res.writeHead(200, {'ContentType':'text/html'})
			res.end(data)
		}
	})
})








