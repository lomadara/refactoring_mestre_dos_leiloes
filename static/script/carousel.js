function carouselLoop() {        
    setTimeout(function() {
        var content = document.getElementsByClassName('card_carousel'); 
        
        var first_item = content[0]
        var second_item = content[1]
        var third_item = content[2]
        var fourth_item = content[3]
        var last_item = content[4]
        
        content[0].parentNode.insertBefore(last_item, content[0]);
        content[0].id = "card_id0"
        content[1].parentNode.insertBefore(first_item, content[1]);
        content[1].id = "card_id1"
        content[2].parentNode.insertBefore(second_item, content[2]);
        content[2].id = "card_id2"
        content[3].parentNode.insertBefore(third_item, content[3]);
        content[3].id = "card_id3"
        content[4].parentNode.insertBefore(fourth_item, content[4]);
        content[4].id = "card_id4"     
        
        carouselLoop();             
                              
    }, 5000)
}

carouselLoop();
