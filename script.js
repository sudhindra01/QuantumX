function submitForm() {
    var questionInput = document.getElementById('questionInput');
    console.log("hello world");

    
    if (questionInput.value.trim() !== '') {
        
        alert('Question submitted: ' + questionInput.value);
        

        
        questionInput.value = '';
    }
}

document.getElementById('questionInput').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        console.log(questionInput);
        submitForm();
    }
});
