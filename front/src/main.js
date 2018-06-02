// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from "vue";
import Vuetify from "vuetify";
import "vuetify/dist/vuetify.min.css";
import App from "./App";
import router from "./modules/router";
import axios from "axios";

// loads the Icon plugin
Vue.use(Vuetify, {
  theme: {
    primary: "#fb9793",
    secondary: "#adc7ef",
    accent: "#ee9674",
    error: "#f2869d"
  }
});
Vue.config.productionTip = process.env.NODE_ENV === "production";
axios.defaults.withCredentials = true;

/* eslint-disable no-new */
new Vue({
  el: "#app",
  router,
  components: { App },
  template: "<App/>"
});
