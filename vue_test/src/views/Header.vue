<template>
    <s-appbar>
        <!--应用栏-左侧导航按钮-->
        <s-icon-button slot="navigation" onclick="document.querySelector('s-drawer').toggle()">
            <s-icon name="menu"></s-icon>
        </s-icon-button>
        <!--应用栏-标题-->
        <div slot="headline"> Title </div>
        <!--应用栏-搜索框-->
        <!-- <s-search slot="search" placeholder="搜索关键字">
            <s-icon name="search" slot="start"></s-icon>
            <s-icon name="close" slot="end"></s-icon>
            <div slot="dropdown" style="height: 128px;">
                ...
            </div>
        </s-search> -->
        <!--应用栏-操作按钮-->
        <s-tooltip slot="action">
            <s-icon-button slot="trigger" @click='toggleTheme'>
                <s-icon name="dark_mode"></s-icon>
            </s-icon-button>
            主题切换
        </s-tooltip>
    </s-appbar>
</template>
<script setup>
function toggleTheme() {
    document.querySelector('#root').theme = document.querySelector('#root').isDark ? 'light' : 'dark'
}
</script>