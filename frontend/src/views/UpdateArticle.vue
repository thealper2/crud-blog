<template>
    <div class="container form">
        <h4>Update post {{ current_article.id }}</h4>
        <form @submit.prevent="update_article">
            <input type="text" placeholder="Article title" class="form-control" v-model="current_article.title" />
            <br />

            <textarea placeholder="Article body" cols="100" rows="10" class="form-control"
                v-model="current_article.body"></textarea>
            <br />
            <button type="submit" class="btn btn-dark">Update</button>
        </form>
    </div>
</template>
  
<script>
import axios from "axios";
export default {
    data() {
        return {
            current_article: [],
        };
    },
    props: {
        id: {
            type: [Number, String],
            required: true,
        },
    },
    methods: {
        selected_article() {
            axios
                .get(`http://127.0.0.1:5000/article/${this.id}/`)
                .then((response) => {
                    this.current_article = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        update_article() {
            axios
                .put(`http://127.0.0.1:5000/article/${this.id}/`, {
                    title: this.current_article.title,
                    body: this.current_article.body,
                })
                .then(() => {
                    this.$router.push({ name: "article" });
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    },

    //calling
    created() {
        this.selected_article();
    },
};
</script>
  
<style></style>