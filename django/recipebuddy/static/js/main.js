$(document).ready(function() {
    
    var steps = '';

    $("#create").click(function() {
        $("<li>").each(function() {
            steps += steps + ',';
            console.log(steps);
        });
    })
});



