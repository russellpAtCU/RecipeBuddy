$(document).ready(function() {
    
    var steps = '';

    $("#create").click(function() {
        $("<li>").each(function() {
            steps += steps + ',';
            console.log(steps);
        });
        $.ajax({
            method: "POST",
            url: "{% url 'recipe' %}",
            data: {'instructions' : steps.join(',')}
        })
    })
});



