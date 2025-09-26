<script src="{{ https://assets.calendly.com/assets/external/widget.js }}" type="text/javascript" async></script>
    <script src="https://unpkg.com/aos@next/dist/aos.js"></script>
        // hamburger
        const hamburger = document.querySelector('.hamburger');
        const navMenu = document.querySelector('.nav-menu');

        hamburger.addEventListener('click', () =>{
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
        })
        document.querySelectorAll('.nav-link').forEach(n => n.addEventListener('click', () => {
            hamburger.classList.remove('active');
            navMenu.classList.remove('active');
        }));

        // navbar
        window.addEventListener('scroll', function(){
            const navbar = document.querySelector('.nav-bar');
            const scrolled = window.pageYOffset;

            if (scrolled > 50) {
                navbar.classList.add('scrolled');
            }else{
                navbar.classList.remove('scrolled');
            }
        })

        //scrolled
        AOS.init({
            duration: 2000,
        });

        window.addEventListener("scroll", function(){
            const navbar = document.querySelector(".nav-bar");
            navbar.classList.toggle("scrolled",window.scrollY>50);
        });

        //typewriter
        const text = "We're building a zero-waste, peer-to-peer marketplace where students buy, sell and exchange books, clothes, gadgets and more safely, affordably and sustainably all through local campus pick-up zones";   // the phrase
        const typewriter = document.querySelector(".typeWriter");
        let i = 0;  // which letter we are on

        function type() {
            if (i < text.length) {
            typewriter.textContent += text.charAt(i); // add one letter
            i++;
            setTimeout(type, 50); // typing speed (100ms per letter)
            }
        }

        type();

        // app.js
function loadCalendly() {
    return new Promise((resolve) => {
        const script = document.createElement("script");
        script.src = "https://assets.calendly.com/assets/external/widget.js";
        script.async = true;
        script.onload = resolve;
        document.body.appendChild(script);
    });
}

document.addEventListener("DOMContentLoaded", async () => {
    await loadCalendly();

    const bookCallBtn = document.querySelector("#bookCall button");

    if (bookCallBtn) {
        bookCallBtn.addEventListener("click", (e) => {
            e.preventDefault();
            Calendly.initPopupWidget({
                url: "https://calendly.com/benedictanwachukwu456"
            });
        });
    }
});


document.addEventListener('DOMContentLoaded', () => {
  const flashes = document.querySelectorAll('.flash-messages .flash');

  flashes.forEach(flash => {
    // auto-hide after 4s
    const timeout = setTimeout(() => hideFlash(flash), 40);

    // close button
    const btn = flash.querySelector('.flash-close');
    if (btn) {
      btn.addEventListener('click', () => {
        clearTimeout(timeout);
        hideFlash(flash);
      });
    }
  });

  function hideFlash(el) {
    el.classList.add('hide');
    // remove from DOM after transition
    el.addEventListener('transitionend', () => {
      if (el.parentNode) el.parentNode.removeChild(el);
    }, { once: true });
  }
});

setTimeout(() => {
    document.querySelectorAll('.flash').forEach(flash => {
      flash.style.display = 'none';
    });
}, 10);
