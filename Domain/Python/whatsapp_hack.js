(function() {
    function t() {
        var t = "<style>div{margin:1em;display:inline-block;max-width:300px}img{object-fit:cover;width:300px;height:200px;}span{float:right;font-size:.85em}h3{padding:10px 5px;font-size:1em}h2{margin:2em;font-size:1.1em;line-height:1.4em}</style>";
        for (var e in list) t += action ? '<div><img src="' + list[e].thumb.replace("t=s", "t=l") + '"><h3>' + list[e].name + "<span>+" + e + "</span></h3></div>" : list[e].name + "," + e + "<br>";
        action && (t += "the great bhansa"), $("body").html(t).css("padding", "10px").css("overflow", "visible")
    }

    function e() {
        $("div.chat").each(function() {
            var t = $(this).find("img.avatar-image.is-loaded"),
                e = $(this).find("div.chat-title"),
                ls = $(this).find("div span.chat-time");
            if (t && t[0] && e && e[0]) {
                var a = t[0].src.match(/u=(\d*)/);
                a && ($("span.drawer-title-body").html("Extracting contacts " + "....".substring(Math.ceil(4 * Math.random()))), list[a[1]] = {
                    thumb: t[0].src,
                    name: e[0].innerText
                })
            }
        }), old = $("div.drawer-body").scrollTop(), $("div.drawer-body").scrollTop(old + 72), old != $("div.drawer-body").scrollTop() ? setTimeout(e, 200) : t()
    }
    var a = document.createElement("script");
    a.src = "https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js", document.getElementsByTagName("head")[0].appendChild(a),action = !0, list = {}, old = -1, count = 0, -1 == old && (document.getElementsByClassName("icon-chat")[0].click(), action = confirm("Press OK to create a photo address book or press Cancel to create a CSV file that you can later import into your Google contacts."), setTimeout(e, 1e3))
}());

//Another Method 
/*
function getWhatsAppAddressBook() {
 
    /* Switch to the All Contacts view in WhatsApp */
    $("button.icon-chat").click();
 
    var list = {}, position = -1;
 
    if (position != $("div.drawer-body").scrollTop()) {
 
        $("div.chat").each(function(i) {
 
            /* Get the profile picture of the WhatsApp contact */
            var img   = $(this).find("img.avatar-image.is-loaded"); 
            aler(img);
 
            /* Extract the Contact Full Name */
            var title = $(this).find("div.chat-title"); 
 
            /* Extract the WhatsApp Phone number */
            var tel = img[0].src.match(/u=(\d*)/); 
 
            /* Save the entry in an associated array */
            list[tel[1]] = {thumb: img[0].src, name: title[0].innerText}; 
 
        });
 
        position = $("div.drawer-body").scrollTop();
        $("div.drawer-body").scrollTop(position + 72); 
 
    }
 
    console.log(list);
 
}
*/