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

    player.playlist = [];
    player.history = [];
    player.trackLoaded = false;
    player.repeatEnabled = false;

    player.addTrackToPlaylist = function (track) {
        player.playlist.push(track);
    };

    player.addTrackToHistory = function (track) {
        var id = player.history.push(track) - 1;
        $('<li></li>')
            .html(track.trackName)
            .addClass('history_item')
            .prependTo(player.ui.history)
            .click(function () {
                player.loadHistoryTrack(id);
                player.play();
                $('#tab_1').click();
            });
    };

    player.loadAudioSrc = function (src) {
        player.ui.audio.get(0).src = src;
        player.ui.audio.get(0).load();
    };

    player.setBackgroundColor = function (url) {
        $.ajax({
            url: '/front_end/dominant_color',
            async: false,
            data: {'url': url},
            dataType: 'json',
            success: function (color) {
//                $('#home').animate({backgroundColor: color});
                $('#home').css('background-color', color);
            }
        });
    };

    player.setCurrentAlbumArtSrc = function (src) {
        player.setBackgroundColor(src);
        player.ui.currentAlbumArt.attr('src', src);
    };

    player.setNextAlbumArtSrc = function (src) {
        player.ui.nextAlbumArt.attr('src', src);
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
        player.setCurrentAlbumArtSrc(track.albumArtURL);
        player.setTrackInfo(track.trackName, track.artistName);
        player.trackLoaded = true;
    };

    player.loadCurrentTrack = function () {
        player.trackLoaded = false;
        player.loadTrack(player.playlist[0]);
        player.setNextAlbumArtSrc(player.playlist[1].albumArtURL);
    };

    player.loadNextTrack = function () {
        // remove first track from playlist and add it to history
        player.addTrackToHistory(player.playlist.shift());
        player.loadCurrentTrack();
    };

    player.loadHistoryTrack = function (id) {
        if (!player.history[id]) {
            throw "Invalid history track ID: " + id;
        }
        // remove first track from playlist and add it to history
        player.addTrackToHistory(player.playlist.shift());
        // push history track into front of playlist
        player.playlist.unshift(player.history[id]);
        player.loadCurrentTrack();
    };

    player.play = function () {
        if (!player.trackLoaded) {
            player.loadCurrentTrack();
        }
        player.ui.audio.get(0).play();
//        player.ui.controls.playPause.html("pause");
    };

    player.pause = function () {
        player.ui.audio.get(0).pause();
//        player.ui.controls.playPause.html("play");
    };

    player.playPause = function () {
        if (player.ui.audio.get(0).paused) {
            player.play();
        } else {
            player.pause();
        }
    };

    player.playNext = function () {
        player.loadNextTrack();
        player.play();
    };

    player.toggleRepeat = function () {
        player.repeatEnabled = !player.repeatEnabled;
        var span = player.ui.controls.repeat.find('span');
        if (player.repeatEnabled) {
            span.html("ON");
        } else {
            span.html("OFF");
        }
    };

    // player event handlers
    player.handlers = {};
    player.handlers.trackEnded = function (event) {
        if (player.repeatEnabled) {
            player.ui.audio.get(0).currentTime = 0;
            player.play();
        } else {
            player.playNext();
        }
    };

    $(function () {
        // player UI elements
        player.ui = {
            'audio': $('#player-audio audio'),
            'trackInfo': {
                'title': $('#player-track-info .title'),
                'artist': $('#player-track-info .artist')
            },
            'currentAlbumArt': $('#current-album img'),
            'nextAlbumArt': $('#next-album img'),
            'controls': {
                'repeat': $('#player-controls .repeat')
            },
            'history': $('#history-list')
        };

        // bind event handlers
        player.ui.audio.bind('ended', player.handlers.trackEnded);
        player.ui.currentAlbumArt.click(player.playPause);
        player.ui.nextAlbumArt.click(player.playNext);
        player.ui.controls.repeat.click(player.toggleRepeat);
    });
}());
