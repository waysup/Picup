Picup
-----

Picup - A Dropzone 3 action plugin which uploads images to the image-hosting site: [sm.ms](https://sm.ms/)

[![](https://visitor-count-badge.herokuapp.com/total.svg?repo_id=waysup.Picup)](https://github.com/waysup/Picup)
[![](https://visitor-count-badge.herokuapp.com/today.svg?repo_id=waysup.Picup)](https://github.com/waysup/Picup)

#### 实现功能
Dropzone 3 通过支持文件拖放来简化 Mac 上的很多操作,是提高工作效率的神器之一.在使用 `Markdown` 写作时,经常需要插入图片, 然而打开图床网站上传十分麻烦,如果可以直接拖拽完成上传,将是极好的.先上图:
<!-- more -->

![Picup-demo-gif](https://i.loli.net/2018/05/31/5b10158e37853.gif)

`Picup` 实现的功能如下:

- **拖放图片实现图片上传**:调用[sm.ms 的 API](https://sm.ms/doc/),上传图片,将上传后的图片的 URL 放置在粘贴板中,直接粘贴即可插入文档使用.
- **在本地保存已上传图片的记录**:上传的图片在本地保留一个备份,并将图片的原始路径和上传后的信息( URL 以及删除链接)保存在日志中.

#### 安装使用

##### 安装 Dropzone3

`Dropzone 3` 是 Mac 上提高效率的工具软件,最新版下载地址[戳这里](https://aptonic.com/dropzone3/latest).

##### 安装Picup

- 从本仓库下载 `.dzbundle` 文件,地址: `https://github.com/waysup/Picup`

- 下载完成后,双击 `.dzbundle` ,选择 `Add to Grid` .
- 在` username `填写图片的本地备份目录,日志也将保存在该目录下,` password `随意填写,单击` Add `即可开始使用.

![picup-config.jpg](https://i.loli.net/2018/06/07/5b194f2f39cd5.jpg)

- 日志文件中保存每一张图片的上传时间、原始路径、备份路径、大小、上传后的链接、删除该图片的链接(分别对应下图中的` upload_time `,` original_path `, ` backup_path `, ` size `, ` url `, ` delete `).

![log-info.gif](https://i.loli.net/2018/06/07/5b1951889f617.gif)
#### TODO

- 拖放同时上传多张图片

#### License

##### MIT

#### 参考资料

- [Add-on actions and API Docs for Dropzone 3](https://github.com/aptonic/dropzone3-actions)
- [sm.ms API](https://sm.ms/doc/)
<!--- 图标来自[IconFinder](https://www.iconfinder.com/icons/314457/inbox_upload_icon#size=512)-->
