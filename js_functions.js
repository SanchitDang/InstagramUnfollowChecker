let allTexts = [];

// Find the target div element
const targetDiv = document.querySelector("div.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6");

function collectTexts() {
    if (targetDiv) {
        // Select all span elements with the specified class inside the target div
        const spans = targetDiv.querySelectorAll("span._ap3a._aaco._aacw._aacx._aad7._aade");

        // Collect text from each span and add it to the array if not already present
        spans.forEach(span => {
            const textContent = span.textContent.trim();
            if (!allTexts.includes(textContent)) {
                allTexts.push(textContent);
            }
        });

        // Log all collected texts
        console.log("All texts collected:", allTexts);
    } else {
        console.log("Target div not found.");
    }
}

// Run the function to collect texts
collectTexts();


///////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////


// Array to store collected texts
let allTexts2 = [];

// Find the target div element
const targetDiv2 = document.querySelector("div.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6");

function scrollDivAndCollect() {
    if (targetDiv2) {
        // Select all span elements with the specified class inside the target div
        const spans = targetDiv2.querySelectorAll("span._ap3a._aaco._aacw._aacx._aad7._aade");
        
        // Collect text from each span and add it to the array if not already present
        spans.forEach(span => {
            const textContent = span.textContent.trim();
            if (!allTexts2.includes(textContent)) {
                allTexts2.push(textContent);
            }
        });

    
    } else {
        console.log("Target div not found.");
    }
}

// Start the scroll and collection process
scrollDivAndCollect();