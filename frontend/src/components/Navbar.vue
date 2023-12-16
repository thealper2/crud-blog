<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light justify-content-between" @click="setNavButtonState">
        <a class="navbar-brand">CRUD Blog App</a>

        <div class="collapse navbar-collapse">
            <ul class="navbar-nav mr-auto" id="navbarSupportedContent">
                <li class="nav-item active">
                    <router-link class="nav-link" to="/">Home</router-link>
                </li>
                <li class="nav-item">
                    <router-link class="nav-link" to="/create_article">Create Article</router-link>
                </li>
            </ul>
        </div>
    </nav>
</template>

<script>
export default {

};
</script>

<style></style>