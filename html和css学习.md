# 一日通关常用的HTML

### 几个语义标签

```html
<b>加粗</b>，<strong>加粗</strong>，<ins>下划线</ins>,<u>下划线</u>
            <i>倾斜</i>，<em>倾斜</em>，<del>删除</del>，<s>删除</s>
<hr>分割线
<br>换行
&nbsp空格
```

<b>展示效果</b>：

​	<b>加粗</b>，<strong>加粗</strong>，<ins>下划线</ins>,<u>下划线</u>
​            <i>倾斜</i>，<em>倾斜</em>，<del>删除</del>，<s>删除</s>

<hr>&nbsp&nbsp

###  几个链接的引用

```html
			<img src="../logo.PNG" title="ustc" height="60" >
<!-- 只设一个height可以自适应调整-->
            <audio src="永恒的东风.mp3" controls></audio>
            <video src="千里邀月.mp4" controls autoplay muted></video>
<!-- 如果想自动播放需要添加autoplay muted，但是会静音打开,设置loop可以循环播放 -->
			<a href="https://www.ustc.edu.cn/" target="_blank">ustc官网</a>
            <!-- target属性默认是_self,表示是在本网页打开，_blank可以实现在新地址打开 -->
```

几个使用地址的，注意属性的设置

### 有序无序以及自定义列表

\<ul>无序标签，\<ol>有序标签，\<ul>到\</ul>中间只能使用\<li>标签，但\<li>标签中可使用其他标签。

自定义列表:

**优先级(父子关系)**：\<dl>(自定义列表list)$>$\<dt>(自定义标题title)$>$\<dd>

\<dl>标签里只能放\<dt>和\<dd>标签，但dt和dd里可以放别的标签

### 表格(table)

```html
 <table border="5">
            <caption><strong>我滴小可爱</strong></caption>
        <thead>
            <tr>
                <th>排名</th>
                <th>姓名</th>
                <th>CV</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>胡桃</td>
                <td>高桥李依</td>
            </tr>
            <tr>
                <td>2</td>
                <td>绫华</td>
                <td>早见沙织</td>
            </tr>
        </tbody> 
        <tfoot>
              <tr>
            <td>总结</td>
            <td colspan="2" align="center">love love love</td>
        </tr>
        </tfoot>
        </table>
```

1. table>tr(表格行)>td(单元格)
2. caption表格标题th表头td普通格子
3. \<thead>,tbody,tfoot对浏览器阅读没有影响，只是为了给代码划分结构增强代码的可读性
4. 要想调分割线(否则没有格子)，在属性里加入border自主调参数
5. 合并单元格，注意不能跨结构！(colspan和rowspan参数)，遵循优先左上原则，右下的不用打

### 表单

```html
<form action="">
    <span>你最喜欢的角色是:</span> <input type="text" placeholder="输入人名">   
    <br>
    密码:<input type="password" placeholder="输入密码"> 
    <br>
    <!-- label的两种用法 -->
    (单选!)<input type="radio" name="wife" id="a"><label for="a">胡桃</label>
    <!-- 第一种用法input的id要和lable for属性一致-->
    <input type="radio" name="wife" id="b"><label for="b">绫华</label>
    <label ><input type="radio" name="wife">心海</label>
    <br>
    (多选)<input type="checkbox" name="" id="" checked>同意协议,不吃牢饭
    <br>
    上传文件<input type="file" multiple>
    <br>
    <input type="submit" value="注册或登陆">
    <input type="reset">
    <input type="button" value="hhh">
    </form>
    <button>我是</button>
    <!--下拉菜单-->
    <select>
        <option >甘雨</option>
        <option >胡桃</option>
        <option>申鹤</option>
        <option selected>小影</option>
    </select>
    <br>
    <!--文本域-->
    <textarea name="" id="" cols="40" rows="10"></textarea>
```

* **input标签**

|   type   |   语义   |                      注释                      |
| :------: | :------: | :--------------------------------------------: |
|   text   | 文本信息 |   placeholder可以设置提示词，password也可以    |
| password |   密码   |             输入会以加密的形式呈现             |
|  radio   |   单选   | 需要设定同一个'name'才能实现单选，checked默认✔ |
| checkbox |   多选   |                  checked默认✔                  |
|   file   | 文件提交 |         添加multiple参数可提交多个文件         |
|  submit  |   提交   |              可以实现提交后端数据              |
|  reset   |   重置   |            需要用\<form>标签框起来             |
|  button  | 普通按钮 |             可通过css实现多样功能              |

* **select**

  ```html
  <select>
          <option >甘雨</option>
          <option >胡桃</option>
          <option>申鹤</option>
          <option selected>小影</option>
  </select>
  ```

  select$>$option,selected表示默认选择

* **文本域textarea**

# CSS部分

**基本格式**  : 选择器+   $\{...\}$

常见css属性:**color, font-size , background-color,width,height**（注意像素单位）

### 调用css的三种方式

1. 内嵌式：在head标签title下建立\<style>标签，在其中填入css部分(小程序)
2. 外联式：引用link标签`<link rel="stylesheet" href="hh.css">(项目开发)`
3. 行内式：边写边设定`<div style="color:blueviolet   "> good!</div>`(配合js)

### 选择器

1. 标签选择器：以标签名命名的选择器，会选中所有标签生效,之前用过

2. 类选择器

* 定义结构：.类名 {}   

* 使用加入class属性即可，可嵌套叠加使用


3. id选择器(配合js)

* 定义结构：#id名 {}   

* 使用加入id属性即可，不可嵌套叠加使用，即一个标签只能有一个id
* id一个页面只能修饰一个标签！！不会报错但是不符合规范

4. 通配符选择器

* 定义结构：*{}   

* 使用即全局标签统一配置

* 用的极少
```html
    <style>
        .redd {
            color: red;
        }
        .size {
            font-size: 66px;
        }
        #blue {
            color: skyblue;
        }
        *{
            margin: 0%;
            padding: 0%;
        }
    </style>
</head>
<body>
    <p>heloo</p>
    <p class="redd size" >hello</p>
    <p id="blue" >hello</p>
    <h3>h3 h3</h3>
```

### 文字样式

1. font-size

   ,浏览器默认16px

2. font-weight(粗细)

   关键字:normal,bold

   数字: 400,700

3. font-style(倾斜)

   normal,italic(倾斜)

4. font-family(字体)

   windows默认微软雅黑,可调为宋体，注意网页更常用微软雅黑，mac常用平方字体