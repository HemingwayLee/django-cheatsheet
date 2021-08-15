const about = "<h1>I am About Page.</h1>";
const home = "<h1>I am home Page.</h1>";
const contact = "<h1>I am contact Page.</h1>";
const notfound = "<h1>404, not found.</h1>";
const routes = {
  '/' : home,
  '/home' : home,
  '/contact' : contact,
  '/about' : about,
  '/404': notfound,
};

const onNavigate = (pathname, tagId) => {
  window.history.pushState(
    {},
    pathname,
    window.location.origin + pathname
  );
  document.getElementById(tagId).innerHTML = routes[pathname];
}
