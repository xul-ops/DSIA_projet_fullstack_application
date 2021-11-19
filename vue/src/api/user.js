import fetch from '@/utils/fetch';


export function login(data) {
  return fetch({
    url: "/user/login/",
    method: "post",
    data,
  });
}


export function register(data) {
  return fetch({
    url: "/user/inscription/",
    method: "post",
    data,
  });
}