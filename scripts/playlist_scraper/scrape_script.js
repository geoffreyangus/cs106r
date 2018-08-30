table = document.body.querySelector("ytd-playlist-video-list-renderer")
data  = table.querySelectorAll("ytd-playlist-video-renderer")

songs = []
for (var i = 0; i < data.length; i++) {
    link = data[i].querySelector("#content a").getAttribute("href")
    title = data[i].querySelector("#content #video-title").innerText
    artist = data[i].querySelector("#content #metadata yt-formatted-string").getAttribute("title")
    time = data[i].querySelector("#content ytd-thumbnail-overlay-time-status-renderer span").innerText
    songs.push({
        title,
        artist,
        time,
        link,

    })
}

for (var i = 0; i < songs.length; i++) {
    console.log("title: " + songs[i].title)
    console.log("artist: " + songs[i].artist)
    console.log("time: " + songs[i].time)
    console.log("link: " + songs[i].link)
}