Currency Converter - Expected Functionality

1️⃣ User Input
	•	Users can enter an amount in their desired currency.
	•	Users select the “from” and “to” currencies from a dropdown.

2️⃣ API Integration
	•	The app fetches real-time exchange rates from a public currency API.
	•	It sends a request with the selected currencies and amount.

3️⃣ Currency Conversion
	•	The backend calculates the converted amount based on the fetched exchange rate.
	•	Returns the result as JSON.

4️⃣ Display Results
	•	The frontend updates dynamically to show the converted amount.
	•	May also display the current exchange rate.

5️⃣ Error Handling
	•	Handles invalid inputs (e.g., empty fields, non-numeric values).
	•	Displays an error if the API request fails.