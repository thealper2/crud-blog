<template>
    <div class="card" style="width: 25rem;"  v-for="article in articles" :key="article.id">
        <div class="card-body">
            <h5 class="card-title">{{ article.title }}</h5>
            <router-link :to="{ name: 'article_details', params: { id: article.id } }">Read More</router-link>
        </div>
    </div>
</template>
<script>
import axios from "axios";

export default {
    data() {
        return {
            articles: [],
        };
    },

    created() {
        axios
            .get("http://127.0.0.1:5000/articles")
            .then((response) => {
                this.articles = response.data;
            })
            .catch((error) => {
                console.log(error);
            });
    },
};
</script>
<style>

</style>