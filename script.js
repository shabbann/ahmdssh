const canvas = document.getElementById('star-canvas');
const ctx = canvas.getContext('2d');

// Define the color palette for the stars (RGB values)
const whiteColor = '255, 255, 255';
const otherColors = [
    '255, 165, 0',   // Orange
    '173, 216, 230', // Blue
    '255, 255, 0',   // Yellow
    '255, 99, 71'    // Red
];

let stars = [];
let numStars = 750;

function setCanvasSize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    numStars = Math.floor((canvas.width * canvas.height) / 500); // Adjust star density based on screen size
}

// Star object
function Star(x, y, radius, opacity, color) {
    this.x = x;
    this.y = y;
    this.radius = radius;
    this.opacity = opacity;
    this.color = color; // Assign the star's color
    this.fading = 'in'; // 'in' or 'out'

    this.draw = function() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        // Use the star's assigned color with its current opacity
        ctx.fillStyle = `rgba(${this.color}, ${this.opacity})`;
        ctx.fill();
    }

    this.update = function() {
        // This controls the speed of the twinkle effect.
        const fadeSpeed = 0.0007; 

        if (this.fading === 'in') {
            this.opacity += fadeSpeed;
            if (this.opacity >= 1) {
                this.fading = 'out';
            }
        } else { // fading out
            this.opacity -= fadeSpeed;
            if (this.opacity <= 0.1) {
                // Reset star to a new position to keep the sky populated
                this.x = Math.random() * canvas.width;
                this.y = Math.random() * canvas.height;
                this.fading = 'in';
            }
        }
        this.draw();
    }
}

function createStars() {
    stars = [];
    for (let i = 0; i < numStars; i++) {
        const x = Math.random() * canvas.width;
        const y = Math.random() * canvas.height;
        const radius = Math.random() * 1.5;
        const opacity = Math.random();
        
        let color;
        // With a 75% chance, make the star white.
        if (Math.random() < 0.75) {
            color = whiteColor;
        } else {
            // Otherwise, pick a random color from the other options.
            color = otherColors[Math.floor(Math.random() * otherColors.length)];
        }

        stars.push(new Star(x, y, radius, opacity, color));
    }
}

function animate() {
    requestAnimationFrame(animate);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    stars.forEach(star => {
        star.update();
    });
}

// Initial setup
setCanvasSize();
createStars();
animate();

// Handle window resize
window.addEventListener('resize', () => {
    setCanvasSize();
    createStars();
});
