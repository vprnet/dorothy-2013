$("#past-book-btn").on("click",function(){$("#past-books").css("display","block");$("#upcoming-books").css("display","none");$("#about-dorothy").css("display","none");$(this).attr("class","btn btn-success");$("#upcoming-book-btn").attr("class","btn btn-primary");$("#about-dorothy-btn").attr("class","btn btn-primary")});$("#upcoming-book-btn").on("click",function(){$("#past-books").css("display","none");$("#upcoming-books").css("display","block");$("#about-dorothy").css("display","none");$(this).attr("class","btn btn-success");$("#past-book-btn").attr("class","btn btn-primary");$("#about-dorothy-btn").attr("class","btn btn-primary")});$("#about-dorothy-btn").on("click",function(){$("#past-books").css("display","none");$("#upcoming-books").css("display","none");$("#about-dorothy").css("display","block");$(this).attr("class","btn btn-success");$("#upcoming-book-btn").attr("class","btn btn-primary");$("#past-book-btn").attr("class","btn btn-primary")});$("a.audio_play").click(function(){if(this.firstChild.paused===!1){this.firstChild.pause();$(this).children("button").children("span.glyphicon").attr("class","glyphicon glyphicon-play")}else{this.firstChild.play();$(this).children("button").children("span.glyphicon").attr("class","glyphicon glyphicon-pause")}});