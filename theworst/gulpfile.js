/**
 ========================
 NOTES
 ========================
 https://css-tricks.com/gulp-for-beginners/
 Tips
 - To run in production mode add --production to the command
 - Plugins are auto loaded and called using $.
 -- Example: To call gulp-concat plugin type $.concat
 - Tasks are defined in separate js files located in [tools/gulp/tasks]
 -- Then called by typing gulp.task('NAME-OF-Task', require('./tools/gulp/tasks/NAME-Of-Task-File')(gulp,$,app));
 --- NAME-OF-Task is what you will type after 'gulp' to execute the task
 --- NAME-Of-Task-File will exlude the .js file extension
 --- (gulp,$,app) is information you are passing into the task as you would a function
 --- This allows tasks to be re-usable (for an example look at the task Version)
 */

var gulp    = require('gulp');
var $       = require('gulp-load-plugins')();// Auto Loads plugins, call them using $
var app     = {};
app.fs      = require('fs');
app.path    = require('path');
app.sync    = require('browser-sync').create(); // create a browser sync instance.
var config  = app.config =
{
    resources: 'theworst/resources',
    static: 'theworst/static'
}

/*
============================
    FUNCTIONS
============================
*/

/**
 * @brief Get sub folders
 */
app.getFolders = function(dir)
{
    return app.fs.readdirSync(dir)
        .filter(function(file) {
            return app.fs.statSync(app.path.join(dir, file)).isDirectory();
        });
};

/**
 ====================================================================
 TASKS
 ====================================================================
 */

/**
 * DEFAULT TASK:
 * @brief This runs when typing 'gulp'
 * @description This is called during build using --production flag so be careful if you edit this.
 */
gulp.task('default', ['css']);

/*
============================
    Minify / Concat CSS
============================
*/

gulp.task('css' ,require('./tools/gulp/tasks/styles')(gulp,$,app));

gulp.task('watch', ['browser-sync'],function(){
    gulp.watch([config.resources + '/**/*.css',config.resources + '/**/*.js'], ['css']);
})

/**
 * BROWSER SYNC TASK
 * @brief Sets up and configs our Browser Syn integration
 */
gulp.task('browser-sync', function() {
    app.sync.init({
        notify: false,
        proxy: "localhost:8000"
    });
});