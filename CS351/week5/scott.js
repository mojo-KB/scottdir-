$(document).ready(function () {
        $('ul.nav > li').click(function (e) {
            e.preventDefault();
            $('ul.nav > li').removeClass('active');
            $(this).addClass('active');                
 	    //alert('MYNAV:' + e);
	    //alert('Value: ' + $(a, this).attr('value'));
	    //alert('Value: ' + $(this).find('a').attr('value'));
 	    var myValue=$(this).find('a').attr('value');
	    // Run ATAC may altready have been selected or this may be the first run
	    // If this is the first time, Just show the Pick Tesstcase Row
	    // Otherwise, show the state of Run ATAC from the last use
	    // 1) If testcase wasn't submitted, just show the testcase line
	    // 2) testcase was submitted, hide Pick Testcase line and 
	    //    display any outputs which have been created (maybe none)
	    //    Each output will have a canvas and a link to it in the
	    //    left column.
	    //    When an output canvas has been created, the data set (.dat)
	    //    file for the canvas is removed from the display.
	    //    Each canvas has associated with it a control panel
	    //    that can control WebGL variables, including animation.
	    if (myValue == 'display') {
		initDisplay();
		//alert('it was help');
	    }
	    if (myValue == 'run') {
		initRun();
	    }
	    if (myValue == 'help') {
		initHelp();
	    }
	    if (myValue == 'contact') {
		initContact();
	    }
	    if (myValue == 'home') {
		initHome();
	    }
        });            
    });
