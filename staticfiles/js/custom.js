/* JS Document */

/******************************

[Table of Contents]

1. Vars and Inits
2. Set Header
3. Init Custom Dropdown
4. Init Page Menu
5. Init Deals Slider
6. Init Tab Lines
7. Init Tabs
8. Init Featured Slider
9. Init Favorites
10. Init ZIndex
11. Init Popular Categories Slider
12. Init Banner 2 Slider
13. Init Arrivals Slider
14. Init Arrivals Slider ZIndex
15. Init Best Sellers Slider
16. Init Trends Slider
17. Init Reviews Slider
18. Init Recently Viewed Slider
19. Init Brands Slider
20. Init Timer


******************************/

$(document).ready(function()
{
	"use strict";

	/* 

	1. Vars and Inits

	*/

	var menuActive = false;
	var header = $('.header');

	setHeader();

	initCustomDropdown();
	initPageMenu();
	initDealsSlider();
	initTabLines();
	initFeaturedSlider();
	featuredSliderZIndex();
	initPopularSlider();
	initBanner2Slider();
	initFavs();
	initArrivalsSlider();
	arrivalsSliderZIndex();
	bestsellersSlider();
	initTabs();
	initTrendsSlider();
	initReviewsSlider();
	initViewedSlider();
	initBrandsSlider();
	initTimer();

	$(window).on('resize', function()
	{
		setHeader();
		featuredSliderZIndex();
		initTabLines();
	});

	/* 

	2. Set Header

	*/

	function setHeader()
	{
		//To pin main nav to the top of the page when it's reached
		//uncomment the following

		// var controller = new ScrollMagic.Controller(
		// {
		// 	globalSceneOptions:
		// 	{
		// 		triggerHook: 'onLeave'
		// 	}
		// });

		// var pin = new ScrollMagic.Scene(
		// {
		// 	triggerElement: '.main_nav'
		// })
		// .setPin('.main_nav').addTo(controller);

		if(window.innerWidth > 991 && menuActive)
		{
			closeMenu();
		}
	}

	/* 

	3. Init Custom Dropdown

	*/

	function initCustomDropdown()
	{
		if($('.custom_dropdown_placeholder').length && $('.custom_list').length)
		{
			var placeholder = $('.custom_dropdown_placeholder');
			var list = $('.custom_list');
		}

		placeholder.on('click', function (ev)
		{
			if(list.hasClass('active'))
			{
				list.removeClass('active');
			}
			else
			{
				list.addClass('active');
			}

			$(document).one('click', function closeForm(e)
			{
				if($(e.target).hasClass('clc'))
				{
					$(document).one('click', closeForm);
				}
				else
				{
					list.removeClass('active');
				}
			});

		});

		$('.custom_list a').on('click', function (ev)
		{
			ev.preventDefault();
			var index = $(this).parent().index();

			placeholder.text( $(this).text() ).css('opacity', '1');

			if(list.hasClass('active'))
			{
				list.removeClass('active');
			}
			else
			{
				list.addClass('active');
			}
		});


		$('select').on('change', function (e)
		{
			placeholder.text(this.value);

			$(this).animate({width: placeholder.width() + 'px' });
		});
	}

	/* 

	4. Init Page Menu
	4. Init Page Menu

	*/

	function initPageMenu()
	{
		if($('.page_menu').length && $('.page_menu_content').length)
		{
			var menu = $('.page_menu');
			var menuContent = $('.page_menu_content');
			var menuTrigger = $('.menu_trigger');

			//Open / close page menu
			menuTrigger.on('click', function()
			{
				if(!menuActive)
				{
					openMenu();
				}
				else
				{
					closeMenu();
				}
			});

			//Handle page menu
			if($('.page_menu_item').length)
			{
				var items = $('.page_menu_item');
				items.each(function()
				{
					var item = $(this);
					if(item.hasClass("has-children"))
					{
						item.on('click', function(evt)
						{
							evt.preventDefault();
							evt.stopPropagation();
							var subItem = item.find('> ul');
						    if(subItem.hasClass('active'))
						    {
						    	subItem.toggleClass('active');
								TweenMax.to(subItem, 0.3, {height:0});
						    }
						    else
						    {
						    	subItem.toggleClass('active');
						    	TweenMax.set(subItem, {height:"auto"});
								TweenMax.from(subItem, 0.3, {height:0});
						    }
						});
					}
				});
			}
		}
	}

	function openMenu()
	{
		var menu = $('.page_menu');
		var menuContent = $('.page_menu_content');
		TweenMax.set(menuContent, {height:"auto"});
		TweenMax.from(menuContent, 0.3, {height:0});
		menuActive = true;
	}

	function closeMenu()
	{
		var menu = $('.page_menu');
		var menuContent = $('.page_menu_content');
		TweenMax.to(menuContent, 0.3, {height:0});
		menuActive = false;
	}

	/* 

	5. Init Deals Slider

	*/

	function initDealsSlider()
	{
		if($('.deals_slider').length)
		{
			var dealsSlider = $('.deals_slider');
			dealsSlider.owlCarousel(
			{
				items:1,
				loop:false,
				navClass:['deals_slider_prev', 'deals_slider_next'],
				nav:false,
				dots:false,
				smartSpeed:1200,
				margin:30,
				autoplay:false,
				autoplayTimeout:5000
			});

			if($('.deals_slider_prev').length)
			{
				var prev = $('.deals_slider_prev');
				prev.on('click', function()
				{
					dealsSlider.trigger('prev.owl.carousel');
				});	
			}

			if($('.deals_slider_next').length)
			{
				var next = $('.deals_slider_next');
				next.on('click', function()
				{
					dealsSlider.trigger('next.owl.carousel');
				});	
			}
		}
	}

	/* 

	6. Init Tab Lines

	*/

	function initTabLines()
	{
		if($('.tabs').length)
		{
			var tabs = $('.tabs');

			tabs.each(function()
			{
				var tabsItem = $(this);
				var tabsLine = tabsItem.find('.tabs_line span');
				var tabGroup = tabsItem.find('ul li');

				var posX = $(tabGroup[0]).position().left;
				tabsLine.css({'left': posX, 'width': $(tabGroup[0]).width()});
				tabGroup.each(function()
				{
					var tab = $(this);
					tab.on('click', function()
					{
						if(!tab.hasClass('active'))
						{
							tabGroup.removeClass('active');
							tab.toggleClass('active');
							var tabXPos = tab.position().left;
							var tabWidth = tab.width();
							tabsLine.css({'left': tabXPos, 'width': tabWidth});
						}
					});
				});
			});
		}
	}

	/* 

	7. Init Tabs

	*/

	function initTabs()
	{
		if($('.tabbed_container').length)
		{
			//Handle tabs switching

			var tabsContainers = $('.tabbed_container');
			tabsContainers.each(function()
			{
				var tabContainer = $(this);
				var tabs = tabContainer.find('.tabs ul li');
				var panels = tabContainer.find('.panel');
				var sliders = panels.find('.slider');

				tabs.each(function()
				{
					var tab = $(this);
					tab.on('click', function()
					{
						panels.removeClass('active');
						var tabIndex = tabs.index(this);
						$($(panels[tabIndex]).addClass('active'));
						sliders.slick("unslick");
						sliders.each(function()
						{
							var slider = $(this);
							// slider.slick("unslick");
							if(slider.hasClass('bestsellers_slider'))
							{
								initBSSlider(slider);
							}
							if(slider.hasClass('featured_slider'))
							{
								initFSlider(slider);
							}
							if(slider.hasClass('arrivals_slider'))
							{
								initASlider(slider);
							}
						});
					});	
				});
			});
		}
	}

	/* 

	8. Init Featured Slider

	*/

	function initFeaturedSlider()
	{
		if($('.featured_slider').length)
		{
			var featuredSliders = $('.featured_slider');
			featuredSliders.each(function()
			{
				var featuredSlider = $(this);
				initFSlider(featuredSlider);
			});
				
		}
	}

	function initFSlider(fs)
	{
		var featuredSlider = fs;
		featuredSlider.on('init', function()
		{
			var activeItems = featuredSlider.find('.slick-slide.slick-active');
			for(var x = 0; x < activeItems.length - 1; x++)
			{
				var item = $(activeItems[x]);
				item.find('.border_active').removeClass('active');
				if(item.hasClass('slick-active'))
				{
					item.find('.border_active').addClass('active');
				}
			}
		}).on(
		{
			afterChange: function(event, slick, current_slide_index, next_slide_index)
			{
				var activeItems = featuredSlider.find('.slick-slide.slick-active');
				activeItems.find('.border_active').removeClass('active');
				for(var x = 0; x < activeItems.length - 1; x++)
				{
					var item = $(activeItems[x]);
					item.find('.border_active').removeClass('active');
					if(item.hasClass('slick-active'))
					{
						item.find('.border_active').addClass('active');
					}
				}
			}
		})
		.slick(
		{
			rows:2,
			slidesToShow:4,
			slidesToScroll:4,
			infinite:false,
			arrows:false,
			dots:true,
			responsive:
			[
				{
					breakpoint:768, settings:
					{
						rows:2,
						slidesToShow:3,
						slidesToScroll:3,
						dots:true
					}
				},
				{
					breakpoint:575, settings:
					{
						rows:2,
						slidesToShow:2,
						slidesToScroll:2,
						dots:false
					}
				},
				{
					breakpoint:480, settings:
					{
						rows:1,
						slidesToShow:1,
						slidesToScroll:1,
						dots:false
					}
				}
			]
		});
	}

	/* 

	9. Init Favorites

	*/

	function initFavs()
	{
		// Handle Favorites
		var items = document.getElementsByClassName('product_fav');
		for(var x = 0; x < items.length; x++)
		{
			var item = items[x];
			item.addEventListener('click', function(fn)
			{
				fn.target.classList.toggle('active');
			});
		}
	}

	/* 

	10. Init ZIndex

	*/

	function featuredSliderZIndex()
	{
		// Hide slider dots on item hover
		var items = document.getElementsByClassName('featured_slider_item');
		
		for(var x = 0; x < items.length; x++)
		{
			var item = items[x];
			item.addEventListener('mouseenter', function()
			{
				$('.featured_slider .slick-dots').css('display', "none");
			});

			item.addEventListener('mouseleave', function()
			{
				$('.featured_slider .slick-dots').css('display', "block");
			});
		}
	}

	/* 

	11. Init Popular Categories Slider

	*/

	function initPopularSlider()
	{
		if($('.popular_categories_slider').length)
		{
			var popularSlider = $('.popular_categories_slider');

			popularSlider.owlCarousel(
			{
				loop:true,
				autoplay:false,
				nav:false,
				dots:false,
				responsive:
				{
					0:{items:1},
					575:{items:2},
					640:{items:3},
					768:{items:4},
					991:{items:5}
				}
			});

			if($('.popular_categories_prev').length)
			{
				var prev = $('.popular_categories_prev');
				prev.on('click', function()
				{
					popularSlider.trigger('prev.owl.carousel');
				});
			}

			if($('.popular_categories_next').length)
			{
				var next = $('.popular_categories_next');
				next.on('click', function()
				{
					popularSlider.trigger('next.owl.carousel');
				});
			}
		}
	}

	/* 

	12. Init Banner 2 Slider

	*/

	function initBanner2Slider()
	{
		if($('.banner_2_slider').length)
		{
			var banner2Slider = $('.banner_2_slider');
			banner2Slider.owlCarousel(
			{
				items:1,
				loop:true,
				nav:false,
				dots:true,
				dotsContainer: '.banner_2_dots',
				smartSpeed:1200
			});
		}
	}

	/* 

	13. Init Arrivals Slider

	*/

	function initArrivalsSlider()
	{
		if($('.arrivals_slider').length)
		{
			var arrivalsSliders = $('.arrivals_slider');
			arrivalsSliders.each(function()
			{
				var arrivalsSlider = $(this);
				initASlider(arrivalsSlider);
			});	
			
		}
	}

	function initASlider(as)
	{
		var arrivalsSlider = as;
		arrivalsSlider.on('init', function()
		{
			var activeItems = arrivalsSlider.find('.slick-slide.slick-active');
			for(var x = 0; x < activeItems.length - 1; x++)
			{
				var item = $(activeItems[x]);
				item.find('.border_active').removeClass('active');
				if(item.hasClass('slick-active'))
				{
					item.find('.border_active').addClass('active');
				}
			}
		}).on(
		{
			afterChange: function(event, slick, current_slide_index, next_slide_index)
			{
				var activeItems = arrivalsSlider.find('.slick-slide.slick-active');
				activeItems.find('.border_active').removeClass('active');
				for(var x = 0; x < activeItems.length - 1; x++)
				{
					var item = $(activeItems[x]);
					item.find('.border_active').removeClass('active');
					if(item.hasClass('slick-active'))
					{
						item.find('.border_active').addClass('active');
					}
				}
			}
		})
		.slick(
		{
			rows:2,
			slidesToShow:5,
			slidesToScroll:5,
			infinite:false,
			arrows:false,
			dots:true,
			responsive:
			[
				{
					breakpoint:768, settings:
					{
						rows:2,
						slidesToShow:3,
						slidesToScroll:3,
						dots:true
					}
				},
				{
					breakpoint:575, settings:
					{
						rows:2,
						slidesToShow:2,
						slidesToScroll:2,
						dots:false
					}
				},
				{
					breakpoint:480, settings:
					{
						rows:1,
						slidesToShow:1,
						slidesToScroll:1,
						dots:false
					}
				}
			]
		});
	}

	/* 

	14. Init Arrivals Slider ZIndex

	*/

	function arrivalsSliderZIndex()
	{
		// Hide slider dots on item hover
		var items = document.getElementsByClassName('arrivals_slider_item');
		
		for(var x = 0; x < items.length; x++)
		{
			var item = items[x];
			item.addEventListener('mouseenter', function()
			{
				$('.arrivals_slider .slick-dots').css('display', "none");
			});

			item.addEventListener('mouseleave', function()
			{
				$('.arrivals_slider .slick-dots').css('display', "block");
			});
		}
	}

	/* 

	15. Init Best Sellers Slider

	*/

	function bestsellersSlider()
	{
		if($('.bestsellers_slider').length)
		{
			var bestsellersSliders = $('.bestsellers_slider');
			bestsellersSliders.each(function()
			{
				var bestsellersSlider = $(this);

				initBSSlider(bestsellersSlider);
			})	
		}
	}

	function initBSSlider(bss)
	{
		var bestsellersSlider = bss;

		bestsellersSlider.slick(
		{
			rows:2,
			infinite:true,
			slidesToShow:3,
			slidesToScroll:3,
			arrows:false,
			dots:true,
			autoplay: true,
  			autoplaySpeed: 6000,
			responsive:
			[
				{
					breakpoint:1199, settings:
					{
						rows:2,
						slidesToShow:2,
						slidesToScroll:2,
						dots:true
					}
				},
				{
					breakpoint:991, settings:
					{
						rows:2,
						slidesToShow:2,
						slidesToScroll:2,
						dots:true
					}
				},
				{
					breakpoint:575, settings:
					{
						rows:1,
						slidesToShow:1,
						slidesToScroll:1,
						dots:false
					}
				}
			]
		});
	}

	/* 

	16. Init Trends Slider

	*/

	function initTrendsSlider()
	{
		if($('.trends_slider').length)
		{
			var trendsSlider = $('.trends_slider');
			trendsSlider.owlCarousel(
			{
				loop:false,
				margin:30,
				nav:false,
				dots:false,
				autoplayHoverPause:true,
				autoplay:false,
				responsive:
				{
					0:{items:1},
					575:{items:2},
					991:{items:3}
				}
			});

			trendsSlider.on('click', '.trends_fav', function (ev)
			{
			    $(ev.target).toggleClass('active');
			});

			if($('.trends_prev').length)
			{
				var prev = $('.trends_prev');
				prev.on('click', function()
				{
					trendsSlider.trigger('prev.owl.carousel');
				});
			}

			if($('.trends_next').length)
			{
				var next = $('.trends_next');
				next.on('click', function()
				{
					trendsSlider.trigger('next.owl.carousel');
				});
			}
		}
	}

	/* 

	17. Init Reviews Slider

	*/

	function initReviewsSlider()
	{
		if($('.reviews_slider').length)
		{
			var reviewsSlider = $('.reviews_slider');

			reviewsSlider.owlCarousel(
			{
				items:3,
				loop:true,
				margin:30,
				autoplay:false,
				nav:false,
				dots:true,
				dotsContainer: '.reviews_dots',
				responsive:
				{
					0:{items:1},
					768:{items:2},
					991:{items:3}
				}
			});
		}
	}

	/* 

	18. Init Recently Viewed Slider

	*/

	function initViewedSlider()
	{
		if($('.viewed_slider').length)
		{
			var viewedSlider = $('.viewed_slider');

			viewedSlider.owlCarousel(
			{
				loop:true,
				margin:30,
				autoplay:true,
				autoplayTimeout:6000,
				nav:false,
				dots:false,
				responsive:
				{
					0:{items:1},
					575:{items:2},
					768:{items:3},
					991:{items:4},
					1199:{items:6}
				}
			});

			if($('.viewed_prev').length)
			{
				var prev = $('.viewed_prev');
				prev.on('click', function()
				{
					viewedSlider.trigger('prev.owl.carousel');
				});
			}

			if($('.viewed_next').length)
			{
				var next = $('.viewed_next');
				next.on('click', function()
				{
					viewedSlider.trigger('next.owl.carousel');
				});
			}
		}
	}

	/* 

	19. Init Brands Slider

	*/

	function initBrandsSlider()
	{
		if($('.brands_slider').length)
		{
			var brandsSlider = $('.brands_slider');

			brandsSlider.owlCarousel(
			{
				loop:true,
				autoplay:true,
				autoplayTimeout:5000,
				nav:false,
				dots:false,
				autoWidth:true,
				items:8,
				margin:42
			});

			if($('.brands_prev').length)
			{
				var prev = $('.brands_prev');
				prev.on('click', function()
				{
					brandsSlider.trigger('prev.owl.carousel');
				});
			}

			if($('.brands_next').length)
			{
				var next = $('.brands_next');
				next.on('click', function()
				{
					brandsSlider.trigger('next.owl.carousel');
				});
			}
		}
	}

	/* 

	20. Init Timer

	*/

	function initTimer()
    {
    	if($('.deals_timer_box').length)
    	{
    		var timers = $('.deals_timer_box');
    		timers.each(function()
    		{
    			var timer = $(this);

    			var targetTime;
    			var target_date;

    			// Add a date to data-target-time of the .deals_timer_box
    			// Format: "Feb 17, 2018"
    			if(timer.data('target-time') !== "")
    			{
    				targetTime = timer.data('target-time');
					target_date = new Date(targetTime).getTime();
    			}
    			else
    			{
    				var date = new Date();
			    	date.setDate(date.getDate() + 3);
			    	target_date = date.getTime();
    			}

				// variables for time units
				var days, hours, minutes, seconds;

				var h = timer.find('.deals_timer_hr');
				var m = timer.find('.deals_timer_min');
				var s = timer.find('.deals_timer_sec');

				setInterval(function ()
				{
				    // find the amount of "seconds" between now and target
				    var current_date = new Date().getTime();
				    var seconds_left = (target_date - current_date) / 1000;
				    console.log(seconds_left);
				 
				    // do some time calculations
				    days = parseInt(seconds_left / 86400);
				    seconds_left = seconds_left % 86400;
				    
				    hours = parseInt(seconds_left / 3600);
				    hours = hours + days * 24;
				    seconds_left = seconds_left % 3600;
				    
				     
				    minutes = parseInt(seconds_left / 60);
				    seconds = parseInt(seconds_left % 60);

				    if(hours.toString().length < 2)
				    {
				    	hours = "0" + hours;
				    }
				    if(minutes.toString().length < 2)
				    {
				    	minutes = "0" + minutes;
				    }
				    if(seconds.toString().length < 2)
				    {
				    	seconds = "0" + seconds;
				    }

				    // display results
				    h.text(hours);
				    m.text(minutes);
				    s.text(seconds); 
				 
				}, 1000);
    		});	
    	}	
    }
});


