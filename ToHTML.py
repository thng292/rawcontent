import csv

shtml = """<!DOCTYPE html><html><head><title>Answer</title><link rel="stylesheet" href="style.css"><meta name="viewport" content="width=device-width, initial-scale=1.0"></head><body><div id="first-column"><div class="sticky-item tableoC"><p>Nội Dung:</p><p class="table-content"><a href="#start-personal">Cá nhân</a></p><p class="table-content"><a href="#start-teacher">Giáo Viên</a><li><a href="#start-grade10">Lớp 10</a></li><li><a href="#start-grade11">Lớp 11</a></li><li><a href="#start-grade12">Lớp 12</a></li></p><p class="table-content"><a href="#start-classmate">Thành viên của CL19-22</a></p></div></div><div id="second-column"><a id="start-personal"></a>"""
ehtml = """<div id="foot">Tạo bởi Nguyễn Quang Thông<br>nguyenquangthong292@gmail.com</div></div><div id="third-column"><div class="sticky-item"><p>More resource:</p><iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/1455869662%3Fsecret_token%3Ds-vgwYohC07TF&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis"><a href="https://soundcloud.com/tung-nguyen-100488950" title="Tung Nguyen" target="_blank" style="color: #cccccc; text-decoration: none;">Tung Nguyen</a> · <a href="https://soundcloud.com/tung-nguyen-100488950/sets/tong-hop-nhac-tre-soi-dong-tiep-suc-mua-thi/s-vgwYohC07TF" title="Tuyển Tập Nhạc Trẻ Sôi Động Tiếp Sức Mùa Thi" target="_blank" style="color: #cccccc; text-decoration: none;">Tuyển Tập Nhạc Trẻ Sôi Động Tiếp Sức Mùa Thi</a></div><a href="https://www.youtube.com/channel/UC7BUeJYF4pI3CdyU47Yf7aA">Youtube 1</a><br><a href="https://www.youtube.com/channel/UCmsmEx_HQ94TXEAyiHj2_xQ">Youtube 2</a><br><a href="https://www.youtube.com/playlist?list=PLgrjBS8cDauxwsVd7KQw_MjuN3EDo27pe">Playlist học online</a><br><a href="https://photos.app.goo.gl/uHwxEUUXAXgtcLwe9">Ảnh lớp</a><br><a href="https://hcm01-my.sharepoint.com/personal/7939555741_hochiminh_itrithuc_vn/_layouts/15/onedrive.aspx?id=%2Fpersonal%2F7939555741%5Fhochiminh%5Fitrithuc%5Fvn%2FDocuments%2F%C4%90%C3%A0%20L%E1%BA%A1t&ga=1">Ảnh Đà Lạt</a><br><a href="">Thêm Ảnh lớp</a><br><a href="https://www.bestie.vn/2022/07/hoc-sinh-chuyen-ly-nhan-xet-de-van-nam-nay-vua-suc">Phóng sự H.Minh, Như</a><br><a href="https://youtu.be/m34NIL2fV5I">Phóng sự VTV<a><br><a href="https://www.facebook.com/watch/?v=553703366317557">Phóng sự Bảo, Duy</a></div></div></body></html>"""

outFile = open("index.html",mode='w',encoding="utf-8")
inFile  = csv.reader(open("Answer.csv",mode='r',encoding="utf-8"))

outFile.write(shtml)

head = next(inFile)
person = []
for row in inFile :
    person.append(row)

for a in person: 
    outFile.write(f'<div class="content"><time>{a[0]}</time><h1>{a[2]}</h1><small>{a[1]}</small>')
    if a[3] :
        outFile.write(f'<h3>{head[3]}</h3><p>{a[3]} </p>')
    if a[4] :
        outFile.write(f'<h3>{head[4]}</h3><p>{a[4]} </p>')
    if a[76] :
        outFile.write(f'<h3>{head[76]}</h3><p>{a[76]} </p>')
    outFile.write(f'</div>')

for i in range(5,79) :
    if i in {75,76} :
        continue
    outFile.write(f'<div class="content"><h2>Về {head[i]}</h2>')
    for a in person :
        if a[i] :
            outFile.write(f'<p>{a[i]}<br> - <strong>{a[2]}</strong> </p>')
    outFile.write(f'</div>')

outFile.write(ehtml)
outFile.close()