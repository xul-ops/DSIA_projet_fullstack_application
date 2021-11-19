import axios from "axios";
import {Notification} from 'element-ui'
import defaultSetting from "@/config/defaultSetting";

const { devApiUrl, timeout } = defaultSetting
axios.defaults.baseURL = devApiUrl
axios.defaults.timeout = timeout

// request interceptor
axios.interceptors.request.use(config => {
    //set header or tocken
    return config;
});

// response interceptor
axios.interceptors.response.use(
    response => {
        console.log(response)
        const code = response.status;
        if (code !== 200) {
            Notification.error({
                title: 'Error',
                message: response.message
            });
            return Promise.reject(response.message);
        } else {
            return response.data
        }

    },
    //error
    error => {
        if (error.message ?? '' !== '') {
            Notification.error({
                title: 'Error',
                message: error.message
            });
        }
        return Promise.reject(error);
    }
);
export default axios;


