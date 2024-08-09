function makePrediction() {
    // Collect data from the form
    const data = {
        additives_n: parseFloat(document.getElementById('additives_n').value),
        fat_100g: parseFloat(document.getElementById('fat_100g').value),
        saturated_fat_100g: parseFloat(document.getElementById('saturated_fat_100g').value),
        carbohydrates_100g: parseFloat(document.getElementById('carbohydrates_100g').value),
        sugars_100g: parseFloat(document.getElementById('sugars_100g').value),
        fiber_100g: parseFloat(document.getElementById('fiber_100g').value),
        proteins_100g: parseFloat(document.getElementById('proteins_100g').value),
        sodium_100g: parseFloat(document.getElementById('sodium_100g').value)
    };

    // Send data to Flask backend
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        // Display the result
        document.getElementById('result').innerHTML = 'Result: ' + data.message;
    })
    .catch(error => console.error('Error:', error));
}