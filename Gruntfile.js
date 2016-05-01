module.exports = function (grunt) {

require('load-grunt-tasks')(grunt);

grunt.initConfig({

browserify: {
      'GestionMusique/player/static/player/main.browser.js': ['GestionMusique/player/static/player/main.js']
    }
});

grunt.registerTask(
    'default',
    'Build and install everything',
    ['browserify']
    );
}