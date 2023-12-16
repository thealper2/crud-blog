<template>
    <div class="container form">
        <h4>Create New Article</h4>

        <br />
        <form @submit.prevent="add_article">
            <input type="text" placeholder="Article title" v-model="formData.title" class="form-control" />
            <br />

            <textarea placeholder="Article body" cols="100" rows="10" v-model="formData.body"
                class="form-control"></textarea>
            <br />
            <button type="submit" class="btn btn-dark">create</button>
        </form>
    </div>
</template>
  
<script>
import axios from "axios";
export default {
    data() {
        return {
            formData: {
                title: "",
                body: "",
            },
        };
    },
    methods: {
        add_article() {
            axios
                .post("http://127.0.0.1:5000/article", this.formData)
                .then((response) => {
                    console.log(response);
                    this.$router.push({ name: "article" });
                })
                .catch((error) => {
                    console.log(error, error.response);
                });
        },
    },
};
</script>
  
<style></style>