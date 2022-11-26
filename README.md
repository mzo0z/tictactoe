# tictactoe
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>mzooz</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='/assets/vendors/bootstrap/css/bootstrap.min.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='/assets/css/basic.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='/assets/css/home.css') }}">


    <script src="{{ url_for('static', filename='/assets/js/jquery/jquery-3.6.0.min.js') }}"></script>

    <script src="{{ url_for('static', filename='/assets/vendors/bootstrap/js/bootstrap.bundle.min.js') }}"></script>


  </head>
  <body class="main">
    <nav class="navbar navbar-expand-lg navbar-dark  bg-dark">
      <a class="navbar-brand" href="">mzooz</a>
      
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a class="nav-link" href="/home">الصفحة الرئيسية<span class="sr-only">(current)</span></a>
          </li>
        </ul>
        
        <ul class="navbar-nav mr-auto main-mzooz-icon">    
          <li class="nav-item active">
            <img class="navbar-brand " src="{{url_for('static', filename='assets/images/mzooz.svg')}}" alt="mzooz icon" width="15%">
          </li>
        </ul>
        

          <li class="nav-item dropdown">
            <a class="dropdown-toggle" style="text-decoration:none;color: aqua;" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">اللغة</a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown" style="margin-right:auto; background-color: rgb(44, 44, 73);">
              <a class="dropdown-item" href="#" >العربية</a>
              <a class="dropdown-item" href="#" >English</a>
            </div>
          </li>

      </div>
    </nav>
  <div class="main_things">
    <img class="center mzooz-welcome-gif" src="{{url_for('static', filename='assets/images/welcome.gif')}}" alt="welcome gif">
    <a class="add-bot-button btn btn-success" target="_blank" href="{{invite_bot}}" role="button">إضافة البوت لـ ديسكورد</a>
    <h1 class="mzooz-bot-text">mzooz bot</h1>

    {% if not authorized %}
      {% if status %}
      <a class="go-on-button btn btn-secondary border border-dark rounded-pill"  href="/login" role="button">الدخول</a>
      {% else %}
      <a class="go-on-button btn btn-secondary border border-dark rounded-pill disabled"  href="#" aria-disabled="true" role="button">الدخول</a>
      {%endif %} 
    {% else %}
      {% if status %}
      <a class="go-on-button btn btn-secondary border border-dark rounded-pill" href="/servers" role="button">الدخول</a>
      {% else %}
      <a class="go-on-button btn btn-secondary border border-dark rounded-pill disabled"  href="#" aria-disabled="true" role="button">الدخول</a>
      {%endif %}
    {%endif %}
    <img class="center mzooz-welcome-gif" src="{{url_for('static', filename='assets/images/line.gif')}}" alt="line gif">
  </div>
  <div class="mzooz-features-right">
    <p class="col-6 security-text yellow-text">حماية للسيرفر, لاتقلق بعد الآن سيرفرك بأمان معي</p>
    <img class="security-icon" src="{{url_for('static', filename='assets/images/shield.svg')}}" alt="shield">        
  </div>
    
  <div class="mzooz-features-left">
    <img class="settings-icon" src="{{url_for('static', filename='assets/images/settings.svg')}}" alt="settings">        
    <p class="col-6 settings-text blue-text ">سيستم, مراقبة السيرفر  وعدة اوامر قم بأكتشافها</p>
  </div>

  <div class="mzooz-features-right">
    <img class="ticket-icon" src="{{url_for('static', filename='assets/images/ticket.svg')}}" alt="ticket">        
    <p class="col-6 ticket-text yellow-text">تيكت</p>
  </div> 

  <div class="mzooz-features-left">
    <img class="controller-icon" src="{{url_for('static', filename='assets/images/controle.svg')}}" alt="controller">        
    <p class="col-6 controller-text blue-text ">العاب, قم بتحدي اصدقائك وفز عليهم!</p>
  </div>

  <div class="mzooz-features-right">
    <img class="moon-icon" src="{{url_for('static', filename='assets/images/moon.svg')}}" alt="moon">        
    <p class="col-6 moon-text yellow-text">ادعية وآيات</p>
  </div>

  <div class="mzooz-features-left">
    <img class="reaction-icon" src="{{url_for('static', filename='assets/images/reaction.svg')}}" alt="reaction">        
    <p class="col-6 reaction-text blue-text ">رياكشن كوماند قم بالحصول على الرتبة بأقل من 10 ثوان</p>
  </div>

  <footer>
    <nav class="mzooz-footer navbar navbar-expand-lg navbar-dark ">
          <a class="nav-link urls" href="#">شروط الخدمة</a>
          <a class="nav-link urls" href="#">سياسة الخصوصية</a>
          <a class="nav-link urls" href="#">تواصل معنا</a>
          <a class="nav-link icon" href="#"><img src="{{url_for('static', filename='assets/images/discord.svg')}}"width="25px"></a>
          <a class="nav-link icon" href="#"><img src="{{url_for('static', filename='assets/images/mzooz.svg')}}"  width="25px"></a>
    </nav>
  </footer>

  <div class="bot-status">
    {% if status %}
    <img class="bot-icon" src="{{url_for('static', filename='assets/images/online.svg')}}" alt="online">        
    {% else %}
    <img class="bot-icon" src="{{url_for('static', filename='assets/images/offline.svg')}}" alt="online">        
    {%endif %}
    <p class="col-6 bot-text">:حالة البوت</p>
  </div>
  <div class="bot-servers">
    <p class="col-6 bot-servers-text">{{servers}} :عدد السيرفرات</p>
  </div>

</body>
</html>
