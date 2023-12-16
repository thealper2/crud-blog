<template>
    <div class="contain">
        <h2>{{ article.date }}</h2>
        <h1>{{ article.title }}</h1>
        <p class="gradient_select">{{ article.body }}</p>
        <div class="btn-group" role="group">
            <button type="button" class="btn btn-danger" @click="delete_article">Delete</button>

            <router-link class="btn btn-primary"
                :to="{ name: 'update_article', params: { id: article.id } }">Update</router-link>
        </div>
    </div>
</template>
<script>
import axios from "axios";
export default {
    data() {
        return {
            article: [],
        };
    },
    props: {
        id: {
            type: [Number, String],
            required: true,
        },
    },
    methods: {
        get_detail() {
            axios
                .get(`http://127.0.0.1:5000/article/${this.id}/`)
                .then((response) => {
                    this.article = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },

        delete_article() {
            axios
                .delete(`http://127.0.0.1:5000/article/${this.id}/`)
                .then(() => {
                    this.$router.push({ name: "article" }).catch((error) => {
                        console.log(error);
                    });
                });
        },
    },
    created() {
        this.get_detail();
    },
};
</script>
<style>

</style>