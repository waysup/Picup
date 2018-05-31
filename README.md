Picup
-----

Picup - A Dropzone 3 action plugin which uploads images to the image-hosting site: [sm.ms](https://sm.ms/)

#### 实现功能
Dropzone 3 通过支持文件拖放来简化 Mac 上的很多操作,是提高工作效率的神器之一.在使用 `Markdown` 写作时,经常需要插入图片, 然而打开图床网站上传十分麻烦,如果可以直接拖拽完成上传,将是极好的.先上图:

![Picup-demo-gif](https://i.loli.net/2018/05/31/5b10158e37853.gif)

`Picup` 实现的功能如下:

- **拖放图片实现图片上传**:调用[sm.ms 的 API](https://sm.ms/doc/),上传图片,将上传后的图片的 URL 放置在粘贴板中,直接粘贴即可插入文档使用.

#### 安装使用

##### 安装 Dropzone3

`Dropzone 3` 是 Mac 上提高效率的工具软件,最新版下载地址[戳这里](https://aptonic.com/dropzone3/latest).

##### 安装Picup

- 从本仓库下载 `.dzbundle` 文件,地址: `https://github.com/waysup/Picup`

- 下载完成后,双击 `.dzbundle` ,选择 `Add to Grid` ,即可开始使用.

#### TODO

- 在本地保存已上传图片的记录
- 支持删除已上传的图片
- 拖放同时上传多张图片

#### 参考资料

- [Add-on actions and API Docs for Dropzone 3](https://github.com/aptonic/dropzone3-actions)
- [sm.ms API](https://sm.ms/doc/)
- 图标来自[IconFinder](https://www.iconfinder.com/icons/314457/inbox_upload_icon#size=512)