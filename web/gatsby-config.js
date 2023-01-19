/**
 * @type {import('gatsby').GatsbyConfig}
 */
module.exports = {
    siteMetadata: {
        title: `metaphors`,
        siteUrl: `https://www.yourdomain.tld`,
    },
    plugins: [
        "gatsby-transformer-remark",
        {
            resolve: "gatsby-source-filesystem",
            options: {
                name: "pages",
                path: "./src/pages/",
            },
            __key: "pages",
        },
        {
            resolve: "@chakra-ui/gatsby-plugin",
            options: {
                /**
                 * @property {boolean} [resetCSS=true]
                 * if false, this plugin will not use `<CSSReset />
                 */
                resetCSS: true,
                /**
                 * @property {boolean} [isUsingColorMode=true]
                 * if false, this plugin will not use <ColorModeProvider />
                 */
                isUsingColorMode: true,
                /**
                 * @property {boolean} [isBaseProvider=false]
                 * if true, will render `<ChakraBaseProvider>`
                 */
                isBaseProvider: false,
            },
        },
        {
            resolve: "gatsby-plugin-eslint",
            options: {
                test: /\.js$|\.jsx$|\.ts$|\.tsx$/,
                exclude: /(node_modules|.cache|public)/,
                stages: ["develop"],
                options: {
                    emitWarning: true,
                    failOnError: false,
                },
            },
        },
    ],
};
