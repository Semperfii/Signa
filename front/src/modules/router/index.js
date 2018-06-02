import Vue from "vue";
import Router from "vue-router";
import Login from "@/components/auth/Login";
import StudentHome from "@/components/StudentHome";
import StudentTopics from "@/components/StudentTopics";
<<<<<<< HEAD
import StudentQuestion from "@/components/StudentQuestion";
=======
import TeacherHome from "@/components/TeacherHome";
>>>>>>> 7cd8b9dbf3f2d63be17ad62d97905e26f128c752

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
    },
    {
<<<<<<< HEAD
      path: "/student/question",
      name: "StudentQuestion",
      component: StudentQuestion
=======
      path: "/teacher/home",
      name: "Teacher/home",
      component: TeacherHome
>>>>>>> 7cd8b9dbf3f2d63be17ad62d97905e26f128c752
    }
  ]
});
