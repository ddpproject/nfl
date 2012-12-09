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
  res.redirect('/about'); // TODO: add a landing page
});

app.get('/about', function(req, res) {
  res.render('about.jade');
});

app.get('/negative', function(req, res) {
  db.collection('players').find({num_neg:{$gt:0}}).sort({'num_neg': -1}).toArray(function(err, results) {
    if (err) {
      res.redirect('/404');
    } else {
      res.render('team.jade', {results: results});
    }
  });
});

app.get('/positive', function(req, res) {
  db.collection('players').find({num_pos:{$gt:0}}).sort({'num_pos': -1}).toArray(function(err, results) {
    if (err) {
      res.redirect('/404');
    } else {
      res.render('team.jade', {results: results});
    }
  });
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

app.get('/team/:team', function(req, res) {
  db.collection('players').find({'Team': req.params.team.replace(/_/g,' ')}).sort({'Name':1}).toArray(function(err, results) {
    if (err) {
      res.redirect('/404');
    } else {
      res.render('team.jade', {results: results});
    }
  });
});

app.get('/player/:player', function(req, res) {
  console.log("id: "+parseInt(req.params.player,10))
  console.log('type: '+req.query.type);
  db.collection('players').findOne({id:parseInt(req.params.player,10)}, function(err, results) {
    if (err) {
      res.redirect('/404');
    } else {
      if (results.num_pos > 0 || results.num_neg > 0) {
        db.collection('tweets').find({'Name':results['Name']}).toArray(function(err, tweets) {
          results['tweets'] = tweets;
          if (req.query.type == 'json') {
            res.json(results);
          } else {
            res.render('player.jade', {player: results});
          }
        });
      } else {
        if (req.query.type == 'json') {
          res.json(results);
        } else {
          res.render('player.jade', {player: results});
        }
      }
    }
  });
});


app.listen(8000);