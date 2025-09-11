It takes the parameters of a used car such as the company name, model name, year of purchase, fuel type, and the number of kilometers driven.

It then predicts the possible price of the car based on these inputs.

How does this project work?

The data was initially scraped from an online marketplace for used cars.

The raw data was cleaned and analyzed thoroughly to make it usable.

A Linear Regression model was trained on this cleaned data, achieving a strong performance with an R² score of 0.92.

Finally, this model was integrated into a Flask-based web application, allowing users to enter car details and receive price predictions in real-time.