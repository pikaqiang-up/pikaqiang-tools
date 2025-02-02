<template>
    <s-page id="root" theme="auto">
        <!--抽屉布局-->
        <s-drawer>
            <!--左侧抽屉-->
            <div slot="start" style="width: auto;">
                <sidebar />
            </div>
            <!--应用栏-->
            <Header />
            <!--主视图-->
            <s-scroll-view style="flex-grow: 1">
                <slot>
                    Hello world
                </slot>
            </s-scroll-view>
        </s-drawer>
    </s-page>
</template>

<script setup>
import Sidebar from './Sidebar.vue';
import Header from './Header.vue';

document.addEventListener('gesturestart', (event) => event.preventDefault())
</script>

<style scoped>
#root {
    position: absolute;
    height: 100%;
    width: 100%;
    transition: all 0.2s;
}
* {
    transition: all 0.2s;
}


</style>