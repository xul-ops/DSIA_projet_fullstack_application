import fetch from '@/utils/fetch';

// get the movie detail page by movie id
export function findMovieById(id) {
    return fetch({
        url: `/movies/getMovieById/${id}`,
        method: 'GET',
    });
}

// get the movies list
export function findMovieList(params) {
    return fetch({
        url: `/movies/leaderBoard/`,
        method: 'GET',
        params
    });
}


// // get the movies search list
// export function findMovieSearchList(params) {
//     return fetch({
//         url: `movies/searchList`,
//         method: 'GET',
//         params
//     });
// }

//get the movies search list: post
export function searchMovieList(params) {
    return fetch({
        url: '/movies/movieSearchList/',
        method: 'GET',
        params
    });
}
