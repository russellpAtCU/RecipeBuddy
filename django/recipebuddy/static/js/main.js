const handlePostData = () => {
    $.ajax({
        type: 'POST',
        url: '/app/create-account/',
        success: function(response) {
            console.log(response)
        },
        error: function(error) {
            console.log(error)
        }
    })
}



