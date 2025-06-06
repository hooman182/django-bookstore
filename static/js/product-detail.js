// Image gallery functionality
function setupImageGallery() {
    const mainImage = document.querySelector('.main-image img');
    const thumbnails = document.querySelectorAll('.thumbnail-images img');

    thumbnails.forEach(thumbnail => {
        thumbnail.addEventListener('click', function() {
            // Swap the main image with the clicked thumbnail
            const tempSrc = mainImage.src;
            mainImage.src = this.src;
            this.src = tempSrc;

            // Add active class to the clicked thumbnail
            thumbnails.forEach(thumb => thumb.classList.remove('active'));
            this.classList.add('active');
        });
    });
}

// Initialize the gallery when the page loads
document.addEventListener('DOMContentLoaded', setupImageGallery);
