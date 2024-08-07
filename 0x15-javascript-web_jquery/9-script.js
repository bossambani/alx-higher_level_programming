$(function(){
    const api_url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

    $.ajax({
        url: api_url,
        method: 'GET',
        dataType: 'json',
        success: function(data){
            const helloMessage = data.hello;
           $('#hello').text(helloMessage);
            }

    });
});
