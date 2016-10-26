function get_content(dom) {
    d = document;
    var f = d.createElement('form');
    f.action = "http://localhost:5000/ishate"
    f.method = 'post';
    var i = d.createElement('input');
    i.type = 'hidden';
    i.name = 'text';
    i.value = dom;
    f.appendChild(i);
    d.body.appendChild(f);
    f.submit();
}

document.addEventListener('DOMContentLoaded', function() {
  var checkPageButton = document.getElementById('checkPage');
  checkPageButton.addEventListener('click', function() {
    
    chrome.tabs.getSelected(null, function(tab) {
      chrome.tabs.sendMessage(tab.id, {text: 'get_content'}, get_content);
    });
  }, false);
}, false);
