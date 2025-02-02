<template>
    <div id="img-viewer">
        <ImageViewer v-for="(img, index) in imgUrlList" :key="index" :imgUrl="img" />
    </div>
</template>
<script setup>
import ImageViewer from "./ImageViewer.vue";
let imgUrlList = [
    "/picture/100356937_p0.jpg",
    "/picture/101351514_p0.png",
    "/picture/102188682_p0.png",
    "/picture/102680748_p0.png",
    "/picture/102773124_p0.png",
    "/picture/102964813_p0.jpg",
    "/picture/103144864_p0.jpg",
    "/picture/103156252_p0.png",
    "/picture/103878428_p0.png",
    "/picture/104861557_p0.png",
    "/picture/104891298_p0.jpg",
    "/picture/105353432_p0.png",
    "/picture/105537995_p0.jpg",
    "/picture/105821294_p0.png",
    "/picture/106125813_p0.jpg",
    "/picture/107111708_p0.jpg",
    "/picture/107121366_p0.png",
    "/picture/107168253_p0.png",
    "/picture/108230856_p0.jpg",
];
</script>

<style scoped>
#img-viewer {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    padding: 2rem;
    justify-content: space-evenly;
    align-items: center;
    height: 100%;
}
</style>
