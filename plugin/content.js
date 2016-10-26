chrome.runtime.onMessage.addListener(function (msg, sender, sendResponse) {
    if (msg.text === 'get_content') {
        sendResponse(document.body.innerText);
    }
});
