var express = require('express'),
  app = express(),
  api = require('./api.js');
  

app.configure(function() {
  app.set('views', __dirname + '/views')
  app.set('view engine', 'jade');
  app.use(express.bodyParser());
  //app.use(express.router);
  app.use('/static', express.static(__dirname + '/static'));

  app.set("db uri", 'mongodb://localhost/nfl');
});

var mongo = require('mongoq');
  db = mongo(app.get('db uri'), {safe:false});

app.get('/', function(req, res) {
  res.redirect('/404'); // TODO: add a landing page
});

app.get('/position/:position', function(req, res) {
  db.collection(req.params.position.toUpperCase()).find().sort({'Score': -1}).toArray(function(err, results) {
    if (err) {
      res.redirect('/404');
    } else {
      res.render('position.jade', {results: results});
    }
  });
});

app.get('/player/:player', function(req, res) {
  res.redirect('/404');
});


app.listen(8080);