document.addEventListener("DOMContentLoaded", function () {
  /* ---------- Mobile nav toggle ---------- */
  var navToggle = document.getElementById("navToggle");
  var navLinks = document.getElementById("navLinks");
  if (navToggle && navLinks) {
    navToggle.addEventListener("click", function () {
      navLinks.classList.toggle("is-open");
    });
    navLinks.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        navLinks.classList.remove("is-open");
      });
    });
  }

  /* ---------- Generic tab switcher (courses + schedule) ---------- */
  document.querySelectorAll("[data-tabs]").forEach(function (group) {
    var buttons = group.querySelectorAll("[data-tab-target]");
    var panels = document.querySelectorAll(
      '[data-tab-panel][data-tabs-group="' + group.getAttribute("data-tabs") + '"]'
    );
    buttons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var target = btn.getAttribute("data-tab-target");
        buttons.forEach(function (b) { b.classList.remove("is-active"); });
        panels.forEach(function (p) { p.classList.remove("is-active"); });
        btn.classList.add("is-active");
        var panel = document.querySelector(
          '[data-tab-panel="' + target + '"][data-tabs-group="' + group.getAttribute("data-tabs") + '"]'
        );
        if (panel) panel.classList.add("is-active");
      });
    });
  });

  /* ---------- Reveal on scroll ---------- */
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && reveals.length) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("is-visible"); });
  }

  /* ---------- Animated stat counters ---------- */
  var counters = document.querySelectorAll("[data-count-to]");
  var prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (counters.length) {
    var counterObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          var el = entry.target;
          var target = parseInt(el.getAttribute("data-count-to"), 10);
          var suffix = el.getAttribute("data-suffix") || "";
          if (prefersReducedMotion) {
            el.textContent = target + suffix;
          } else {
            var current = 0;
            var duration = 1100;
            var startTime = null;
            function step(ts) {
              if (!startTime) startTime = ts;
              var progress = Math.min((ts - startTime) / duration, 1);
              current = Math.floor(progress * target);
              el.textContent = current + suffix;
              if (progress < 1) requestAnimationFrame(step);
              else el.textContent = target + suffix;
            }
            requestAnimationFrame(step);
          }
          counterObserver.unobserve(el);
        });
      },
      { threshold: 0.4 }
    );
    counters.forEach(function (el) { counterObserver.observe(el); });
  }

  /* ---------- Terminal typing effect ---------- */
  var termBody = document.getElementById("terminalBody");
  if (termBody) {
    var lines = [
      { type: "cmd", text: "whoami" },
      { type: "out", text: "นักศึกษาสาขาวิชาวิทยาการคอมพิวเตอร์" },
      { type: "cmd", text: "ls ./skills" },
      { type: "out", text: "software-dev/  ai-data-science/  cyber-security/" },
      { type: "cmd", text: "./build_your_future.sh" },
      { type: "out", text: "กำลังคอมไพล์อนาคตของคุณ... เสร็จสมบูรณ์ ✓" }
    ];

    if (prefersReducedMotion) {
      renderStatic();
    } else {
      typeLoop();
    }

    function renderStatic() {
      termBody.innerHTML = "";
      lines.forEach(function (line) {
        var row = document.createElement("div");
        if (line.type === "cmd") {
          row.className = "terminal__line";
          row.innerHTML = '<span class="terminal__prompt">$</span><span class="terminal__cmd">' + line.text + "</span>";
        } else {
          row.className = "terminal__out";
          row.textContent = line.text;
        }
        termBody.appendChild(row);
      });
    }

    function typeLoop() {
      termBody.innerHTML = "";
      var i = 0;

      function typeLine() {
        if (i >= lines.length) {
          setTimeout(function () {
            typeLoop();
          }, 2200);
          return;
        }
        var line = lines[i];
        var row = document.createElement("div");

        if (line.type === "cmd") {
          row.className = "terminal__line";
          var prompt = document.createElement("span");
          prompt.className = "terminal__prompt";
          prompt.textContent = "$";
          var cmd = document.createElement("span");
          cmd.className = "terminal__cmd";
          row.appendChild(prompt);
          row.appendChild(cmd);
          termBody.appendChild(row);
          typeChars(cmd, line.text, function () {
            i++;
            setTimeout(typeLine, 260);
          });
        } else {
          row.className = "terminal__out";
          termBody.appendChild(row);
          typeChars(row, line.text, function () {
            i++;
            setTimeout(typeLine, 260);
          });
        }
      }

      function typeChars(el, text, done) {
        var idx = 0;
        var caret = document.createElement("span");
        caret.className = "caret";
        el.appendChild(caret);
        var interval = setInterval(function () {
          if (idx < text.length) {
            caret.insertAdjacentText("beforebegin", text[idx]);
            idx++;
          } else {
            clearInterval(interval);
            caret.remove();
            done();
          }
        }, 26);
      }

      typeLine();
    }
  }

  /* ---------- Contact form (front-end only) ---------- */
  var contactForm = document.getElementById("contactForm");
  if (contactForm) {
    contactForm.addEventListener("submit", function (e) {
      e.preventDefault();
      var success = document.getElementById("formSuccess");
      if (success) {
        success.classList.add("is-visible");
        setTimeout(function () { success.classList.remove("is-visible"); }, 5000);
      }
      contactForm.reset();
    });
  }
});
