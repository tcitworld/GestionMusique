module.exports = function (grunt) {

require('load-grunt-tasks')(grunt);

grunt.initConfig({

browserify: {
      'GestionMusique/player/static/player/main.browser.js': ['GestionMusique/player/static/player/main.js']
    },
copy: {
	materialize: {
        expand: true,
        cwd: 'bower_components/Materialize/bin',
        src: 'materialize.css',
        dest: 'GestionMusique/player/static/player/'
      }
	}
});

grunt.registerTask(
    'default',
    'Build and install everything',
    ['browserify', 'copy']
    );
}