//document.getElementById('veg_garden_disruption').innerHTML="<h3>Veg Garden Disruption</h3><span>The old-fashion lady screamed at the boy:'Stop immediately naught devil!'.But he didn't because he had a screw loose and continued to ravage the old lady's veg garden.</span>";

function get_text(file_path){
    var req = new XMLHttpRequest();
    req.open("GET", file_path, false);
    req.send(null);
    return req.responseText.split(/\n{2,}/g);//at least 2 \n Globally
}
//slice without end reaches the end of str
function text_to_object(file_path){
    var stories_list = get_text(file_path);
    var title_body = {};
    for (count = 0; count < stories_list.length; count++) {
        var current = stories_list[count].split("\n");
        title_body[current[0]] = current.slice(1);
    }
    return title_body;
}



function change_content(id, content){
    document.getElementById(id).innerHTML=func().content;
    alert(get_text("../text/stories.txt"));
}
alert(text_to_object("../text/stories.txt")["Veg Garden Disruption"]);

//Words api to be used via mashape account
$.ajax({
    url: 'https://SOMEAPI.p.mashape.com/', // The URL to the API. You can get this in the API page of the API you intend to consume
    type: 'GET', // The HTTP Method, can be GET POST PUT DELETE etc
    data: {}, // Additional parameters here
    dataType: 'json',
    success: function(data) { console.dir((data.source)); },
    error: function(err) { alert(err); },
    beforeSend: function(xhr) {
    xhr.setRequestHeader("X-Mashape-Authorization", "YOUR-MASHAPE-KEY"); // Enter here your Mashape key
    }
});
