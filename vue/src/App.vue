<template>
  <div id="app">
    <router-view></router-view>
    <el-backtop :visibility-height="100">
      <!-- <div id="back-top">UP</div> -->
    </el-backtop>
  </div>
</template>

<script>
export default {
  name: "app",
};
</script>

<style lang="scss">
@import "./styles/element-variables.scss";
#app {
  font-family: BoschSans-Regular, Arial, "Helvetica Neue", Helvetica, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-size: 14px;
  color: #333;
}
#nprogress .bar {
  background: $--color-primary;
}
</style>