// my-js


function picture_one(){ 
	document.getElementById('product_inner_slider').display = block;
	// var pic = "http://img.tesco.com/Groceries/pi/118/5000175411118/IDShot_90x90.jpg"
	// document.getElementById('bigpic').src = pic.replace('90x90', '225x225');

	}


     // Hide submenus
	 $('#body-row .collapse').collapse('hide'); 

	 // Collapse/Expand icon
	 $('#collapse-icon').addClass('fa-angle-double-left'); 
	 
	 // Collapse click
	 $('[data-toggle=sidebar-colapse]').click(function() {
		 SidebarCollapse();
	 });
	 
	 function SidebarCollapse () {
		 $('.menu-collapsed').toggleClass('d-none');
		 $('.sidebar-submenu').toggleClass('d-none');
		 $('.submenu-icon').toggleClass('d-none');
		 $('#sidebar-container').toggleClass('sidebar-expanded sidebar-collapsed');
		 
		 // Treating d-flex/d-none on separators with title
		 var SeparatorTitle = $('.sidebar-separator-title');
		 if ( SeparatorTitle.hasClass('d-flex') ) {
			 SeparatorTitle.removeClass('d-flex');
		 } else {
			 SeparatorTitle.addClass('d-flex');
		 }
		 
		 // Collapse/Expand icon
		 $('#collapse-icon').toggleClass('fa-angle-double-left fa-angle-double-right');
	 }


	

	 function  myfncr() {
		document.getElementById('div_one').style.display = "none";
		document.getElementById('div_two').style.display = "block";
	}



	
