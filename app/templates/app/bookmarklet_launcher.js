// Launcher Script

(function () {
  if (!window.bookmarklet) {
    bookmarklet_js = document.body.appendChild(
      document.createElement("script")
    );

    // TODO: create this file later
    bookmarklet_js.src = `//127.0.0.1:8000/static/js/bookmarklet.js?r=${Math.floor(
      Math.random() * 999999999999999 // to prevent browser from loading the file from the browser's cache
      // also to make sure the bookmarklet runs the most up-to-date js code
    )}`;
  } else {
    bookmarkletLaunch();
  }
})();
