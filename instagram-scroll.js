/**********
*  Setup  *
***********/

// Tag to display
var tag_name = 'helsinki';

// Your client id (given by instagram api)
var client_id = '5b8ae8f010d64112a48f969b6af736d5';

var thumb_dimension = 220;

var div_to_add_pics = '#holder';
// Include Instagram caption with image?
var include_caption = false;
// Include Instagram username with image?
var include_username = false;

var window_width;


var url = 'https://api.instagram.com/v1/tags/'+tag_name+'/media/recent?client_id='+client_id;

/************************
*   Load and Process    *
*************************/

// Grab JSON data from Instagram
function LoadResults(){
		$.ajax({
			dataType:'jsonp',
			url:url,
			success:function(response){
				// Send data to be processed
				return ProcessData(response);
			}
		});
	};

// Process JSON data by creating a <ul> and adding each image
// as a <li>
function ProcessData(response){
	if(response != null){
		$(response.data).each(function(index,obj){
            var items = "<a href ='"+obj.link+ "'><img src = '" + obj.images.thumbnail.url + "' class='item'/></a>";
            $(div_to_add_pics).prepend( $( items ) );
            if(index == 20)
    			return response.pagination.next_url;
        });

        url = response.pagination.next_url;
    }
};

/*********
 * Setup *
 *********/

var nextLink = false;
var loadingImages = false;

/******************
 *     Scroll	 *
 ******************/

/* Loads the next set of images and appends them to #div_to_add_pics */
function loadNext() {
  	// Prevent (redundantly) loading images if we're already loading them,
  	// and prevent us from entering an infinite loop
  	if (loadingImages || nextLink == url) {
  	  return false;
  	}else{
	// We are now loading images!
	loadingImages = true;

	LoadResults();
	nextLink = url;

    // Aaaaaand we're done loading.
    loadingImages = false;
    }
  
}
 
/* When the user scrolls to the bottom of the page, load the next set
 * of images */

var last_load = 0;

var scrollDiv = function (dir, px) {
    $(scroller).animate({
        scrollLeft: go + px  // becomes '-=int' or '+=int' 
    }, 500); // duration
};

function animateScroll(target, speed){
    $(target).animate(
        {
            'top': $(window).scrollTop() + $(window).height()
        },
        {
            duration: speed,
            complete: function(){
                animateScroll(this, speed);
                loadNext();
            }
        }
    );
};

animateScroll($('#holder'), 5000);

var offset = 500; // Change for distance to load
  
