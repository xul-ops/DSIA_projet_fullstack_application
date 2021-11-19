<template>
  <div class="search">
    <div class="search-area">
      <el-input
          v-model="searchContent"
          :placeholder="'Please input ' + select.toLocaleLowerCase()"
          class="input-with-select"
      >
        <el-select slot="prepend" v-model="select">
          <el-option
              v-for="item in selectList"
              :key="item"
              :label="item"
              :value="item"
          ></el-option>
        </el-select>
        <el-button
            slot="append"
            icon="el-icon-search"
            @click="handleSearch"
        ></el-button>
      </el-input>
    </div>
    <div class="movie-list">
      <h2>Search Result</h2>
      <template v-if="movieList.length">
        <div v-for="item in movieList" :key="item.id" class="movie-item">
          <div class="flex">
            <div class="cover">
              <img :src="item.cover" alt=""/>
            </div>
            <div class="info">
              <div>
                <el-button type="text" @click="goDetail(item.id)">{{
                    item.title
                  }}
                </el-button>
              </div>
              <div class="desc">
                {{ item.year }}/{{ item.genre.join("/") }}/{{
                  item.director.join("/")
                }}/{{ item.writer.join("/") }}/{{ item.star.join("/") }}
              </div>
              <div class="rate flex">
                <el-rate
                    v-model="item.rating"
                    :max="10"
                    disabled
                    score-template="{value}"
                    show-score
                    text-color="#ff9900"
                >
                </el-rate>
              </div>
              <div>{{ item.rankingPeople }} ont commenté</div>
            </div>
          </div>

          <el-divider></el-divider>
        </div>
      </template>
      <template v-else>
        <el-empty description="Not Found"></el-empty>
      </template>
    </div>
  </div>
</template>

<script>
import {searchMovieList} from "../../api/movies";

export default {
  name: "Search",
  data() {
    return {
      searchContent: "",
      select: "Title",
      selectList: ["Title", "Star", "Writer", "Director"],
      movieList: [],
    };
  },
  methods: {
    handleSearch() {
      searchMovieList({
        type: this.select,
        content: this.searchContent
      }).then(res => {
        if (res.code === 200) {
          this.movieList = res.data
        } else {
          this.movieList = []
        }

      })
    },
    goDetail(id) {
      this.$router.push({
        path: "/movie/detail",
        query: {
          id: id,
        },
      });
    },
  },
};
</script>

<style lang="scss" scoped>
::v-deep .el-input-group__prepend {
  width: 100px;
}

.search-area {
  width: 100%;
  text-align: center;
  padding: 64px 32px;

  .input-with-select {
    width: 600px;
    text-align: center;
  }
}

.movie-list {
  margin-top: 32px;
}

.movie-item {
  //height: 128px;

  .cover img {
    width: 75px;
    height: 110px;
    margin-right: 32px;
  }

  .info {
    line-height: 34px;

    .desc {
      //max-width:500px;
    }
  }
}
</style>
