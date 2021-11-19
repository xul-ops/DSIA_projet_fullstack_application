<template>
  <div class="list">
    <div class="filter">
      <div class="row flex">
        <div class="label">Genre</div>
        <div class="value">
          <el-tag
              v-for="item in categoryList"
              :key="item"
              :effect="currentSelect.category === item ? 'dark' : 'plain'"
              class="tag"
              @click="filter('category', item)"
          >
            {{ item }}
          </el-tag>
        </div>
      </div>
      <div class="row flex">
        <div class="label">Year</div>
        <div class="value">
          <el-tag
              v-for="item in timeList"
              :key="item"
              :effect="currentSelect.time === item ? 'dark' : 'plain'"
              class="tag"
              @click="filter('time', item)"
          >
            {{ item }}
          </el-tag>
        </div>
      </div>
      <div class="row flex">
        <div class="label">Rank</div>
        <div class="value">
          <el-tag
              v-for="item in rateList"
              :key="item"
              :effect="currentSelect.rate === item ? 'dark' : 'plain'"
              class="tag"
              @click="filter('rate', item)"
          >
            {{ item }}
          </el-tag>
        </div>
      </div>
    </div>

    <div class="movie-list">
      <h2>Leaderboard</h2>
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
        <el-empty description="No Data"></el-empty>
      </template>
    </div>
  </div>
</template>

<script>
import {findMovieList} from "../../api/movies";

export default {
  name: "List",
  data() {
    return {
      currentSelect: {
        category: 'ALL',
        time: 'ALL',
        rate: 'rating',
      },
      categoryList: [
        "ALL",
        "Action",
        "Adventure",
        "Animation",
        "Biography",
        "Comedy",
        "Crime",
        "Drama",
        "Horror",
        "Fantasy",
        "Romance",
        "Thriller",
        // "Mystery",
        // "Sci-Fi",
      ],
      timeList: [
          "ALL",
          "2021",
          "2020",
          "2019",
          "2018",
          "2017",
          "2016",
          "2015",
          "2014",
          "2013",
          "2012"
      ],
      rateList: [
        "rating",
        "popularity",
        "metascore",
        "ranking_people",
        // "reviews_num",
        // "critic_reviews_num",
      ],
      movieList: [],
    };
  },
  created() {
    this.getData()
  },
  methods: {
    getData() {
      const {category, time, rate} = this.currentSelect
      findMovieList({
        genre: category,
        year: time,
        rank: rate
      }).then(res => {
        //console.log(res)
        if (res.code === 200) {
          // console.log(res)
          this.movieList = res.data
        } else {
          this.movieList = []
        }
      })
    },
    filter(type, value) {
      this.currentSelect[type] = value;
      this.getData()
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
.list {
  padding: 24px;

  .filter .row {
    align-items: center;
    margin-bottom: 16px;

    .label {
      width: 120px;
    }

    .value {
      .tag {
        margin-right: 8px;
        cursor: pointer;
        user-select: none;
      }
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
}
</style>
