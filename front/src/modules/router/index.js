import Vue from "vue";
import Router from "vue-router";
import Login from "@/components/auth/Login";
import StudentHome from "@/components/StudentHome";
import ParentStatistic from "@/components/ParentStatistic";
import StudentQuestion from "@/components/StudentQuestion";
import TeacherHome from "@/components/TeacherHome";
import StudentOpponent from "@/components/StudentOpponent";

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
      path: "/student/question",
      name: "StudentQuestion",
      component: StudentQuestion
    },
    {
      path: "/teacher/home",
      name: "Teacher/home",
      component: TeacherHome
    },
    {
      path: "/parent/statistic",
      name: "ParentStatistic",
      component: ParentStatistic
    },
    {
      path: "/student/opponent",
      name: "StudentOpponent",
      component: StudentOpponent
    }
  ]
});
