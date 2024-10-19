$(function(){
    const api_url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

    $.ajax({
        url: api_url,
        method: 'GET',
        dataType: 'json',
        success: function(data){
            const personName = data.name;
            let personDetails = '';

            personDetails += `<li>Name: ${personName}</li>`

            $('#character').html(personDetails);
            }

    });
});
