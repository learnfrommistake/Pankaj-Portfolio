gsap.registerPlugin(ScrollTrigger);

/* LOADER */
window.addEventListener("load", () => {
  gsap.to(".loader", {
    opacity: 0,
    duration: 1,
    delay: 0.5,
    onComplete: () => {
      document.querySelector(".loader").style.display = "none";
    },
  });
});

/* HERO */
gsap.from(".hero h1", { y: 50, opacity: 0, duration: 1.4 });
gsap.from(".hero p", { y: 30, opacity: 0, delay: 0.5 });

/* SCROLL */
gsap.utils.toArray(".fade-up").forEach((el) => {
  gsap.to(el, {
    scrollTrigger: { trigger: el, start: "top 85%" },
    opacity: 1,
    y: 0,
    duration: 1,
  });
});

/* CURSOR */
const glow = document.querySelector(".cursor-glow");
window.addEventListener("mousemove", (e) => {
  glow.style.top = e.clientY + "px";
  glow.style.left = e.clientX + "px";
});

/* THEME */
function toggleTheme() {
  document.body.classList.toggle("light");
}
