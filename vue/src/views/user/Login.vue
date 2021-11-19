<template>
  <div class="container flex flex-center">
    <div class="login-c flex flex-between">
      <div class="left flex flex-center">
        <svg-icon class="login-image" name="login"></svg-icon>
      </div>
      <div class="right flex flex-column">
        <h1>imovie</h1>
        <div v-if="display === 'login'" class="login-form">
          <el-form
            key="login"
            ref="loginForm"
            :model="loginForm"
            :rules="loginRule"
          >
            <el-form-item prop="user">
              <el-input
                v-model.trim="loginForm.user"
                placeholder="Please input your account"
                prefix-icon="el-icon-user"
                type="text"
              />
            </el-form-item>
            <el-form-item prop="password">
              <el-input
                v-model.trim="loginForm.password"
                autocomplete="off"
                placeholder="Please input your password"
                prefix-icon="el-icon-lock"
                show-password
                type="password"
              />
            </el-form-item>
            <el-form-item>
              <el-button class="login-btn" type="primary" @click="login"
                >Log in
              </el-button>
            </el-form-item>
            <el-form-item>
              No account?
              <el-button type="text" @click="changeDisplay('register')"
                >Create a account now
              </el-button>
            </el-form-item>
          </el-form>
        </div>
        <div v-if="display === 'register'" class="login-form">
          <el-form
            key="register"
            ref="registerForm"
            :model="registerForm"
            :rules="registerRule"
          >
            <el-form-item prop="email">
              <el-input
                v-model.trim="registerForm.email"
                placeholder="Please input your email"
                prefix-icon="el-icon-message"
                type="text"
              />
            </el-form-item>
            <el-form-item prop="user">
              <el-input
                v-model.trim="registerForm.user"
                placeholder="Please input your account"
                prefix-icon="el-icon-user"
                type="text"
              />
            </el-form-item>
            <el-form-item prop="password">
              <el-input
                v-model.trim="registerForm.password"
                autocomplete="off"
                placeholder="Please input your password"
                prefix-icon="el-icon-lock"
                show-password
                type="password"
              />
            </el-form-item>
            <el-form-item prop="confirmPassword">
              <el-input
                v-model.trim="registerForm.confirmPassword"
                autocomplete="off"
                placeholder="Please input your password again"
                prefix-icon="el-icon-lock"
                show-password
                type="password"
              />
            </el-form-item>
            <el-form-item>
              <el-button class="login-btn" type="primary" @click="register"
                >Create account
              </el-button>
            </el-form-item>
            <el-form-item>
              <el-button type="text" @click="changeDisplay('login')"
                >Sign in
              </el-button>
            </el-form-item>
          </el-form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { login, register } from "../../api/user";

export default {
  components: {},
  data() {
    const confirmValidator = (rule, value, callback) => {
      // console.log(value);
      if (!value) {
        callback(new Error("Password is requied."));
      } else if (value !== this.registerForm.password) {
        callback(new Error("The two passwords are inconsistent."));
      } else {
        callback();
      }
    };
    const emailvalidator = (rule, value, callback) => {
      const isEmail = (s) => {
        return /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((.[a-zA-Z0-9_-]{2,3}){1,2})$/.test(
          s
        );
      };
      if (!isEmail(value)) {
        callback(new Error("Email format is incorrect"));
      } else {
        callback();
      }
    };
    return {
      display: "login",
      loginForm: {
        user: "",
        password: "",
      },
      loginRule: {
        user: [
          {
            trigger: "blur",
            required: true,
            message: "Account is requied.",
          },
        ],
        password: [
          {
            trigger: "blur",
            required: true,
            message: "Password is requied.",
          },
        ],
      },
      registerForm: {
        user: "",
        password: "",
        confirmPassword: "",
        email: "",
      },
      registerRule: {
        user: [
          {
            trigger: "blur",
            required: true,
            message: "Account is requied.",
          },
        ],
        password: [
          {
            trigger: "blur",
            required: true,
            message: "Password is requied.",
          },
        ],
        confirmPassword: [
          {
            trigger: "blur",
            validator: confirmValidator,
          },
        ],
        email: [
          { required: true, message: "Email is required.", trigger: "blur" },
          { validator: emailvalidator, trigger: "blur" },
        ],
      },
    };
  },
  methods: {
    changeDisplay(type) {
      this.display = type;
      this.$nextTick(() => {
        if (type === "login") {
          this.loginForm = {
            user: "",
            password: "",
          };
          this.$refs.loginForm.clearValidate();
        } else {
          this.registerForm = {
            user: "",
            password: "",
            email: "",
          };
          this.$refs.registerForm.clearValidate();
        }
      });
    },
    login() {
      this.$refs.loginForm.validate((value) => {
        if (value) {
          const { user, password } = this.loginForm;
          login({
            username: user,
            password: password,
          }).then((res) => {
            if (res.code === 200) {
              this.$router.push("/movie/list");
            } else if (res.code === 204) {
              this.$notify.error({
                title: "Error",
                message: "User not exisit!",
              });
            } else {
              this.$notify.error({
                title: "Error",
                message: "Wrong user name or password!",
              });
            }
          });
        }
      });
    },
    register() {
      // console.log(this.registerForm);
      this.$refs.registerForm.validate((value) => {
        if (value) {
          const { user, password, email } = this.registerForm;
          register({
            username: user,
            password1: password,
            email: email,
          }).then((res) => {
            if (res.code === 200) {
              this.$notify.success({
                title: "Success",
                message: "Register successful!",
              });
              this.$router.go(0);
            } else if (res.code === 203) {
              this.$notify.error({
                title: "Error",
                message: "User is existed !",
              });
            } else {
              this.$notify.error({
                title: "Error",
                message: res.message,
              });
            }
          });
        }
      });
    },
  },
};
</script>
<style lang="scss" scoped>
.logo {
  font-size: 100px;
}

.container {
  width: 100vw;
  height: 100vh;
  background: url("../../assets/login-bg.png") center;
  background-size: cover;
}

.login-c {
  width: 60%;
  height: 70%;
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
  border-radius: 12px;
  background: #ffffff;
  overflow: hidden;
}

.left,
.right {
  width: 50%;
  height: 100%;
}

.login-image {
  font-size: 300px;
}

.left {
  background: linear-gradient(
    180deg,
    rgba(100, 169, 255, 1) 0%,
    rgba(100, 169, 255, 1) 0%,
    rgba(35, 116, 255, 1) 100%,
    rgba(35, 116, 255, 1) 100%
  );
}

.right {
  align-items: center;
  justify-content: center;

  h1 {
    font-family: logo;
    text-align: center;
    color: rgba(35, 116, 255, 1);
    font-size: 48px;
  }

  .login-form {
    width: 60%;
  }

  .login-btn {
    width: 100%;
  }
}
</style>
