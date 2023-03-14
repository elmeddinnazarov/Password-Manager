$('input[type=submit]').on('click', function(e){
    e.preventDefault();
    $('form').addClass('ahashakeheartache');
  });
  
  $('form').on('webkitAnimationEnd oanimationend msAnimationEnd animationend', function(e){
    $('form').delay(200).removeClass('ahashakeheartache');
  });
  