document.getElementById("mybutton").onclick = async function() {
  let response = await fetch("http://localhost:8000/cgi-bin/handle_request.py");
  let text = await response.text();
  alert(text);
}