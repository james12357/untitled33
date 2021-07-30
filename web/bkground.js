var mysql = require('mysql');
var http = require('http');
var URL = require("url");
var crypto = require("crypto")
var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'james',
  password : '123456',
  database : 'testdb'
});
function cry(passw){
  var md5 = crypto.createHash('sha128');
	var password = md5.update(passw).digest('base64');
	return password;
}


connection.connect();
http.createServer(function (request, response) {
  let args = URL.parse(request.url, true).query;
  if(args.type === "register"){
    if (args.name, args.passwd){
      connection.query('INSERT INTO table_name (name,hash128)VALUES (?,?);', [args.name, cry(args.passw)], function (error, results, fields) {
      if (error) throw error;
    });}
    }
  
  response.writeHead(200, {'Content-Type': 'text/plain'});
  response.end('Hello World\n');
}).listen(8888);

// 终端打印如下信息
console.log('Server running at http://127.0.0.1:8888/');

 
connection.query('SELECT * FROM passwd_test', function (error, results, fields) {
  if (error) throw error;
  console.log(results[0].name);
});