<template>
  <div class="detail">
    <div class="base-info flex">
      <div class="cover">
        <img :src="movieDetail.image" alt="" class="cover-img">
      </div>
      <div class="info">
        <h1>{{ movieDetail.title }}</h1>
        <el-form label-position="left" label-suffix=":" label-width="70px">
          <el-form-item label="Year">{{ movieDetail.year }}</el-form-item>
          <el-form-item label="Duration">{{ movieDetail.duration }}</el-form-item>
          <el-form-item label="Genre">
            {{ [movieDetail.genres_1].join('、') }}
          </el-form-item>
          <el-form-item label="Star">
            {{ [movieDetail.stars_1].join('、') }}
          </el-form-item>
        </el-form>
      </div>
    </div>
    <div class="rate-info">
      <h2>Ranking Infomation</h2>
      <el-form label-position="left" label-suffix=":">
        <el-row>
          <el-col :span="12">
            <el-form-item label="Rating">
              <el-rate
                  v-model="movieDetail.rating"
                  :max="10"
                  disabled
                  score-template="{value}"
                  show-score
                  text-color="#ff9900">
              </el-rate>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="Ranking People">{{ movieDetail.ranking_people }}</el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="ReviewsNum">{{ movieDetail.reviews_num }}</el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="CriticReviewsName">{{ movieDetail.critic_reviews_num }}</el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="Meta Score">
              <el-rate
                  v-model="movieDetail.metascore"
                  :max="10"
                  disabled
                  score-template="{value}"
                  show-score
                  text-color="#ff9900">
              </el-rate>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="Popularity">
              <el-rate
                  v-model="movieDetail.popularity"
                  :max="10"
                  disabled
                  score-template="{value}"
                  show-score
                  text-color="#ff9900">
              </el-rate>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
    </div>
    <div class="other-info">
      <h2>Other Infomation</h2>
      <el-form label-position="left" label-suffix=":" label-width="120px">
        <el-form-item label="Director">{{ [movieDetail.director_1].join('、') }}</el-form-item>
        <el-form-item label="Writer">
          {{ [movieDetail.writers_1].join('、') }}
        </el-form-item>
        <el-form-item label="Presentation">{{ movieDetail.presentation }}</el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>
import {findMovieById} from "../../api/movies";

export default {
  name: "Detail",
  data() {
    return {
      id: "",
      movieDetail: {},
    }
  },
  created() {
    this.id = this.$route.query.id
    this.getData()
  },
  methods: {
    getData() {
      findMovieById(
          this.id
      ).then(res => {
        if (res.code === 200) {
          Object.assign(this.movieDetail, res.data)
        }
      })
    }
  }
}
</script>

<style lang="scss" scoped>
::v-deep .el-form-item {
  margin-bottom: 0;
}

::v-deep .el-rate {
  height: 40px;
  line-height: 40px;

  .el-rate__icon {
    vertical-align: middle;
  }
}

.detail {
  padding: 32px;
}

.cover {
  margin-right: 32px;
}

.cover-img {
  width: 135px;
  height: 200px;
}

.info {
  flex: 1;
  font-size: 12px;
}
</style>
