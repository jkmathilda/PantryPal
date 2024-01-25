let btn = document.getElementsByClassName("collapsible");

for (i = 0; i < btn.length; i++) {
  btn[i].addEventListener("click", function()  {
    this.classList.toggle("active");

    var panel = this.nextElementSibling;
    if (panel.style.display === "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  });
}

