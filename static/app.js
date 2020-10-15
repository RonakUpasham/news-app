
var i = 0;
var articles;
var headlines;
var img_links;
var website_names;
var website_links;


$(document).ready(function() {
  renderDisplay();
  $('button:contains("All News")').click();
});


function renderDisplay() { 
  document.querySelector(".article-cont").style.visibility = "hidden"; 
  document.querySelector(".loading").style.visibility = "visible"; 
}; 


  $('.btn-dark').bind('click', function() {
    renderDisplay();
    $.getJSON('/interactive',{category: (this.value)}, function(data) {
       articles=[]
       articles = data.articles;
       headlines = data.headlines;
       img_links = data.img_links;
       website_links = data.website_links;
       website_names = data.website_names;
       i = 0;
       display();
    });
    return false;
  });


function display() {
      document.querySelector(".loading").style.display = "none"; 
      document.querySelector(".article-cont").style.visibility = "visible";
      $("#article-text").text(articles[i]);
      $("#headline").text(headlines[i]);
      $(".img-section").css({ "background": "url(" + img_links[i] + ")",   "background-size": "cover",
      "background-position-x": "50%",
      "background-position-y": "50%",
      "box-shadow": "5px 10px 8px #888888",
      "border-radius": "25px",
      "border": "2px solid black",
      "max-height": "350px",
      "height": "350px",
      "overflow-x": "hidden",
      "overflow-y": "hidden" });
      $("#full-article a").attr("href", website_links[i])
      $("#website_names").text(website_names[i]);
}


$('#prevArticle').bind('click', function() {
  console.log(i);
  console.log(articles.length);
  if(i==0){
    i = articles.length;
  }
    i = i-1;
    display();
  });

$('#nextArticle').bind('click', function() {
  console.log(i);
  console.log(articles.length);
  if(i==articles.length-1){
    i = -1;
  }
    i = i+1;
    display();
  });



$(".btn-group > .btn").click(function(){
  $(this).addClass("active").siblings().removeClass("active");
});
