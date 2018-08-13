table = document.body.querySelector("#pl-video-table")
data  = table.querySelectorAll("tr")

songs = []
for (var i = 0; i < data.length; i++) {
    title = data[i].getAttribute("data-title")
    link = data[i].querySelector(".pl-video-title-link").getAttribute("href")
    time = data[i].querySelector(".pl-video-time").innerText
    songs.push({
        title,
        link,
        time
    })
}

