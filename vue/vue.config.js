const path = require("path");
module.exports = {
    devServer: {
        port: '5050'
    },
    publicPath: './',
    productionSourceMap: false,
    chainWebpack: config => {
        // delete prefetch 
        config.plugins.delete('prefetch')
        // delete preload 
        config.plugins.delete('preload')
        config.plugin('html')
            .tap(args => {
                args[0].title = 'imovie'
                return args
            })
        config.module
            .rule('svg')
            .exclude.add(path.join(__dirname, 'src/assets/icons')) // exclude custom directory
            .end()
        config.module
            .rule('icons') // new rule
            .test(/\.svg$/)
            .include.add(path.join(__dirname, 'src/assets/icons')) // apply
            .end()
            .use('svg-sprite-loader') // sprite-loader
            .loader('svg-sprite-loader')
            .options({
                symbolId: 'icon-[name]'
            })
            .end()
    }
}

