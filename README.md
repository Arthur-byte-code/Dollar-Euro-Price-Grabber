### Dollar-Euro Price Grabber
![D E](https://github.com/Arthur-byte-code/Dollar-Euro-Price-Grabber/assets/152222113/69923a41-e566-4d84-be7a-14f35c3d8e65)

This Python code creates a desktop application using the Tkinter library for graphical interface. The application allows the user to search for the price of the dollar and the euro on the web using the Microsoft Edge browser and displays the chosen currency's value and its multiplications from 2 to 10.

#### Step-by-Step Explanation:

1. **Libraries Used:**
   - `pyautogui`: Controls the mouse and keyboard.
   - `time`: Adds pauses.
   - `pyperclip`: Copies and pastes texts to the clipboard.
   - `tkinter`: Creates the graphical interface.

2. **Function Definitions:**
   - `SearchDolar()`: Searches for the dollar price.
   - `SearchEuro()`: Searches for the euro price.
   Both functions perform the same actions but for different currencies.

3. **Search Functions:**
   - Presses the "Win" key to open the Start menu.
   - Types "microsoft edge" to open the Microsoft Edge browser.
   - Types "google" in the address bar and presses Enter to open Google.
   - Types "valor do dólar" or "valor do euro" in the Google search bar and presses Enter to search for the desired currency's price.
   - Clicks on a specific position on the screen to select the currency price value.
   - Copies the selected value to the clipboard.
   - Converts the copied value to a floating-point number.
   - Prints the currency value to the console.
   - Calculates the currency multiplications from 2 to 10 and stores the results in a formatted string.

4. **Graphical Interface:**
   - Uses Tkinter to create a GUI with two labels to display the chosen currency's value and its multiplications, respectively, and two buttons to search for the prices of the dollar and the euro.

5. **Main Loop:**
   - Starts the main loop (`mainloop()`) to display the graphical interface and wait for user interaction.

