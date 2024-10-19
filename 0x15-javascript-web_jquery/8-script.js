$(function(){
    const api_url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

    $.ajax({
        url: api_url,
        method: 'GET',
        dataType: 'json',
        success: function(data){
            const movies = data.results;
            let movieList = '';

            movies.forEach(function(movie) {
                movieList += `<li>${movie.title}</li>`;
            });

            $('#list_movies').html(movieList);
        }

    });
});
