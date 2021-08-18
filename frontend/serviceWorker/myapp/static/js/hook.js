self.addEventListener('fetch', function (event) {
  var myheaders = {
    ywlee: "My Name",
    who: "ywlee"
  };

  for (var entry of event.request.headers.entries()) {
    myheaders[entry[0]] = entry[1];
  }

  console.log(myheaders);

  var req = new Request(event.request, {
    headers: {
      ...event.request.headers,
      ywlee: "My Name",
      who: "ywlee"
    }
  });

  event.respondWith(fetch(req));
});
