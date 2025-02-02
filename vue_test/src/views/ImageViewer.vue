<template>
    <s-card type="outlined" clickable="true" @click="fullable = !fullable">
        <img slot="image" :src="imgUrl" class="img-block">
    </s-card>
    <teleport to="body">
        <div class="full-viewer" v-if="fullable" @click="fullable = !fullable">
<img :src="imgUrl" class="full-img">
        </div>
    </teleport>
</template>

<style>
.img-block {
    max-width: 280px;
    min-width: 180;
    max-height: 460px;
    min-height: 120px;
    height: auto;
}

.full-viewer {
    display: flex;
    position: absolute;
    justify-content: center;
    align-items: center;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.4);
    z-index: 1000;
}
.full-img {
    position: relative;
    object-fit: contain;
    min-height: 50dvh;
    min-width: 50dvh;
    max-width: 90dvw;
    max-height: 90dvh;
}
</style>
<script setup>
import { defineProps, ref } from 'vue';
defineProps(['imgUrl']);
let fullable = ref(false);
</script>