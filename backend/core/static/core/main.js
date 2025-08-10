// core/static/core/main.js - THE FINAL HOMEPAGE VERSION (CORRECTED)

document.addEventListener('DOMContentLoaded', function() {
    
    // Check if GSAP and ScrollTrigger are loaded.
    if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') {
        console.error('GSAP or ScrollTrigger is not loaded. Make sure the script tags are in your base.html.');
        return;
    }

    gsap.registerPlugin(ScrollTrigger);

    // --- Hero Text Animation ---
    const heroTitle = document.querySelector('.hero-title');
    if (heroTitle) {
        gsap.from(heroTitle, {
            duration: 1,
            yPercent: 100,
            ease: 'power4.out',
            delay: 0.2
        });
    }
    
    // --- General Fade-in Animations (for single elements) ---
    const fadeElements = gsap.utils.toArray('.fade-in');
    fadeElements.forEach(el => {
        gsap.from(el, {
            duration: 1,
            autoAlpha: 0,
            y: 20,
            ease: 'power3.out',
            delay: 0.5,
            scrollTrigger: {
                trigger: el,
                start: 'top 85%',
                toggleActions: 'play none none none'
            }
        });
    });

    // --- Text Mask Reveal Animation for Section Headings ---
    const revealHeadings = gsap.utils.toArray('.reveal-heading');
    revealHeadings.forEach(heading => {
        gsap.from(heading, {
            yPercent: 100,
            duration: 1,
            ease: 'power4.out',
            scrollTrigger: {
                trigger: heading.closest('.section-heading-wrapper'),
                start: 'top 90%',
                toggleActions: 'play none none none'
            }
        });
    });

    // --- Feature Card & Live Blueprint Animation ---
    const featureGridSection = document.querySelector('.feature-grid-section');
    if (featureGridSection) {
        const cards = gsap.utils.toArray('.feature-card');
        const line = document.querySelector('#line-1');

        if (line) {
            const length = line.getTotalLength();
            gsap.set(line, { strokeDasharray: length, strokeDashoffset: length });
        }
        
        let tl = gsap.timeline({
            scrollTrigger: {
                trigger: featureGridSection,
                start: 'top 60%',
                toggleActions: 'play none none none'
            }
        });

        tl.fromTo(cards, 
            { autoAlpha: 0, y: 50 }, 
            { duration: 1, autoAlpha: 1, y: 0, ease: 'power3.out', stagger: 0.2 }
        );
        
        if (line) {
            tl.to(line, { strokeDashoffset: 0, duration: 1.5, ease: 'power2.inOut' }, "-=0.8");
        }
    }

    // --- 3D Interactive Card Tilt Effect ---
    const interactiveCards = document.querySelectorAll('.feature-card');
    interactiveCards.forEach(card => {
        const maxRotation = 8;
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const rotateX = -gsap.utils.mapRange(0, rect.height, -maxRotation, maxRotation, y);
            const rotateY = gsap.utils.mapRange(0, rect.width, -maxRotation, maxRotation, x);
            gsap.to(card, { duration: 0.4, rotationX: rotateX, rotationY: rotateY, transformPerspective: 1000, ease: 'power2.out' });
        });
        card.addEventListener('mouseleave', () => {
            gsap.to(card, { duration: 0.8, rotationX: 0, rotationY: 0, ease: 'elastic.out(1, 0.5)' });
        });
    });

    // --- Manifesto Section Animation ---
    const manifesto = document.querySelector('.manifesto-content');
    if (manifesto) {
        gsap.from(manifesto, {
            autoAlpha: 0,
            scale: 0.95,
            duration: 1.5,
            ease: 'power3.out',
            scrollTrigger: {
                trigger: manifesto,
                start: 'top 80%'
            }
        });
    }

    // --- THE FIX IS APPLIED HERE: Using robust fromTo() for all staggered animations ---
    // --- How It Works Section Animation ---
    const steps = gsap.utils.toArray('.step-item');
    if (steps.length > 0) {
        gsap.fromTo(steps, 
            { autoAlpha: 0, y: 50 },
            {
                autoAlpha: 1,
                y: 0,
                duration: 1,
                ease: 'power3.out',
                stagger: 0.2,
                scrollTrigger: {
                    trigger: '.steps-grid',
                    start: 'top 80%'
                }
            }
        );
    }

    // --- Founders Section Animation ---
    const founders = gsap.utils.toArray('.founder-profile');
    if (founders.length > 0) {
        gsap.fromTo(founders,
            { autoAlpha: 0, y: 50 },
            {
                autoAlpha: 1,
                y: 0,
                duration: 1,
                ease: 'power3.out',
                stagger: 0.3,
                scrollTrigger: {
                    trigger: '.founders-grid',
                    start: 'top 80%'
                }
            }
        );
    }
    
    // --- Unfair Advantage Section Animation ---
    const advantageCards = gsap.utils.toArray('.advantage-card');
    if (advantageCards.length > 0) {
        gsap.fromTo(advantageCards, 
            { autoAlpha: 0, y: 50 }, 
            {
                autoAlpha: 1,
                y: 0,
                duration: 1,
                ease: 'power3.out',
                stagger: 0.2,
                scrollTrigger: {
                    trigger: '.advantage-grid',
                    start: 'top 80%'
                }
            }
        );
    }

    // --- Accordion for FAQ ---
    const accordionItems = document.querySelectorAll('.accordion-item');
    accordionItems.forEach(item => {
        const header = item.querySelector('.accordion-header');
        const content = item.querySelector('.accordion-content');
        gsap.set(content, { maxHeight: 0, autoAlpha: 0 });
        header.addEventListener('click', () => {
            accordionItems.forEach(otherItem => {
                if (otherItem !== item && otherItem.classList.contains('active')) {
                    otherItem.classList.remove('active');
                    gsap.to(otherItem.querySelector('.accordion-content'), { maxHeight: 0, duration: 0.3, ease: 'power2.inOut', autoAlpha: 0 });
                }
            });
            if (item.classList.contains('active')) {
                item.classList.remove('active');
                gsap.to(content, { maxHeight: 0, duration: 0.3, ease: 'power2.inOut', autoAlpha: 0 });
            } else {
                item.classList.add('active');
                gsap.to(content, { maxHeight: content.scrollHeight, duration: 0.4, ease: 'power2.out', autoAlpha: 1 });
            }
        });
    });

});