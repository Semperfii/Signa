import axios from 'axios'
import router from '../router/index'

let user = {
  authenticated: false,
  profile: JSON.parse(localStorage.getItem('profile'))
};

function login(context, email, password) {
  axios.post(process.env.AUTH_URL + '/login', {
    email: email,
    password: password
  })
    .then((response) => {
      if (response.status === 200) {
        localStorage.setItem('access_token', response.data.access_token);
        localStorage.setItem('refresh_token', response.data.refresh_token);
        checkAuth().then(() => {
         router.push("/" + user.home + "/home");
        });
      } else {
        context.error = true;
      }
    })
    .catch(function (error) {
      context.error = true;
      context.errorMessage = '';
      if (error.response) {
        context.errorMessage = error.response.data.error;
      } else {
        console.log(error);
      }
    });
}

function refresh(context) {
  return new Promise(((resolve, reject) => {
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('refresh_token');
    axios.post(process.env.AUTH_URL + '/refresh')
      .then(function (response) {
        if (response.status === 200) {
          localStorage.setItem('access_token', response.data.access_token);
          checkAuth().then(() => {
            resolve();
          }, () => {
            reject();
          });
        } else {
          reject();
        }
      }, (error) => {
        reject();
      });
  }));
}

function logout() {
  localStorage.removeItem('access_token');
  localStorage.removeItem('profile');
  axios.defaults.headers.common['Authorization'] = '';
  user.authenticated = false;
  user.profile = null;
  router.replace('/');
}

function checkAuth() {
  return new Promise((resolve, reject) => {
    const jwt = localStorage.getItem('access_token');
    if (jwt !== null) {
      user.authenticated = true;
      axios.defaults.headers.common['Authorization'] = 'Bearer ' + jwt;
      axios.get(process.env.API_URL + '/me')
        .then(function (response) {
          user.authenticated = response.status === 200;
          if (!user.authenticated) {
            throw new Error(response);
          } else {
            localStorage.setItem('profile', JSON.stringify(response.data));
            user.profile = response.data;
            if (user.profile.type === 0) {
              user.home = "student";
            } else if (user.profile.type === 1) {
              user.home = "teacher";
            } else if (user.profile.type === 2) {
              user.home = "parent";
            }
            resolve();
          }
        })
        .catch(function (error) {
          if (error.response && error.response.status === 401) {
            refresh().then(() => {
              resolve();
            }, () => {
              reject();
              logout();
            });
          } else {
            user.authenticated = false;
            reject();
            logout();
          }
        });
    } else {
      user.authenticated = false;
      reject();
    }
    if (!user.authenticated) {
      router.replace('/');
    }
  });
}

export default {
  user,
  login,
  logout,
  checkAuth
}
