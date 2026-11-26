(function () {
  "use strict";
  document.documentElement.classList.add("js");

  var kopf = document.querySelector("[data-kopf]");
  var knopf = document.querySelector("[data-menue-knopf]");
  var menue = document.querySelector("[data-menue]");
  var text = document.querySelector("[data-menue-text]");

  function setzeMenue(offen) {
    knopf.setAttribute("aria-expanded", String(offen));
    menue.hidden = !offen;
    text.textContent = offen ? "Schließen" : "Menü";
  }
  if (knopf && menue) {
    knopf.addEventListener("click", function () { setzeMenue(knopf.getAttribute("aria-expanded") !== "true"); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && !menue.hidden) { setzeMenue(false); knopf.focus(); }
    });
    window.matchMedia("(min-width: 861px)").addEventListener("change", function (m) { if (m.matches) setzeMenue(false); });
  }

  function scroll() { if (kopf) kopf.classList.toggle("ist-gescrollt", window.scrollY > 8); }
  window.addEventListener("scroll", scroll, { passive: true });
  scroll();

  var ziele = document.querySelectorAll(".zeige");
  if ("IntersectionObserver" in window && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    var io = new IntersectionObserver(function (eintraege) {
      eintraege.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("ist-sichtbar"); io.unobserve(e.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px" });
    ziele.forEach(function (z) { io.observe(z); });
  } else {
    ziele.forEach(function (z) { z.classList.add("ist-sichtbar"); });
  }
})();
