let RunSentimentAnalysis = () => {
    const textToAnalyze = document.getElementById("textToAnalyze").value;

    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4) {
            if (this.status === 200) {
                document.getElementById("system_response").innerHTML = this.responseText;
            } else if (this.status === 400) {
                document.getElementById("system_response").innerHTML = this.responseText;
            }
        }
    };
    xhttp.open(
        "GET",
        "/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze),
        true
    );
    xhttp.send();
};
