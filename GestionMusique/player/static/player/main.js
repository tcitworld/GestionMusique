var Spotify = require('spotify-web-api-js');
var jQuery = $ = require('jquery');
require('velocity');
var s = new Spotify();
require('materialize-css');
require('bootstrap');

window.onload=function(){

  $('#trackslist').on('click', '.play', function() {
      if ($(this).parent().find('audio').get(0).paused == true) {
        $('audio').trigger('pause');
        $(this).parent().find('audio').trigger("play");
      } else {
        $(this).parent().find('audio').trigger("pause");
      }
    });

  if (document.querySelector(".albumTitle") != null) {

  var album = document.querySelector(".albumTitle").textContent;
	var artist = document.querySelector(".artist").textContent;
	var trackList = document.querySelector("#trackslist").getElementsByTagName('tbody')[0];

	s.searchAlbums(album + " artist:" + artist)
	.then(function(data) {
    	let pics = document.querySelectorAll(".pic");
      for (let pic of Array.from(pics)) {
        pic.setAttribute('src',data.albums.items[0].images[0].url);
      }
    	return data.albums.items[0].id;
  	})
  	.then(function(albumid) {
  		return s.getAlbumTracks(albumid);
  	})
  	.then(function(tracks) {
  		for (var track of tracks.items) {

        var duration2 = new Date(track.duration_ms);
        var sec = (duration2.getUTCSeconds() < 10) ? "0" + duration2.getUTCSeconds() : duration2.getUTCSeconds();
        var duration  = duration2.getUTCMinutes() + ":" +  sec;

        $(trackList)
          .append($('<tr>')
            .append($('<td>')
              .append($('<a>')
                  .attr('class', 'waves-effect waves-light btn modal-trigger')
                  .attr('href', '#Playlist1')
                  .attr('aria-label','Add to playlist')
                  .append($('<span>')
                    .attr('class','glyphicon glyphicon-plus')
                ) 
              )
            )
            .append($('<td>')
              .append($('<audio>')
                .attr('src', track.preview_url)
              )
              .append($('<button>')
                .attr('class','btn play')
                .append($('<span>')
                  .attr('class', 'glyphicon glyphicon-play-circle')
                )
                .attr('aria-label', 'Play')
              )
            )
            .append($('<td>')
              .text(track.track_number)
            )
            .append($('<td>')
              .text(track.name)
            )
            .append($('<td>')
              .text(duration)
            )
        );
  		}
      document.querySelector(".tracks_layout").style.display = "block";
      document.querySelector("#loading").style.display = "none";

      $('.modal-trigger').leanModal();
  	})
  	.catch(function(error) {

      console.log(error);
      document.querySelector("#loading").style.display = "none";
      document.querySelector("#noTracks").style.display = "block";
  });

    // $('.addPlaylistButton').click(function() {
    //   $.ajax(
    //     )
    // });
  } else {

    artist = document.querySelector(".artist").textContent;

    s.searchArtists(artist)
    .then(function(data) {
      var pics = document.querySelectorAll(".artist_background .pic");
      for (var pic of Array.from(pics)) {
        pic.setAttribute('src',data.artists.items[0].images[0].url);
      }
    }, function(err) {
    });

    $(".album_card").each(function() {

      var album = $(this);

      s.searchAlbums($(this).find(".album_card_title").text() + " artist:" + artist)
      .then(function(data) {
        album.find(".pic").attr('src', data.albums.items[0].images[0].url);
      })
      .catch(function(error) {
      });
    });      
  }
}