//chart_three

var data = [{
	"annee": 2016,
	"data": {
	  "indicDab": 0.86,
	  "indicDag": 0.74,
	  "indicDam": 0.72
	}
  }, {
	"annee": 2017,
	"data": {
	  "indicDab": 1,
	  "indicDag": 0.72,
	  "indicDam": 0.80
	}
  }, {
	"annee": 2018,
	"data": {
	  "indicDab": 0.75,
	  "indicDag": 0.7134831460674157,
	  "indicDam": 0.8478802992518704
	}
  }, {
	"annee": 2019,
	"data": {
	  "indicDab": 1,
	  "indicDag": 0.8799019607843137,
	  "indicDam": 0.9259259259259259
	}
  }, {
	"annee": 2020,
	"data": {
	  "indicDab": 1,
	  "indicDag": 0.8948948948948949,
	  "indicDam": 0.905940594059406
	}
  }];
  
  
  var labels = [],
	dab = [],
	dag = [],
	dam = [];
  data.forEach(function(elt) {
	labels.push(elt.annee);
	dab.push(Math.ceil(elt.data.indicDab * 100));
	dag.push(Math.ceil(elt.data.indicDag * 100));
	dam.push(Math.ceil(elt.data.indicDam * 100));
  });
  
  var indicateursData = {
	labels: labels,
	datasets: [{
	  label: 'DAB',
	  fill: false,
	  borderColor: "rgba(255, 108, 110, 1)",
	  backgroundColor: "rgba(255, 108, 110, 1)",
	  pointBackgroundColor: "rgba(255, 108, 110, 1)",
	  pointBorderColor: "#fff",
	  pointHoverBackgroundColor: '#fff',
	  pointHoverBorderColor: "rgba(255, 108, 110, 1)",
	  borderWidth: 3,
	  pointBorderWidth: 1,
	  data: dab
	}, {
	  label: 'DAG',
	  fill: false,
	  borderColor: "rgba(50, 155, 255, 1)",
	  backgroundColor: "rgba(50, 155, 255, 1)",
	  pointBackgroundColor: "rgba(50, 155, 255, 1)",
	  pointBorderColor: "#fff",
	  pointHoverBackgroundColor: '#fff',
	  pointHoverBorderColor: "rgba(50, 155, 255, 1)",
	  borderWidth: 3,
	  pointBorderWidth: 1,
	  data: dag
	}, {
	  label: 'DAM',
	  fill: false,
	  borderColor: "rgba(0, 166, 0, 1)",
	  backgroundColor: "rgba(0, 166, 0, 1)",
	  pointBackgroundColor: "rgba(0, 166, 0, 1)",
	  pointBorderColor: '#fff',
	  pointHoverBackgroundColor: '#fff',
	  pointHoverBorderColor: "rgba(0, 166, 0, 1)",
	  borderWidth: 3,
	  pointBorderWidth: 1,
	  data: dam
	}]
  };
  
  var config = {
	type: 'line',
	data: indicateursData,
	options: {
	  tooltips: {
		mode: 'label',
		bodySpacing: 6,
		titleMarginBottom: 10,
		titleFontSize: 14,
		bodyFontSize: 14,
		callbacks: {
		  label: function(tooltipItem, data) {
			return data.datasets[tooltipItem.datasetIndex].label + ': ' +
			  data.datasets[tooltipItem.datasetIndex].data[tooltipItem.index] + '%';
		  }
		}
	  },
	  hover: {
		mode: 'dataset'
	  },
	  maintainAspectRatio: false,
	  scales: {
		yAxes: [{
		  ticks: {
			beginAtZero: false,
			min: 50,
			stepSize: 10
		  },
		  gridLines: {
			color: "rgba(0, 0, 0, 0.06)",
			zeroLineColor: "rgba(0,0,0,0.1)",
			offsetGridLines: false
		  }
		}],
		xAxes: [{
		  ticks: {
			maxRotation: 0,
			minRotation: 0
		  },
		  gridLines: {
			color: "rgba(0, 0, 0, 0.06)",
			zeroLineColor: "rgba(0,0,0,0.1)",
			offsetGridLines: false
		  }
		}]
	  },
	  elements: {
		line: {
		  borderWidth: 2
		},
		point: {
		  radius: 4,
		  borderColor: "#ffffff",
		}
	  },
	  legend: {
		display: true,
		position: 'bottom',
		labels: {
		  boxWidth: 20,
		  padding: 20
		}
	  },
	  drawHorizontalLine: {
		lineY: [80, 80],
		lineColor: "rgba(50, 155, 255, 0.85)",
		text: 'Obj 67 & 68',
		textPosition: 720,
		textFont: '18px sans-serif',
		textColor: "rgba(50, 155, 255, 0.85)"
	  }
	}
  };
  
  Chart.pluginService.register({
	beforeDraw: function(chartInstance, easing) {
	  var lineOpts = chartInstance.options.drawHorizontalLine;
	  if (lineOpts) {
  
		var yAxis = chartInstance.scales["y-axis-0"];
		var yValueStart = yAxis.getPixelForValue(lineOpts.lineY[0], 0, 0, true);
		var yValueEnd = yAxis.getPixelForValue(lineOpts.lineY[1], 0, 0, true);
  
		var xAxis = chartInstance.scales["x-axis-0"];
		var xValueStart = xAxis.getPixelForTick(0) - 5;
		//var xValueEnd = xAxis.getPixelForTick(xAxis.ticks.length-1) + 15/*xAxis.right*/;
		var xValueEnd = xAxis.right;
  
		console.log('xValueEnd', xValueEnd);
		console.log('xAxis.ticks.length', xAxis.ticks.length);
		console.log(xAxis.getPixelForTick(xAxis.ticks.length - 1));
  
		var ctx = chartInstance.chart.ctx;
		ctx.save();
  
		// le texte
		ctx.font = lineOpts.textFont;
		ctx.fillStyle = lineOpts.textColor;
		ctx.fillText(lineOpts.text, lineOpts.textPosition, yValueStart + 8);
  
		// la ligne en pointillés
  
		ctx.setLineDash([15, 15]);
		ctx.strokeStyle = lineOpts.lineColor;
		ctx.lineWidth = 2.5;
		ctx.beginPath();
		ctx.moveTo(xValueStart, yValueStart);
		ctx.lineTo(xValueEnd, yValueEnd);
		ctx.stroke();
  
		ctx.restore();
	  }
	}
  });
  
  var ctxLineChart = document.getElementById("indicateursChart").getContext("2d");

  var lineChart = new Chart(ctxLineChart, config);

  
  //chart_four


  var options = {
	type: 'line',
	data: {
	  labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
	  datasets: [
		  {
			label: '# of Votes',
			data: [12, 19, 3, 5, 2, 3],
			borderWidth: 1
		  },	
			  {
				  label: '# of Points',
				  data: [7, 11, 5, 8, 3, 7],
				  borderWidth: 1
			  }
		  ]
	},
	options: {
		scales: {
		  yAxes: [{
		  ticks: {
					  reverse: false
		  }
		}]
	  }
	} 
  };
  
  var lineCanvas = document.getElementById("chartJSContainer");
 
		 
  var ctx = lineCanvas.getContext('2d');
  var lineChart = new Chart(ctx, options);
  
  console.log("INSIDE lineChart::")
  console.log(lineChart)
  
  lineCanvas.onclick = function (e) {
	 console.log("INSIDE lineChart::")
	 console.log(lineChart)
  
	 var firstPoint  = lineChart.getElementAtEvent(e);
	 console.log("firstPoint::")
	 console.log( firstPoint )
  
	 if (firstPoint) {
	   console.log("lineChart.data::")
	   console.log( lineChart.data )
	   var first_point_index= firstPoint._index
	   console.log("+1 first_point_index::")
	   console.log( first_point_index )
  
	   var firstPoint_dataset_index= firstPoint._datasetIndex
	   console.log("+2 first_point_index::")
	   console.log( first_point_index )
	   
	   var label = lineChart.data.labels[firstPoint._index];
	   console.log("+3 label::")
	   console.log( label )
	   
	   var value = lineChart.data.datasets[firstPoint._datasetIndex].data[firstPoint._index];
	   alert( "label::"+(label) + "  value::"+(value) )
	 }
  } // lineChart.onclick = function(e) {
  
  
 

	

