$().ready(function() {
  $('a[target=_blank]').each(function() {
      if ($(this).html().indexOf('images/') == 0) {
          var path = $(this).attr('href');
          path = path.substring(0, path.lastIndexOf('/'))
                  + '/thumbs_150'
                  + path.substring(path.lastIndexOf('/'));
          $(this).parent().after('<a style="margin-left: 10em" href="'
                  + $(this).attr('href') + '" target="_blank"><img src="'
                  + path + '" alt="image"/></a>');
      }
  });
});