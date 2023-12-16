import { createRouter, createWebHistory } from "vue-router"

const routes = [
    {
        path: "/",
        name: "article",
        component: () => import('../views/ArticlesList'),
    },
    {
        path: "/create_article",
        name: "create",
        component: () => import('../views/CreateArticle'),
    },
    {
        path: "/article_details/:id",
        name: "article_details",
        component: () => import('../views/ArticleDetail'),
        props: true,
    },
    {
        path: "/update_article/:id",
        name: "update_article",
        component: () => import('../views/UpdateArticle'),
        props: true,
    },
    {
        path: "/:catchAll(.*)",
        name: 'notFound',
        component: () => import('../views/NotFound')
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;