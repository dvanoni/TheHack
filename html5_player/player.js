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

    player.audioElem = null;
    player.albumArtImg = null;
    player.controls = {};
    player.controls.playPause = null;
    player.playlist = [];
    player.currentTrack = 0;
    player.trackLoaded = false;

    player.loadAlbumArtSrc = function (src) {
        player.albumArtImg.attr('src', src);
    };

    player.loadAudioSrc = function (src) {
        player.audioElem.get(0).src = src;
        player.audioElem.get(0).load();
    };

    player.loadTrack = function (track) {
        if (!track) {
            throw "Invalid track: " + track;
        }
        player.loadAudioSrc(track.trackURL);
        player.loadAlbumArtSrc(track.albumArtURL);
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
        player.audioElem.get(0).play();
        player.controls.playPause.html("pause");
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
        player.audioElem.get(0).pause();
        player.controls.playPause.html("play");
    };

    player.playPause = function () {
        if (player.audioElem.get(0).paused) {
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
        player.audioElem = $('#player_audio audio');
        player.albumArtImg = $('#player_album_art img');
        player.controls.playPause = $('#player_controls_playpause');

        player.audioElem.bind('ended', player.handlers.trackEnded);
    });
}());
