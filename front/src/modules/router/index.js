import Vue from "vue";
import Router from "vue-router";
import Login from "@/components/auth/Login";
import Callback from "@/components/auth/Callback";
import Main from "@/components/Main";
import AddMatch from "@/components/AddMatch";
import StudentHome from "@/components/StudentHome";
import StudentTopics from "@/components/StudentTopics";
import StudentQuestion from "@/components/StudentQuestion";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "Login",
      component: Login
    },
    {
      path: "/auth/callback",
      name: "Callback",
      component: Callback
    },
    {
      path: "/main",
      name: "Main",
      component: Main
    },
    {
      path: "/main/add",
      name: "AddMatch",
      component: AddMatch
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
    },
    {
      path: "/student/question",
      name: "StudentQuestion",
      component: StudentQuestion
    }
  ]
});
