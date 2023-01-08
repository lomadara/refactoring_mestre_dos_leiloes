function carouselLoop() {        
    setTimeout(function() {
        var content = document.getElementsByClassName('card_carousel'); 
        
        var card_1 = content[0]
        var card_2 = content[1]
        var card_3 = content[2]
        var card_4 = content[3]
        var card_5 = content[4]
        
        content[0].parentNode.insertBefore(card_5, content[0]);
        content[1].parentNode.insertBefore(card_1, content[1]);
        content[2].parentNode.insertBefore(card_2, content[2]);
        content[3].parentNode.insertBefore(card_3, content[3]);
        content[4].parentNode.insertBefore(card_4, content[4]);

        content[0].id = "card_id0"
        content[1].id = "card_id1"
        content[2].id = "card_id2"
        content[3].id = "card_id3"
        content[4].id = "card_id4"     
        
        carouselLoop();             
                              
    }, 8000)
}

carouselLoop();
