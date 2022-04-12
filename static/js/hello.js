$(document).ready(function(){
    setInterval(function(){
        $.ajax({
            type:'GET',
            url :"{% url 'getNews' %}" ,
            success : function(response){
                //console.log(response);
                $("#jhh").empty();
        
                for (var key in response.q)
                {
                    // var temp="<li>" + response.q[key].article_heading+"</li>";
                    $("#blog-info").append(
                        <>
                    <h5>${response.q[key].article_heading}</h5>
                    <p>${response.q[key].article_text}</p>
                    </>
                    );
                }

            }, 
            error : function(response ){
                consoler.log("Error");
            }
        });


    }, 500);

})