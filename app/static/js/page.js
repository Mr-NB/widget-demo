function Page() {
    this.container = $(".register_login");
    //console.log(this.container);
    this.flag = true;
    this.init();

}


Page.prototype = {
    init:function(){
        this.createContent();
    },
    createContent:function(params=this.flag){
        this.container.html('')
        if(params){

            this.login =  new Login(this.container);
        }else{

            this.register = new Register(this.container);
        }
    }
}

new Page();