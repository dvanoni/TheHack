var player = {};

(function () {
    'use strict';

    player.audioElem = null;
    player.controls = {};
    player.controls.playPause = null;
    player.playlist = [];
    player.currentTrack = 0;
    player.trackLoaded = false;

    // Track class
    function Track() {
        this.trackName = null;
        this.artistName = null;
        this.albumName = null;
        this.trackURL = null;
        this.albumArtURL = null;
    }

    player.loadSrc = function (src) {
        player.audioElem.get(0).src = src;
        player.audioElem.get(0).load();
    };

    player.loadTrack = function (track) {
        if (!track) {
            throw "Invalid track: " + track;
        }
        player.loadSrc(track.trackURL);
        player.trackLoaded = true;
    };

    player.loadTrackByID = function (id) {
        player.loadTrack(player.playlist[id]);
    };

    player.loadCurrentTrack = function () {
        player.loadTrackByID(player.currentTrack);
    };

    player.gotoID = function (id) {
        player.trackLoaded = false;
        if (!player.playlist[id]) {
            throw "Invalid track ID: " + id;
        }
        player.currentTrack = id;
        player.loadCurrentTrack();
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
    };

    player.playPause = function () {
        if (player.audioElem.get(0).paused) {
            player.play();
            player.controls.playPause.html("pause");
        } else {
            player.pause();
            player.controls.playPause.html("play");
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
        player.controls.playPause = $('#player_controls_playpause');

        player.audioElem.bind('ended', player.handlers.trackEnded);

        player.playlist[0] = new Track();
        player.playlist[0].trackURL = "http://previews.7digital.com/clips/34/9522.clip.mp3";

        var t = new Track();
        t.trackURL = "http://previews.7digital.com/clips/34/7736436.clip.mp3";
        player.addTrack(t);
    });
}());
