// Zarqand: mobile menu, booking form that opens Telegram with a prefilled message, menu category bar.

// Restoranning Telegram username'i, @ belgisisiz. Bo'sh bo'lsa forma ogohlantirish ko'rsatadi.
const TELEGRAM_USERNAME = "";

// --- mobile menu ---
const nav = document.querySelector(".nav");
const burger = document.querySelector(".burger");
burger.addEventListener("click", () => {
  const open = nav.classList.toggle("open");
  burger.setAttribute("aria-expanded", String(open));
  burger.setAttribute("aria-label", open ? "Menyuni yopish" : "Menyuni ochish");
});
nav.querySelectorAll(".links a").forEach((a) =>
  a.addEventListener("click", () => {
    nav.classList.remove("open");
    burger.setAttribute("aria-expanded", "false");
  })
);

// --- booking form (landing only) ---
const form = document.getElementById("bron-form");
if (form) {
  const status = document.getElementById("form-status");
  const dateInput = form.elements.date;

  const today = new Date();
  const iso = (d) => new Date(d.getTime() - d.getTimezoneOffset() * 60000).toISOString().slice(0, 10);
  dateInput.min = iso(today);
  dateInput.value = iso(today);

  const phoneDigits = (v) => v.replace(/\D/g, "").replace(/^998/, "");

  const checks = {
    name: (v) => v.trim().length >= 2,
    phone: (v) => phoneDigits(v).length === 9,
    date: (v) => Boolean(v) && v >= dateInput.min,
  };

  function validate(field) {
    const ok = checks[field.name](field.value);
    field.closest(".f").classList.toggle("err", !ok);
    field.setAttribute("aria-invalid", String(!ok));
    return ok;
  }

  Object.keys(checks).forEach((name) =>
    form.elements[name].addEventListener("input", (e) => {
      if (e.target.closest(".f").classList.contains("err")) validate(e.target);
    })
  );

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const fields = Object.keys(checks).map((n) => form.elements[n]);
    const bad = fields.filter((f) => !validate(f));
    if (bad.length) {
      bad[0].focus();
      status.textContent = "Belgilangan maydonlarni to‘ldiring.";
      return;
    }

    const d = form.elements;
    const date = new Date(d.date.value).toLocaleDateString("uz-UZ", { day: "numeric", month: "long" });
    const text = [
      "Assalomu alaykum! Stol band qilmoqchiman.",
      `Ism: ${d.name.value.trim()}`,
      `Telefon: +998 ${phoneDigits(d.phone.value)}`,
      `Sana: ${date}, soat ${d.time.value}`,
      `Mehmonlar: ${d.guests.value} kishi`,
    ].join("\n");

    if (!TELEGRAM_USERNAME) {
      status.textContent = "Telegram manzili hali ulanmagan. Iltimos, telefon orqali bog‘laning.";
      return;
    }
    status.textContent = "Telegram ochilmoqda…";
    window.open(`https://t.me/${TELEGRAM_USERNAME}?text=${encodeURIComponent(text)}`, "_blank", "noopener");
  });
}

// --- menu page: highlight the category in view ---
const catLinks = [...document.querySelectorAll(".catbar a")];
if (catLinks.length) {
  // entrance for the parts of each section, staggered within the section
  if (!matchMedia("(prefers-reduced-motion: reduce)").matches) {
    document.documentElement.classList.add("js");
    const rise = new IntersectionObserver(
      (entries) =>
        entries.forEach((en) => {
          if (!en.isIntersecting) return;
          en.target.classList.add("shown");
          rise.unobserve(en.target);
        }),
      { rootMargin: "0px 0px -8% 0px" }
    );
    document.querySelectorAll("main section").forEach((sec) =>
      sec.querySelectorAll(".h2, .lede, .note, .pic, .arch-wrap, .grp h3, .it, .dcol").forEach((el, i) => {
        el.classList.add("rv");
        el.style.transitionDelay = `${(i % 8) * 70}ms`;
        rise.observe(el);
      })
    );
  }

  const byId = new Map(catLinks.map((a) => [a.hash.slice(1), a]));
  const spy = new IntersectionObserver(
    (entries) => {
      entries.forEach((en) => {
        if (!en.isIntersecting) return;
        catLinks.forEach((a) => a.classList.remove("on"));
        const link = byId.get(en.target.id);
        link.classList.add("on");
        const bar = link.closest("ul");
        if (link.offsetLeft < bar.scrollLeft || link.offsetLeft + link.offsetWidth > bar.scrollLeft + bar.clientWidth)
          bar.scrollTo({ left: link.offsetLeft - 20, behavior: "smooth" });
      });
    },
    { rootMargin: "-40% 0px -55% 0px" }
  );
  byId.forEach((_, id) => spy.observe(document.getElementById(id)));
}
