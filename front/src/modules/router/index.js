import Vue from "vue";
import Router from "vue-router";
import Login from "@/components/auth/Login";
import StudentHome from "@/components/StudentHome";
import ParentStatistic from "@/components/ParentStatistic";
import StudentQuestion from "@/components/StudentQuestion";
import TeacherHome from "@/components/TeacherHome";
import DuelAnimation from "@/components/DuelAnimation";
import StudentOpponent from "@/components/StudentOpponent";
import StudentSummary from "@/components/StudentSummary";

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
      path: "/student/question/:type",
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
      path: "/duel/animation",
      name: "DuelAnimation",
      component: DuelAnimation
    },
    {
      path: "/student/opponent",
      name: "StudentOpponent",
      component: StudentOpponent
    },
    {
      path: "/student/summary",
      name: "StudentSummary",
      component: StudentSummary
    }
  ]
});
