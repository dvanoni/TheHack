var player = {};

// Track class
function Track(trackInfo) {
    'use strict';
    this.trackName = null;
    this.artistName = null;
    this.trackURL = null;
    this.albumArtURL = null;

    this.parseInput = function (input) {
        if (input.name) {
            this.trackName = input.name;
        }
        if (input.artist) {
            this.artistName = input.artist;
        }
        if (input.preview_url) {
            this.trackURL = input.preview_url;
        }
        if (input.album_img) {
            this.albumArtURL = input.album_img;
        }
    };

    if (trackInfo) {
        this.parseInput(trackInfo);
    }
}

(function () {
    'use strict';

    // player UI elements
    player.ui = {
        'audio': null,
        'trackInfo': {'title': null, 'artist': null},
        'albumArt': null,
        'controls': {'playPause': null}
    };

    player.playlist = [];
    player.currentTrack = 0;
    player.trackLoaded = false;

    player.loadAudioSrc = function (src) {
        player.ui.audio.get(0).src = src;
        player.ui.audio.get(0).load();
    };

    player.loadAlbumArtSrc = function (src) {
        player.ui.albumArt.attr('src', src);
    };

    player.setTrackInfo = function (title, artist) {
        player.ui.trackInfo.title.html(title);
        player.ui.trackInfo.artist.html(artist);
    };

    player.loadTrack = function (track) {
        if (!track) {
            throw "Invalid track: " + track;
        }
        player.loadAudioSrc(track.trackURL);
        player.loadAlbumArtSrc(track.albumArtURL);
        player.setTrackInfo(track.trackName, track.artistName);
        player.trackLoaded = true;
    };

    player.loadTrackByID = function (id) {
        if (!player.playlist[id]) {
            throw "Invalid track ID: " + id;
        }
        player.currentTrack = id;
        player.loadTrack(player.playlist[id]);
        console.log("Loaded track " + id);
    };

    player.loadCurrentTrack = function () {
        player.loadTrackByID(player.currentTrack);
    };

    player.gotoID = function (id) {
        player.trackLoaded = false;
        player.loadTrackByID(id);
    };

    player.gotoNext = function () {
        player.gotoID(player.currentTrack + 1);
    };

    player.gotoPrev = function () {
        player.gotoID(player.currentTrack - 1);
    };

    player.play = function () {
        if (!player.trackLoaded) {
            player.loadCurrentTrack();
        }
        player.ui.audio.get(0).play();
        player.ui.controls.playPause.html("pause");
    };

    player.playNext = function () {
        player.gotoNext();
        player.play();
    };

    player.playPrev = function () {
        player.gotoPrev();
        player.play();
    };

    player.pause = function () {
        player.ui.audio.get(0).pause();
        player.ui.controls.playPause.html("play");
    };

    player.playPause = function () {
        if (player.ui.audio.get(0).paused) {
            player.play();
        } else {
            player.pause();
        }
    };

    player.addTrack = function (track) {
        player.playlist.push(track);
    };

    player.handlers = {};
    player.handlers.trackEnded = function (event) {
        player.playNext();
    };

    $(function () {
        player.ui.audio = $('#player_audio audio');
        player.ui.albumArt = $('#player_album_art img');
        player.ui.trackInfo.title = $('#player_track_info_title');
        player.ui.trackInfo.artist = $('#player_track_info_artist');
        player.ui.controls.playPause = $('#player_controls_playpause');

        player.ui.audio.bind('ended', player.handlers.trackEnded);
    });
}());
