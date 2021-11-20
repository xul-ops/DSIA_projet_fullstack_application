<template>
  <div class="layout">
    <header class="flex flex-between">
      <div>
        <span class="title" @click="$router.push('/movie/list')"> imovie </span>
      </div>
      <div class="nav">
        <el-menu
          :default-active="activeIndex"
          class="el-menu-demo"
          mode="horizontal"
          router
          @select="handleSelect"
        >
          <el-menu-item index="/movie/list">Leaderboard</el-menu-item>
          <el-menu-item index="/movie/search">Search</el-menu-item>
        </el-menu>
      </div>
      <el-dropdown @command="handleClick">
        <div class="user flex">
          <el-avatar :size="24"> {{username}}</el-avatar>
          <span class="name">{{username}}</span>
        </div>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item >Log out</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </header>
    <main>
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
export default {
  name: "Layout",
  data() {
    return {
      activeIndex: "1",
    };
  },
  computed: {
    username() {
      return sessionStorage.getItem("username");
    },
  },
  methods: {
    handleSelect() {},
    handleClick() {
      console.log(1);
      this.$confirm("Are you sure to log out??", "Tip", {
        confirmButtonText: "Confirm",
        cancelButtonText: "Cancel",
        type: "warning",
      })
        .then(() => {
          sessionStorage.clear()
          this.$router.push("/");
        })
        .catch(() => {});
    },
  },
};
</script>

<style lang="scss" scoped>
$primary-color: rgba(35, 116, 255, 1);
::v-deep .el-menu--horizontal > .el-menu-item {
  height: 80px;
  line-height: 80px;
  border-bottom: none;
  position: relative;
  color: $primary-color !important;

  &.is-active {
    border-bottom: none;
    //color: $primary-color;
  }

  //&.is-active:after {
  //  content: "";
  //  display: inline-block;
  //  position: absolute;
  //  bottom: -1px;
  //  left: calc(50% - 15px);
  //  width: 30px;
  //  height: 2px;
  //  background: $primary-color;
  //}
}

.layout {
  width: 100%;
  height: 100%;

  header,
  main {
    width: 1040px;
    margin: 0 auto;
  }

  header {
    height: 80px;
    align-items: center;
    border-bottom: 1px solid #dcdfe6;

    .title {
      font-family: logo;
      text-align: center;
      color: $primary-color;
      font-size: 40px;
      cursor: pointer;
    }

    .nav {
      //flex: 1;
      //
      //margin-left: 32px;
    }

    .user {
      height: 80px;
      align-items: center;
      font-size: 14px;

      .name {
        display: inline-block;
        margin-left: 8px;
      }
    }
  }
}
</style>
