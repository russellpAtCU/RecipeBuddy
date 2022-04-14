$(document).ready(function() {
    var steps = [];
    $("<li>").each(function() {
        steps.push($(this).text());
    });
    $("#create").click(function() {
        $.ajax({
            url: "{% url 'recipe/<uuid:id>' %}",
            type: "POST",
            data: steps
        })
    })
});



