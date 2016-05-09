module.exports = function (grunt) {

require('load-grunt-tasks')(grunt);

grunt.initConfig({

browserify: {
      'GestionMusique/player/static/player/main.browser.js': ['GestionMusique/player/static/player/main.js']
    },
uglify: {
  js: {
    files: {
      'GestionMusique/player/static/player/main.min.js': ['GestionMusique/player/static/player/main.babel.js']
    },
    options: {
      sourceMap: true,
    }
  },
},
copy: {
    pickerjs: {
        expand: true,
        cwd: 'node_modules/pickadate/lib',
        src: 'picker.js',
        dest: 'node_modules/materialize-css/bin'
      },
      materialize: {
        expand: true,
        cwd: 'node_modules/bootstrap/dist/css',
        src: 'bootstrap.min.css',
        dest: 'GestionMusique/player/static/player'
      },
      bootstrapfonts: {
        expand: true,
        cwd: 'node_modules/bootstrap/dist/fonts',
        src: '*',
        dest: 'GestionMusique/player/static/fonts'
      },
      materializefonts: {
        expand: true,
        cwd: 'node_modules/materialize-css/fonts/roboto',
        src: '*',
        dest: 'GestionMusique/player/static/fonts/roboto'
      },
      materializecss: {
        expand: true,
        cwd: 'node_modules/materialize-css/bin',
        src: 'materialize.css',
        dest: 'GestionMusique/player/static/player'
      }
},
babel: {
        options: {
            sourceMap: true,
            presets: ['es2015']
        },
        dist: {
            files: {
                'GestionMusique/player/static/player/main.babel.js': 'GestionMusique/player/static/player/main.browser.js'
            }
        }
    }

});

grunt.registerTask(
    'default',
    'Build and install everything',
    ['copy', 'browserify']
    );
}