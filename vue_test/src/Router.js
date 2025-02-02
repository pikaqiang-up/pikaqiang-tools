import { createRouter, createWebHashHistory } from "vue-router";

const router = createRouter({
    history: createWebHashHistory(),
    routes: [
        {
            path: "/",
            name: "Home",
            component: () => import("@/views/Main.vue"),
        },
        {
            path: "/img",
            name: "Img",
            component: () => import("@/views/ImageViewer.vue"),
        }
    ],
});
export default router;
