var express = require('express'),
  app = express();
  //api = require('./api.js');
  

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
  res.redirect('/position/qb'); // TODO: add a landing page
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
  console.log("id: "+parseInt(req.params.player,10))
  db.collection('players').findOne({id:parseInt(req.params.player,10)}, function(err, results) {
    if (err) {
      res.redirect('/404');
    } else {
      if (results.num_pos > 0 || results.num_neg > 0) {
        db.collection('tweets').find({'Name':results['Name']}).toArray(function(err, tweets) {
          results['tweets'] = tweets;
          res.json(results);
        });
      } else {
        res.json(results);
      }
    }
  });
});


app.listen(8000);