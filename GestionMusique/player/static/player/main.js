var Spotify = require('spotify-web-api-js');
var s = new Spotify();

window.onload=function(){
	album = document.querySelector(".albumTitle").textContent;
	artist = document.querySelector(".artist").textContent;
	trackList = document.querySelector("#trackslist").getElementsByTagName('tbody')[0];

	console.log(album);
	console.log(artist);

	s.searchAlbums(album + " artist:" + artist)
	.then(function(data) {
    	console.log('Search artists', data.albums.items[0]);
    	document.querySelector(".pic").setAttribute('src',data.albums.items[0].images[0].url);
    	return data.albums.items[0].id;
  	})
  	.then(function(albumid) {
  		return s.getAlbumTracks(albumid);
  	})
  	.then(function(tracks) {
  		console.log(tracks);
  		for (var track of tracks.items) {
  			var newRow   = trackList.insertRow(trackList.rows.length);

  			var cell1  = newRow.insertCell(0);
  			var tracknumber  = document.createTextNode(track.track_number);
  			cell1.appendChild(tracknumber);

  			var cell2  = newRow.insertCell(1);
  			var name  = document.createTextNode(track.name);
  			cell2.appendChild(name);

  			var cell3  = newRow.insertCell(2);
  			var duration  = document.createTextNode(track.duration_ms);
  			cell3.appendChild(duration);

  			console.log(track);
  		}
  	})
  	.catch(function(error) {
    	console.error(error);
  });
}