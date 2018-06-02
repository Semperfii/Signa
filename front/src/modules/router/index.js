import Vue from "vue";
import Router from "vue-router";
import Login from "@/components/auth/Login";
import StudentHome from "@/components/StudentHome";
import StudentTopics from "@/components/StudentTopics";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "Login",
      component: Login
    },
    {
      path: "/student/home",
      name: "StudentHome",
      component: StudentHome
    },
    {
      path: "/student/topics",
      name: "Student/topics",
      component: StudentTopics
    }
  ]
});
