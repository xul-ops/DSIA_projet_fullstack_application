import fetch from '@/utils/fetch';


export function login(data) {
  data = `username=${data.username}&password=${data.password}`
  return fetch({
    url: "/user/login",
    method: "post",
    headers: { "content-type": "application/x-www-form-urlencoded" },
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