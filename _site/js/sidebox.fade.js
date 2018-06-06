
$(function() {

			var $el, $ps, $up, totalHeight;
			var $orgHeight = $('.sidebar-box').height();
			// console.log($orgHeight);

			$(".sidebar-box .read-more-button").click(function() {

				// IE 7 doesn't even get this far. I didn't feel like dicking with it.

				totalHeight = 0

				$el = $(this);
				$p  = $el.parent();
				$up = $p.parent();
				$ps = $up.find("p:not('.read-more')");

				// measure how tall inside should be by adding together heights of all inside paragraphs (except read-more paragraph)
				$ps.each(function() {
					totalHeight += $(this).outerHeight()+15;
					// FAIL totalHeight += $(this).css("margin-bottom");
				});

				$up
					.css({
						// Set height to prevent instant jumpdown when max height is removed
						"height": $up.height(),
						"max-height": 9999
					})
					.animate({
						"height": totalHeight
					});

				// fade out read-more
				$p.fadeOut();
				$('.read-less').fadeIn();

				// prevent jump-down
				return false;

			});

			$(".sidebar-box .read-less-button").click(function() {

				// IE 7 doesn't even get this far. I didn't feel like dicking with it.

				$el = $(this);
				$p  = $el.parent();
				$up = $p.parent();
				totalHeight = $up.height();

				$up
					.css({
						// Set height to prevent instant jumpdown when max height is removed
						"height": totalHeight,
						"max-height": 9999
					})
					.animate({
						"height": $orgHeight
					});

				// fade out read-less
				$p.fadeOut();
				$('.read-more').fadeIn();

				// prevent jump-down
				return false;

			});

		});
