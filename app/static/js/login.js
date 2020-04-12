//创建一个Login：
function Login(container) {
    //容器实例属性：
    this.container = container;
    //调用入口方法：
    this.init();
}

//引入html标签：
Login.template = `
 <div class = "register content">
    <div class="logo">
            <img src="https://cas.1000phone.net/cas/images/login/logo.png">
    </div>
    <form class = "register-form">
        <div class="form-group">
            <label for="exampleInputEmail1">用户名</label>
            <input type="email" class="form-control register_username" id="exampleInputEmail1" placeholder="Username">
        </div>
        <div class="form-group">
            <label for="exampleInputPassword1">密码</label>
            <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
        </div>
        <button type="button" class="btn btn-success register_btn1" id = "register_btn1">去登陆</button>
        <button type="submit" class="btn btn-info register_btn">注册</button>
    </form>
</div>`

//Login的原型方法：
Login.prototype = {
    init:function(){
    this.createDom();
    },
    createDom:function(){
        this.el = $("<div class='content'></div>");
        this.el.append(Login.template);
        console.log(Login.template)
        this.container.append(this.el);
    }
}

new Page();