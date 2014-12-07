
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../favicon.ico">

    <title>Jitalk - the new way to talk!</title>

    <!-- Bootstrap core CSS -->
    <!-- <link href="/static/bootstrap.min.css" rel="stylesheet"> -->
    <link rel="stylesheet" type="text/css" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
    <link href='http://fonts.googleapis.com/css?family=Roboto:400,300&subset=latin,latin-ext' rel='stylesheet' type='text/css'>

    <link href="/static/style.css" rel="stylesheet">

    <!-- Firebase -->
    <script src="https://cdn.firebase.com/js/client/2.0.6/firebase.js"></script>
  </head>

  <body>
    <div class="username">afahim</div>
    <div class="roomID">{{roomID}}</div>
    <div class="language">english</div>

    <div class="container">

      <div class="people">
        <div class="person other-person">Mahmoud</div>
        <div class="person this-person">Afnan</div>
      </div>

      <div class="chatbox" id="chatbox">
      </div>

      <div class="chat-textfield">
        <span class="input-field" contentEditable="true"></span>
        <span class="submit arrow-right glyphicon glyphicon-arrow-right"></span>
      </div>

    </div><!-- /.container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="/static/script.js"></script>
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>

  </body>
</html>
