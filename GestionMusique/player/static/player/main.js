var Spotify = require('spotify-web-api-js');
var jQuery = $ = require('jquery');
require('velocity');
var s = new Spotify();
require('materialize-css');
require('bootstrap');

window.onload=function(){

  /**
   * 
   * Playing tracks
   *
   */

  $('#trackslist').on('click', '.play', function() {
      if ($(this).parent().find('audio').get(0).paused == true) {
        $('audio').trigger('pause');
        $('.play span').addClass('glyphicon-play');
        $('.play span').removeClass('glyphicon-pause');
        $(this).parent().find('audio').trigger("play");
      } else {
        $(this).parent().find('audio').trigger("pause");
      }
      if ($(this).find('span').hasClass('glyphicon-play')) {
        $(this).find('span').toggleClass('glyphicon-pause');
      } else {
        $(this).find('span').toggleClass('glyphicon-play');
      }
    });

  $('#trackslist').on('click', '.remove', function() {
    var btn = $(this);
    $.ajax({
      url: location.origin + "/delete-song-from-playlist/" + $('.playlistID').text() + "/" + $(this).parent().find(".trackID").text(),
      method: "GET",
      data: {
        csrfmiddlewaretoken: $('#csrf').val()
      }
    })
    .done(function() {
      btn.parent().parent().slideToggle("slow");
    });
  });

  $('#addPlaylistButton').on('click',function() {
    $.ajax({
      url: location.origin + "/add-playlist/",
      method: "POST",
      data: { 
        playlistName: $('#playlistName').val(),
        csrfmiddlewaretoken: $('#csrf').val()
         }
    }).
    done(function() {
      Materialize.toast('Playlist ' + $('#playlistName').val() + ' ajoutée', 4000);
      $('#Playlist1').closeModal();
    });
  });

  $("#addSongToPlayListButton").on('click', function() {
    $.ajax({
      url: location.origin + "/add-song-to-playlist/",
      method: "POST",
      data: {
        playlist_id: $('select[name="playlistName"]').val(),
        csrfmiddlewaretoken: $('#csrf').val(),
        song_id: song_id
      }
    }).
    done(function() {
      Materialize.toast('Chanson ajoutée à la playlist ' + $('select option:selected').text(), 4000);
      $('#Playlist1').closeModal();
    });
  });

  /**
   *
   * Displaying tracks
   *
   */

  if (document.querySelector(".albumTitle") != null) {

  var album = document.querySelector(".albumTitle").textContent;
	var artist = document.querySelector(".artist").textContent;
	var trackList = document.querySelector("#trackslist").getElementsByTagName('tbody')[0];

	s.searchAlbums(album + " artist:" + artist)
	.then(function(data) {
    	var pics = document.querySelectorAll(".pic");
      for (var pic of Array.from(pics)) {
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

        var connected = document.querySelector("#connected") != null;

        $(trackList)
          .append($('<tr>')
            .append($('<td>')
              .append($('<a>')
                  .attr('class', 'waves-effect waves-light btn modal-trigger' + (connected ? "" : " hidden"))
                  .attr('href', '#Playlist1')
                  .attr('aria-label','Add to playlist')
                  .append($('<span>')
                    .attr('class','glyphicon glyphicon-plus' + (connected ? "" : " hidden"))
                ) 
              )
              .append($('<audio>')
                .attr('src', track.preview_url)
              )
              .append($('<button>')
                .attr('class','btn play')
                .append($('<span>')
                  .attr('class', 'glyphicon glyphicon-play')
                )
                .attr('aria-label', 'Play')
              )
              .append($('<span>')
                .text(track.id)
                .attr('class','trackID')
                .hide()
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
      $('.modal-trigger').on('click', function() {
        song_id = $(this).parent().find('.trackID').text();
      });
  	})
  	.catch(function(error) {

      // console.log(error);
      document.querySelector("#loading").style.display = "none";
      document.querySelector("#noTracks").style.display = "block";
  });

  } 
  if (document.querySelector('.layout_full_artist') != null) {

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

  if (document.querySelector(".playlistTitle") != null) {
    $(".hidden li").each(function() {
      s.getTrack($(this).text())
      .then(function(track) {
        var duration2 = new Date(track.duration_ms);
        var sec = (duration2.getUTCSeconds() < 10) ? "0" + duration2.getUTCSeconds() : duration2.getUTCSeconds();
        var duration  = duration2.getUTCMinutes() + ":" +  sec;

        $('#trackslist tbody')
          .append($('<tr>')
            .attr('class','track')
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
              .append($('<button>')
                .attr('class', 'btn remove')
                .append($('<span>')
                  .attr('class', 'glyphicon glyphicon-remove')
                )
                .attr('aria-label', 'Remove')
              )
              .append($('<span>')
                .text(track.id)
                .attr('class','trackID')
                .hide()
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
            .append($('<td>')
              .text(track.artists[0].name)
            )
            .append($('<td>')
              .text(track.album.name)
            )
        );
      document.querySelector(".tracks_layout").style.display = "block";
      document.querySelector("#loading").style.display = "none";

      $('.modal-trigger').leanModal();
      $('.modal-trigger').on('click', function() {
        song_id = $(this).parent().find('.trackID').text();
      });
    })
    .catch(function(error) {

      console.log(error);
      document.querySelector("#loading").style.display = "none";
      document.querySelector("#noTracks").style.display = "block";
  });
    });
  }

  if (document.querySelector("#playlistsTitle") != null) {
    $(".playlist-img").each(function() {
      var playlist = $(this);
      playlist.find(".hidden span").each(function() {
        var sid = $(this).text();
        var img = playlist.find("img[data-src='None']");
        if (img.attr("data-src") == "None") {
          img.first().attr("data-src", "ok");
          s.getTrack(sid)
          .then(function(track) {
            img.attr("src", track.album.images[0].url);
          })
          .catch(function(error) {
            console.log(error);
          });
        }
      });
    });
  }
}