var express = require("express"),
    request = require("request"),
    bodyParser  =   require("body-parser"),
    app         =   express();

app.set("view engine","ejs");
app.use(express.static("public"));
app.use(bodyParser.urlencoded({extended : true}));

var priceList
var url = 'http://127.0.0.1:5000/price'


app.get("/",function(req,res){
    
    request.get(url,function(err,res,body){
        priceList = JSON.parse(body);
        console.log(priceList['stats']['BTC'])
    });
    res.render("index",{priceList:priceList});
});

app.listen(8080,function(){
    console.log("Server is running")
})